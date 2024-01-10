from domain.entities import Person


class PersonRepo:
    def __init__(self):
        self.__people = []

    def r_find(self, p_list, id):
        if p_list[0].getID() == id:
            return p_list[0]
        return self.r_find(p_list[1:], id)

    def find(self, id):
        """
        Cauta persoana cu id-ul dat
        :param id: id dat
        :type id: str
        :return: persoana cu id dat, None daca nu exista
        :rtype: Person
        """
        # for pers in self.__people:
        #     if pers.getID() == id:
        #         return pers
        # return None
        return self.r_find(self.__people, id)

    def r_find_index(self, p_list, id, index):
        if p_list[0].getID() == id:
            return index
        return self.r_find_index(p_list[1:], id, index + 1)

    def find_index(self, id):
        """
        Gaseste index-ul (pozitia) la care este persoana cu id dat
        :param id: id dat
        :type id: str
        :return: pozitia in lista a persoanei cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        # index = -1
        # for i in range(self.size()):
        #     if self.__people[i].getID() == id:
        #         index = i
        # return index
        return self.r_find_index(self.__people, id, 0)

    def store(self, person):
        """
        Adauga o persoana in lista
        :param person: persoana care se adauga
        :type person: Person
        :return: -; lista de persoane se modifica prin adaugarea persoanei date
        :rtype:
        :raises: ValueError daca persoana exista deja
        """
        if self.find(person.getID()) is not None:
            raise ValueError('Exista deja persoana cu acest id.')
        self.__people.append(person)

    def size(self):
        """
        Returneaza numarul de persoane din repo
        :rtype: int
        """
        return len(self.__people)

    def get_all_people(self):
        """
        Returneaza olista cu toate persoanele existente
        :rtype: lista de obiecte de tip Person
        """
        return self.__people

    def delete_by_id(self, id):
        """
        Sterge persoana dupa id
        :param id: id-ul dat
        :type id: str
        :return: persoana stearsa
        :rtype: Person
        :raises: ValueError daca id-ul nu exista
        """
        person = self.find(id)
        if person is None:
            raise ValueError('Nu exista persoana cu acest id.')
        self.__people.remove(person)
        return person

    def update(self, id, modified_pers):
        """
        Modifica datele persoanei cu id-ul dat
        :param id: id-ul dat
        :type id: str
        :param modified_pers: persoana cu datele noi
        :type modified_pers: Person
        :return: persoana modificata
        :rtype: Person
        """
        person = self.find(id)
        if person is None:
            raise ValueError('Nu exista persoana cu acest id.')
        old_pers = self.find(id)
        self.__people[self.find_index(id)] = modified_pers
        return modified_pers

    def delete_all(self):
        self.__people = []


# def setup_test_repo1():
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     pers2 = Person('2', 'Blake Brews', 'Second Street')
#     pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
#     pers4 = Person('4', 'Dante D\'Alembert', 'Fourth Street')
#     pers5 = Person('5', 'Eugene Erickson', 'Fifth Street')
#
#     test_repo = PersonRepo()
#
#     test_repo.store(pers1)
#     test_repo.store(pers2)
#     test_repo.store(pers3)
#     test_repo.store(pers4)
#     test_repo.store(pers5)
#
#     return test_repo


# def test_find():
#     test_repo = setup_test_repo1()
#
#     p1 = test_repo.find('3')
#     assert (p1.getName() == 'Cleopatra Candy')
#     assert (p1.getAddress() == 'Third Street')
#
#     p2 = test_repo.find('6')
#     assert (p2 is None)
#
#
# def test_find_index():
#     test_repo = setup_test_repo1()
#
#     p1 = test_repo.find_index('3')
#     assert (p1 == 2)
#
#     p2 = test_repo.find_index('6')
#     assert (p2 == -1)
#
#
# def test_store():
#     test_repo = PersonRepo()
#
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     test_repo.store(pers1)
#     assert (test_repo.size() == 1)
#
#     pers2 = Person('2', 'Blake Brews', 'Second Street')
#     test_repo.store(pers2)
#     assert (test_repo.size() == 2)
#
#     try:
#         # duplicate person
#         test_repo.store(pers2)
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_size():
#     test_repo = setup_test_repo1()
#
#     assert (test_repo.size() == 5)
#
#     pers1 = Person('6', 'Florence Fury', 'Sixth Street')
#     pers2 = Person('7', 'Gabrielle Grace', 'Seventh Street')
#     test_repo.store(pers1)
#     test_repo.store(pers2)
#
#     assert (test_repo.size() == 7)
#
#
# def test_get_all_people():
#     test_repo = setup_test_repo1()
#
#     crt_pers_list = test_repo.get_all_people()
#     assert (type(crt_pers_list) == list)
#     assert (len(crt_pers_list) == 5)
#
#     pers = Person('6', 'Florence Fury', 'Sixth Street')
#     test_repo.store(pers)
#     assert (len(crt_pers_list) == 6)
#
#     assert (test_repo.get_all_people()[-1].getName() == 'Florence Fury')
#     assert (test_repo.get_all_people()[-1].getAddress() == 'Sixth Street')
#
#
# def test_delete():
#     test_repo = PersonRepo()
#
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     test_repo.store(pers1)
#     pers2 = Person('2', 'Blake Brews', 'Second Street')
#     test_repo.store(pers2)
#
#     deleted_person = test_repo.delete_by_id('1')
#     assert (deleted_person.getName() == 'Arizona Andrews')
#     assert (deleted_person.getAddress() == 'First Street')
#
#     assert (test_repo.size() == 1)
#
#     person_left = test_repo.find('2')
#     assert (person_left.getName() == 'Blake Brews')
#     assert (person_left.getAddress() == 'Second Street')
#
#     try:
#         test_repo.delete_by_id('3')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_update():
#     test_repo = PersonRepo()
#
#     pers1 = Person('1', 'Arizona Andrews', 'First Street')
#     test_repo.store(pers1)
#     pers2 = Person('2', 'Blake Brews', 'Second Street')
#     test_repo.store(pers2)
#     pers3 = Person('6', 'Florence Fury', 'Sixth Street')
#     test_repo.store(pers3)
#
#     modified_pers = test_repo.update('2', pers3)
#     assert (modified_pers.getName() == 'Florence Fury')
#     assert (modified_pers.getAddress() == 'Sixth Street')
#
#     try:
#         test_repo.update('5', pers3)
#         assert False
#     except ValueError:
#         assert True
#
#
# test_find()
# test_find_index()
# test_store()
# test_size()
# test_get_all_people()
# test_delete()
# test_update()


class FilePersonRepo:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de persoane din fisier
        :rtype: lista de obiecte de tip Person
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        people = []
        for line in lines:
            person_id, person_name, person_address = [token.strip() for token in line.split('; ')]
            p = Person(person_id, person_name, person_address)
            people.append(p)

        f.close()
        return people

    def save_to_file(self, people):
        """
        Salveaza persoanele in fisier
        :param people: lista cu persoane
        """
        with open(self.__filename, 'w') as f:
            for person in people:
                person_str = str(person.getID()) + '; ' + str(person.getName()) + '; ' + str(person.getAddress()) + \
                             '\n'
                f.write(person_str)

    def size(self):
        """
        Returneaza numarul de persoane din multime
        :return: numar persoane existente
        :rtype: int
        """
        return len(self.load_from_file())

    def find(self, id):
        """
        Cauta persoana cu id-ul dat
        :param id: id dat
        :type id: str
        :return: persoana cu id dat, None daca nu exista
        :rtype: Person
        """
        people = self.load_from_file()
        for pers in people:
            if pers.getID() == id:
                return pers
        return None

    def find_index(self, id):
        """
        Gaseste index-ul (pozitia) la care este persoana cu id dat
        :param id: id dat
        :type id: str
        :return: pozitia in lista a persoanei cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        people = self.load_from_file()
        index = -1
        for i in range(self.size()):
            if people[i].getID() == id:
                index = i
        return index

    def store(self, person):
        """
        Adauga o persoana in lista
        :param person: persoana care se adauga
        :type person: Person
        :return: -; lista de persoane se modifica prin adaugarea persoanei date
        :rtype:
        :raises: ValueError daca persoana exista deja
        """
        people = self.load_from_file()
        if self.find(person.getID()) is not None:
            raise ValueError('Exista deja persoana cu acest id.')
        people.append(person)
        self.save_to_file(people)

    def get_all_people(self):
        """
        Returneaza olista cu toate persoanele existente
        :rtype: lista de obiecte de tip Person
        """
        return self.load_from_file()

    def delete_by_id(self, id):
        """
        Sterge persoana dupa id
        :param id: id-ul dat
        :type id: str
        :return: persoana stearsa
        :rtype: Person
        :raises: ValueError daca id-ul nu exista
        """
        people = self.load_from_file()
        index = self.find_index(id)
        person = self.find(id)
        if person is None:
            raise ValueError('Nu exista persoana cu acest id.')
        deleted_pers = people.pop(index)
        self.save_to_file(people)
        return deleted_pers

    def update(self, id, modified_pers):
        """
        Modifica datele persoanei cu id-ul dat
        :param id: id-ul dat
        :type id: str
        :param modified_pers: persoana cu datele noi
        :type modified_pers: Person
        :return: persoana modificata
        :rtype: Person
        """
        people = self.load_from_file()
        index = self.find_index(id)
        person = self.find(id)
        if person is None:
            raise ValueError('Nu exista persoana cu acest id.')
        people[index] = modified_pers
        self.save_to_file(people)
        return modified_pers

    def delete_all(self):
        self.save_to_file([])


def test_find():
    test_repo = FilePersonRepo('data/test_people.txt')

    p1 = test_repo.find('3')
    assert (p1.getName() == 'Cleopatra Candy')
    assert (p1.getAddress() == 'Third Street')

    p2 = test_repo.find('10')
    assert (p2 is None)


def test_find_index():
    test_repo = FilePersonRepo('data/test_people.txt')

    p1 = test_repo.find_index('3')
    assert (p1 == 2)

    p2 = test_repo.find_index('10')
    assert (p2 == -1)


def test_store():
    test_repo = FilePersonRepo('data/test_people.txt')

    pers1 = Person('6', 'Frida Flower', 'Sixth Street')
    test_repo.store(pers1)
    assert (test_repo.size() == 6)

    try:
        test_repo.store(pers1)
        assert False
    except ValueError:
        assert True

    test_repo.delete_by_id('6')


def test_size():
    test_repo = FilePersonRepo('data/test_people.txt')

    assert (test_repo.size() == 5)

    pers1 = Person('6', 'Florence Fury', 'Sixth Street')
    pers2 = Person('7', 'Gabrielle Grace', 'Seventh Street')
    test_repo.store(pers1)
    test_repo.store(pers2)

    assert (test_repo.size() == 7)

    test_repo.delete_by_id('6')
    test_repo.delete_by_id('7')


def test_get_all_people():
    test_repo = FilePersonRepo('data/test_people.txt')

    crt_pers_list = test_repo.get_all_people()
    assert (type(crt_pers_list) == list)
    assert (len(crt_pers_list) == 5)

    pers = Person('6', 'Florence Fury', 'Sixth Street')
    test_repo.store(pers)

    crt_pers_list = test_repo.get_all_people()
    assert (len(crt_pers_list) == 6)

    assert (test_repo.get_all_people()[-1].getName() == 'Florence Fury')
    assert (test_repo.get_all_people()[-1].getAddress() == 'Sixth Street')


def test_delete():
    test_repo = FilePersonRepo('data/test_people.txt')

    deleted_person = test_repo.delete_by_id('6')
    assert (deleted_person.getName() == 'Florence Fury')
    assert (deleted_person.getAddress() == 'Sixth Street')

    assert (test_repo.size() == 5)

    person_left = test_repo.find('2')
    assert (person_left.getName() == 'Blake Brews')
    assert (person_left.getAddress() == 'Second Street')

    try:
        test_repo.delete_by_id('10')
        assert False
    except ValueError:
        assert True


def test_update():
    test_repo = FilePersonRepo('data/test_people.txt')

    pers3 = Person('6', 'Florence Fury', 'Sixth Street')

    modified_pers = test_repo.update('2', pers3)
    assert (modified_pers.getName() == 'Florence Fury')
    assert (modified_pers.getAddress() == 'Sixth Street')

    pers = Person('2', 'Blake Brews', 'Second Street')
    test_repo.update('6', pers)

    try:
        test_repo.update('10', pers3)
        assert False
    except ValueError:
        assert True


test_find()
test_find_index()
test_store()
test_size()
test_get_all_people()
test_delete()
test_update()
