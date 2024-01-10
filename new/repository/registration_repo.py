from domain.entities import Registration, Person, Event
from repository.person_repo import FilePersonRepo
from repository.event_repo import FileEventRepo


class RegistrationRepo:
    def __init__(self):
        self.__registrations = []

    def find(self, idp, ide):
        """
        Cauta daca persoana cu id-ul dat este inscrisa la evenimentul cu id-ul dat
        :param idp: id dat
        :type idp: str
        :param ide: id dat
        :type ide: str
        :return: inscrierea cu id dat, None daca nu exista
        :rtype: Registration
        """
        for r in self.__registrations:
            if r.getPerson().getID() == idp and r.getEvent().getID() == ide:
                return r
        return None

    def find_index(self, idp, ide):
        """
        Gaseste index-ul (pozitia) la care este inscrierea cu id dat
        :param idp: id persoana
        :type idp: str
        :param ide: id eveniment
        :type ide: str
        :return: pozitia in lista a inscrierii cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        registrations = self.__registrations
        index = -1
        for i in range(self.size()):
            if registrations[i].getPerson().getID() == idp and registrations[i].getEvent().getID() == ide:
                index = i
        return index

    def store(self, registration):
        """
        Adauga o inscriere in lista
        :param registration: inscrierea care se adauga
        :type registration: Registration
        :return: -; lista de inscrieri se modifica prin adaugare
        :rtype:
        :raises: ValueError daca inscrierea exista deja
        """
        if self.find(registration.getPerson().getID(), registration.getEvent().getID()) is not None:
            raise ValueError('Persoana data este deja inscrisa la acest eveniment.')
        self.__registrations.append(registration)

    def size(self):
        """
        Returneaza numarul de inscrieri din repo
        :rtype: int
        """
        return len(self.__registrations)

    def delete(self, idp, ide):
        """
        Sterge inscrierea cu id-ul dat
        :param idp: id persoana
        :type idp: str
        :param ide: id eveniment
        :type ide: str
        :return: inscrierea corespunzatoare, None daca nu exista
        :rtype: Registration
        """
        registrations = self.__registrations
        index = self.find_index(idp, ide)
        registration = self.find(idp, ide)
        if registration is None:
            raise ValueError('Nu exista inscrierea cu aceste date.')
        deleted_reg = registrations.pop(index)
        return deleted_reg

    def get_all_registrations(self):
        """
        Returneaza o lista cu toate inscrierile existente
        :rtype: lista de obiecte de tip Registration
        """
        return self.__registrations

    def delete_all(self):
        self.__registrations = []


# def setup_test_repo3():
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     pers2 = Person('2', 'Blake Brews', 'Second Street')
#     pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
#     pers4 = Person('4', 'Dante D\'Alembert', 'Fourth Street')
#
#     ev1 = Event('1', '01.01.2022', '01:01', 'Date Night')
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     ev3 = Event('3', '03.03.2022', '03:03', 'Dancing Night')
#     ev4 = Event('4', '04.04.2022', '04:04', 'Rock Night')
#     ev5 = Event('5', '05.05.2022', '05:05', 'Salsa Night')
#
#     reg1 = Registration(pers1, ev1)
#     reg2 = Registration(pers1, ev2)
#     reg3 = Registration(pers2, ev1)
#     reg4 = Registration(pers2, ev3)
#     reg5 = Registration(pers3, ev3)
#     reg6 = Registration(pers4, ev5)
#     reg7 = Registration(pers2, ev4)
#
#     test_repo = RegistrationRepo()
#
#     test_repo.store(reg1)
#     test_repo.store(reg2)
#     test_repo.store(reg3)
#     test_repo.store(reg4)
#     test_repo.store(reg5)
#     test_repo.store(reg6)
#     test_repo.store(reg7)
#
#     return test_repo


# def test_find():
#     test_repo = setup_test_repo3()
#
#     r1 = test_repo.find('1', '1')
#     assert (r1.getPerson().getName() == 'Arizona Andrews')
#     assert (r1.getPerson().getAddress() == 'First Street')
#     assert (r1.getEvent().getDate() == '01.01.2022')
#     assert (r1.getEvent().getTime() == '01:01')
#     assert (r1.getEvent().getDesc() == 'Date Night')
#
#     r2 = test_repo.find('8', '8')
#     assert (r2 is None)
#
#
# def test_store():
#     test_repo = RegistrationRepo()
#
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
#     reg1 = Registration(pers3, ev2)
#     test_repo.store(reg1)
#     assert (test_repo.size() == 1)
#
#     ev4 = Event('4', '04.04.2022', '04:04', 'Rock Night')
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     reg2 = Registration(pers1, ev4)
#     test_repo.store(reg2)
#     assert (test_repo.size() == 2)
#
#     try:
#         test_repo.store(reg2)
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_size():
#     test_repo = setup_test_repo3()
#
#     assert (test_repo.size() == 7)
#
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
#     reg1 = Registration(pers3, ev2)
#     test_repo.store(reg1)
#
#     assert (test_repo.size() == 8)
#
#
# def test_get_all_registrations():
#     test_repo = setup_test_repo3()
#
#     crt_reg_list = test_repo.get_all_registrations()
#     assert (type(crt_reg_list) == list)
#     assert (len(crt_reg_list) == 7)
#
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
#     reg1 = Registration(pers3, ev2)
#     test_repo.store(reg1)
#     assert (len(crt_reg_list) == 8)
#
#     assert (test_repo.get_all_registrations()[-1].getPerson().getName() == 'Cleopatra Candy')
#     assert (test_repo.get_all_registrations()[-1].getPerson().getAddress() == 'Third Street')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getDate() == '02.02.2022')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getTime() == '02:02')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getDesc() == 'Drinking Night')
#
#
# test_find()
# test_store()
# test_size()
# test_get_all_registrations()


class FileRegistrationRepo:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de inscrieri din fisier
        :rtype: lista de obiecte de tip Registration
        """
        repo_pers = FilePersonRepo('data/people.txt')
        repo_ev = FileEventRepo('data/events.txt')

        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        registrations = []
        for line in lines:
            id_pers, id_ev = [token.strip() for token in line.split('; ')]
            p = repo_pers.find(id_pers)
            e = repo_ev.find(id_ev)
            r = Registration(p, e)
            registrations.append(r)
        f.close()
        return registrations

    def save_to_file(self, registrations):
        """
        Salveaza inscrierile in fisier
        :param registrations: lista cu inscrieri
        """
        with open(self.__filename, 'w') as f:
            for reg in registrations:
                reg_str = str(reg.getPerson().getID()) + '; ' + str(reg.getEvent().getID()) + '\n'
                f.write(reg_str)

    def size(self):
        """
        Returneaza numarul de inscrieri din multime
        :return: numar inscrieri existente
        :rtype: int
        """
        return len(self.load_from_file())

    def find(self, idp, ide):
        """
        Cauta persoana cu id-ul dat
        :param idp: id persoana
        :type idp: str
        :param ide: id eveniment
        :type ide: str
        :return: inscrierea corespunzatoare, None daca nu exista
        :rtype: Registration
        """
        registrations = self.load_from_file()
        for reg in registrations:
            if reg.getPerson().getID() == idp and reg.getEvent().getID() == ide:
                return reg
        return None

    def find_index(self, idp, ide):
        """
        Gaseste index-ul (pozitia) la care este inscrierea cu id dat
        :param idp: id persoana
        :type idp: str
        :param ide: id eveniment
        :type ide: str
        :return: pozitia in lista a inscrierii cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        registrations = self.load_from_file()
        index = -1
        for i in range(self.size()):
            if registrations[i].getPerson().getID() == idp and registrations[i].getEvent().getID() == ide:
                index = i
        return index

    def store(self, registration):
        """
        Adauga o inscriere in lista
        :param registration: inscrierea care se adauga
        :type registration: Registration
        :return: -; lista de inscrieri se modifica prin adaugare
        :rtype:
        :raises: ValueError daca inscrierea exista deja
        """
        registrations = self.load_from_file()
        if self.find(registration.getPerson().getID(), registration.getEvent().getID()) is not None:
            raise ValueError('Persoana data este deja inscrisa la acest eveniment.')
        registrations.append(registration)
        self.save_to_file(registrations)

    def delete(self, idp, ide):
        """
        Sterge inscrierea cu id-ul dat
        :param idp: id persoana
        :type idp: str
        :param ide: id eveniment
        :type ide: str
        :return: inscrierea corespunzatoare, None daca nu exista
        :rtype: Registration
        """
        registrations = self.load_from_file()
        index = self.find_index(idp, ide)
        registration = self.find(idp, ide)
        if registration is None:
            raise ValueError('Nu exista inscrierea cu aceste date.')
        deleted_reg = registrations.pop(index)
        self.save_to_file(registrations)
        return deleted_reg

    def get_all_registrations(self):
        """
        Returneaza o lista cu toate inscrierile existente
        :rtype: lista de obiecte de tip Registration
        """
        return self.load_from_file()

    def delete_all(self):
        self.save_to_file([])


# def test_find():
#     test_repo = FileRegistrationRepo('data/test_registrations.txt')
#
#     r1 = test_repo.find('1', '1')
#     assert (r1.getPerson().getName() == 'Arizona Andrews')
#     assert (r1.getPerson().getAddress() == 'First Street')
#     assert (r1.getEvent().getDate() == '01.01.2022')
#     assert (r1.getEvent().getTime() == '01:01')
#     assert (r1.getEvent().getDesc() == 'Movie Night')
#
#     r2 = test_repo.find('8', '8')
#     assert (r2 is None)
#
#
#
# def test_store_w():
#     test_repo = FileRegistrationRepo('data/test_registrations.txt')
#     pers_repo = FilePersonRepo('data/people.txt')
#     ev_repo = FileEventRepo('data/events.txt')
#
#     pers = pers_repo.find('2')
#     ev = ev_repo.find('1')
#     reg = Registration(pers, ev)
#     test_repo.store(reg)
#     assert (test_repo.size() == 7)
#
#     try:
#         test_repo.store(reg)
#         assert False
#     except ValueError:
#         assert True
#
#     test_repo.delete('2', '1')
#
# def test_store_b():
#     test_repo = FileRegistrationRepo('data/test_registrations.txt')
#     pers_repo = FilePersonRepo('data/people.txt')
#     ev_repo = FileEventRepo('data/events.txt')
#
#     pers = pers_repo.find('2')
#     ev = ev_repo.find('1')
#     reg = Registration(pers, ev)
#     test_repo.store(reg)
#     assert (test_repo.size() == 7)
#
#     try:
#         test_repo.store(reg)
#         assert False
#     except ValueError:
#         assert True
#
#     test_repo.delete('2', '1')
#
#
#
# def test_size():
#     test_repo = FileRegistrationRepo('data/test_registrations.txt')
#     pers_repo = FilePersonRepo('data/people.txt')
#     ev_repo = FileEventRepo('data/events.txt')
#
#     assert (test_repo.size() == 6)
#
#     pers = pers_repo.find('3')
#     ev = ev_repo.find('2')
#     reg = Registration(pers, ev)
#     test_repo.store(reg)
#
#     assert (test_repo.size() == 7)
#
#     test_repo.delete('3', '2')
#
#
# def test_get_all_registrations():
#     test_repo = FileRegistrationRepo('data/test_registrations.txt')
#     pers_repo = FilePersonRepo('data/people.txt')
#     ev_repo = FileEventRepo('data/events.txt')
#
#     crt_reg_list = test_repo.get_all_registrations()
#     assert (type(crt_reg_list) == list)
#     assert (len(crt_reg_list) == 6)
#
#     pers = pers_repo.find('3')
#     ev = ev_repo.find('2')
#     reg = Registration(pers, ev)
#     test_repo.store(reg)
#     crt_reg_list = test_repo.get_all_registrations()
#     assert (len(crt_reg_list) == 7)
#
#     assert (test_repo.get_all_registrations()[-1].getPerson().getName() == 'Cleopatra Candy')
#     assert (test_repo.get_all_registrations()[-1].getPerson().getAddress() == 'Third Street')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getDate() == '02.02.2022')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getTime() == '02:02')
#     assert (test_repo.get_all_registrations()[-1].getEvent().getDesc() == 'Drinking Night')
#
#     test_repo.delete('3', '2')
#
#
# test_find()
# test_store()
# test_size()
# test_get_all_registrations()
