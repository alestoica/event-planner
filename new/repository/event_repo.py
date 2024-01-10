from domain.entities import Event


class EventRepo:
    def __init__(self):
        self.__events = []

    def find(self, id):
        """
        Cauta evenimentul cu id-ul dat
        :param id: id dat
        :type id: str
        :return: evenimentul cu id dat, None daca nu exista
        :rtype: Event
        """
        for ev in self.__events:
            if ev.getID() == id:
                return ev
        return None

    def find_index(self, id):
        """
        Gaseste index-ul (pozitia) la care este evenimentul cu id dat
        :param id: id dat
        :type id: str
        :return: pozitia in lista a evenimentului cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        index = -1
        for i in range(self.size()):
            if self.__events[i].getID() == id:
                index = i
        return index

    def store(self, event):
        """
        Adauga un eveniment in lista
        :param event: evenimentul care se adauga
        :type event: Event
        :return: -; lista de evenimente se modifica prin adaugarea evenimentului dat
        :rtype:
        :raises: ValueError daca evenimentul exista deja
        """
        # verificare id duplicat
        if self.find(event.getID()) is not None:
            raise ValueError('Exista deja evenimentul cu acest id.')
        self.__events.append(event)

    def size(self):
        """
        Returneaza numarul de evenimente din repo
        :rtype: int
        """
        return len(self.__events)

    def get_all_events(self):
        """
        Returneaza olista cu toate persoanele existente
        :rtype: lista de obiecte de tip Person
        """
        return self.__events

    def delete_by_id(self, id):
        """
        Sterge evenimentul dupa id
        :param id: id-ul dat
        :type id: str
        :return: evenimentul sters
        :rtype: Event
        :raises: ValueError daca id-ul nu exista
        """
        event = self.find(id)
        if event is None:
            raise ValueError('Nu exista evenimentul cu acest id.')
        self.__events.remove(event)
        return event

    def delete_all(self):
        """
        Sterge toate evenimentele din lista
        """
        self.__events = []

    def update(self, id, modified_ev):
        """
        Modifica datele evenimentului cu id-ul dat
        :param id: id-ul dat
        :type id: str
        :param modified_ev: evenimentul cu datele noi
        :type modified_ev: Event
        :return: evenimentul modificata
        :rtype: Event
        """
        person = self.find(id)
        if person is None:
            raise ValueError('Nu exista evenimentul cu acest id.')
        old_pers = self.find(id)
        self.__events[self.find_index(id)] = modified_ev
        return modified_ev


# def setup_test_repo2():
#     ev1 = Event('1', '01.01.2022', '01:01', 'Movie Night')
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     ev3 = Event('3', '03.03.2022', '03:03', 'Dancing Night')
#     ev4 = Event('4', '04.04.2022', '04:04', 'Rock Night')
#     ev5 = Event('5', '05.05.2022', '05:05', 'Salsa Night')
#     test_repo = EventRepo()
#
#     test_repo.store(ev1)
#     test_repo.store(ev2)
#     test_repo.store(ev3)
#     test_repo.store(ev4)
#     test_repo.store(ev5)
#
#     return test_repo
#
#
# def test_find():
#     test_repo = setup_test_repo2()
#
#     e1 = test_repo.find('3')
#     assert (e1.getDate() == '03.03.2022')
#     assert (e1.getTime() == '03:03')
#     assert (e1.getDesc() == 'Dancing Night')
#
#     e2 = test_repo.find('6')
#     assert (e2 is None)
#
#
# def test_find_index():
#     test_repo = setup_test_repo2()
#
#     e1 = test_repo.find_index('4')
#     assert (e1 == 3)
#
#     e2 = test_repo.find_index('6')
#     assert (e2 == -1)
#
#
# def test_store():
#     test_repo = EventRepo()
#
#     ev1 = Event('1', '01.01.2022', '01:01', 'Movie Night')
#     test_repo.store(ev1)
#     assert (test_repo.size() == 1)
#
#     ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
#     test_repo.store(ev2)
#     assert (test_repo.size() == 2)
#
#     try:
#         # duplicate person
#         test_repo.store(ev2)
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_size():
#     test_repo = setup_test_repo2()
#
#     assert (test_repo.size() == 5)
#
#     ev1 = Event('6', '06.06.2022', '06:06', 'Games Night')
#     ev2 = Event('7', '07.07.2022', '07:07', 'Karaoke Night')
#     test_repo.store(ev1)
#     test_repo.store(ev2)
#
#     assert (test_repo.size() == 7)
#
#
# def test_get_all_events():
#     test_repo = setup_test_repo2()
#
#     crt_ev_list = test_repo.get_all_events()
#     assert (type(crt_ev_list) == list)
#     assert (len(crt_ev_list) == 5)
#
#     ev = Event('6', '06.06.2022', '06:06', 'Games Night')
#     test_repo.store(ev)
#     assert (len(crt_ev_list) == 6)
#
#     assert (test_repo.get_all_events()[-1].getDate() == '06.06.2022')
#     assert (test_repo.get_all_events()[-1].getTime() == '06:06')
#     assert (test_repo.get_all_events()[-1].getDesc() == 'Games Night')
#
#
# def test_delete():
#     test_repo = EventRepo()
#
#     ev1 = Event('6', '06.06.2022', '06:06', 'Games Night')
#     test_repo.store(ev1)
#     ev2 = Event('7', '07.07.2022', '07:07', 'Karaoke Night')
#     test_repo.store(ev2)
#
#     deleted_event = test_repo.delete_by_id('6')
#     assert (deleted_event.getDate() == '06.06.2022')
#     assert (deleted_event.getTime() == '06:06')
#     assert (deleted_event.getDesc() == 'Games Night')
#
#     assert (test_repo.size() == 1)
#
#     event_left = test_repo.find('7')
#     assert (event_left.getDate() == '07.07.2022')
#     assert (event_left.getTime() == '07:07')
#     assert (event_left.getDesc() == 'Karaoke Night')
#
#     try:
#         test_repo.delete_by_id('3')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_update():
#     test_repo = EventRepo()
#
#     ev1 = Event('6', '06.06.2022', '06:06', 'Games Night')
#     test_repo.store(ev1)
#     ev2 = Event('7', '07.07.2022', '07:07', 'Karaoke Night')
#     test_repo.store(ev2)
#     ev3 = Event('1', '01.01.2022', '01:01', 'Movie Night')
#     test_repo.store(ev3)
#
#     modified_ev = test_repo.update('7', ev3)
#     assert (modified_ev.getDate() == '01.01.2022')
#     assert (modified_ev.getTime() == '01:01')
#     assert (modified_ev.getDesc() == 'Movie Night')
#
#     try:
#         test_repo.update('5', ev3)
#         assert False
#     except ValueError:
#         assert True
#
#
# test_find()
# test_find_index()
# test_store()
# test_size()
# test_get_all_events()
# test_delete()
# test_update()


class FileEventRepo:
    def __init__(self, filename):
        self.__filename = filename

    def load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de evenimente din fisier
        :rtype: lista de obiecte de tip Event
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        events = []
        for line in lines:
            event_id, event_date, event_time, event_desc = [token.strip() for token in line.split('; ')]
            e = Event(event_id, event_date, event_time, event_desc)
            events.append(e)
        f.close()
        return events

    def save_to_file(self, events):
        """
        Salveaza evenimentele in fisier
        :param events: lista cu evenimente
        """
        with open(self.__filename, 'w') as f:
            for event in events:
                event_str = str(event.getID()) + '; ' + str(event.getDate()) + '; ' + str(event.getTime()) + '; ' + \
                            str(event.getDesc()) + '\n'
                f.write(event_str)

    def size(self):
        """
        Returneaza numarul de evenimente din multime
        :return: numar evenimente existente
        :rtype: int
        """
        return len(self.load_from_file())

    def find(self, id):
        """
        Cauta evenimentul cu id-ul dat
        :param id: id dat
        :type id: str
        :return: evenimentul cu id dat, None daca nu exista
        :rtype: Event
        """
        events = self.load_from_file()
        for ev in events:
            if ev.getID() == id:
                return ev
        return None

    def find_index(self, id):
        """
        Gaseste index-ul (pozitia) la care este evenimentul cu id dat
        :param id: id dat
        :type id: str
        :return: pozitia in lista a evenimentului cu id dat, -1 daca nu exista
        :rtype: int (>= 0, < repo.size())
        """
        events = self.load_from_file()
        index = -1
        for i in range(self.size()):
            if events[i].getID() == id:
                index = i
        return index

    def store(self, event):
        """
        Adauga un eveniment in lista
        :param event: evenimentul care se adauga
        :type event: Event
        :return: -; lista de evenimente se modifica prin adaugarea evenimentului dat
        :rtype:
        :raises: ValueError daca evenimentul exista deja
        """
        events = self.load_from_file()
        if self.find(event.getID()) is not None:
            raise ValueError('Exista deja evenimentul cu acest id.')
        events.append(event)
        self.save_to_file(events)

    def get_all_events(self):
        """
        Returneaza olista cu toate persoanele existente
        :rtype: lista de obiecte de tip Person
        """
        return self.load_from_file()

    def delete_by_id(self, id):
        """
        Sterge evenimentul dupa id
        :param id: id-ul dat
        :type id: str
        :return: evenimentul sters
        :rtype: Event
        :raises: ValueError daca id-ul nu exista
        """
        events = self.load_from_file()
        index = self.find_index(id)
        event = self.find(id)
        if event is None:
            raise ValueError('Nu exista evenimentul cu acest id.')
        deleted_ev = events.pop(index)
        self.save_to_file(events)
        return deleted_ev

    def update(self, id, modified_ev):
        """
        Modifica datele evenimentului cu id-ul dat
        :param id: id-ul dat
        :type id: str
        :param modified_ev: evenimentul cu datele noi
        :type modified_ev: Event
        :return: evenimentul modificata
        :rtype: Event
        """
        events = self.load_from_file()
        index = self.find_index(id)
        event = self.find(id)
        if event is None:
            raise ValueError('Nu exista evenimentul cu acest id.')
        events[index] = modified_ev
        self.save_to_file(events)
        return modified_ev

    def delete_all(self):
        self.save_to_file([])


# def test_find():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     e1 = test_repo.find('3')
#     assert (e1.getDate() == '03.03.2022')
#     assert (e1.getTime() == '03:03')
#     assert (e1.getDesc() == 'Dancing Night')
#
#     e2 = test_repo.find('10')
#     assert (e2 is None)
#
#
# def test_find_index():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     e1 = test_repo.find_index('4')
#     assert (e1 == 3)
#
#     e2 = test_repo.find_index('10')
#     assert (e2 == -1)
#
#
# def test_store():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     ev1 = Event('5', '05.05.2022', '05:05', 'Salsa Night')
#     test_repo.store(ev1)
#     assert (test_repo.size() == 5)
#
#     ev2 = Event('6', '06.06.2022', '06:06', 'Games Night')
#     test_repo.store(ev2)
#     assert (test_repo.size() == 6)
#
#     try:
#         test_repo.store(ev2)
#         assert False
#     except ValueError:
#         test_repo.delete_by_id('5')
#         test_repo.delete_by_id('6')
#         assert True
#
#
# def test_size():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     assert (test_repo.size() == 4)
#
#     ev1 = Event('8', '08.08.2022', '08:08', 'Girls Night')
#     ev2 = Event('9', '09.09.2022', '09:09', 'Christmas Night')
#     test_repo.store(ev1)
#     test_repo.store(ev2)
#
#     assert (test_repo.size() == 6)
#
#     test_repo.delete_by_id('8')
#     test_repo.delete_by_id('9')
#
#
# def test_get_all_events():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     crt_ev_list = test_repo.get_all_events()
#     assert (type(crt_ev_list) == list)
#     assert (len(crt_ev_list) == 4)
#
#     ev = Event('10', '10.10.2022', '10:10', 'The Voice Night')
#     test_repo.store(ev)
#     assert (test_repo.size() == 5)
#
#     assert (test_repo.get_all_events()[-1].getDate() == '10.10.2022')
#     assert (test_repo.get_all_events()[-1].getTime() == '10:10')
#     assert (test_repo.get_all_events()[-1].getDesc() == 'The Voice Night')
#
#
# def test_delete():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     deleted_event = test_repo.delete_by_id('10')
#     assert (deleted_event.getDate() == '10.10.2022')
#     assert (deleted_event.getTime() == '10:10')
#     assert (deleted_event.getDesc() == 'The Voice Night')
#
#     assert (test_repo.size() == 4)
#
#     event_left = test_repo.find('4')
#     assert (event_left.getDate() == '04.04.2022')
#     assert (event_left.getTime() == '04:04')
#     assert (event_left.getDesc() == 'Rock Night')
#
#     test_repo.delete_by_id('4')
#     ev = Event('4', '04.04.2022', '04:04', 'Rock Night')
#     test_repo.store(ev)
#
#     try:
#         test_repo.delete_by_id('10')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_update():
#     test_repo = FileEventRepo('data/test_events.txt')
#
#     ev3 = Event('11', '11.11.2022', '11:11', 'Halloween Night')
#
#     modified_ev = test_repo.update('4', ev3)
#     assert (modified_ev.getDate() == '11.11.2022')
#     assert (modified_ev.getTime() == '11:11')
#     assert (modified_ev.getDesc() == 'Halloween Night')
#
#     ev = Event('4', '04.04.2022', '04:04', 'Rock Night')
#     test_repo.update('11', ev)
#
#     try:
#         test_repo.update('12', ev3)
#         assert False
#     except ValueError:
#         assert True
#
#
# test_find()
# test_find_index()
# test_store()
# test_size()
# test_get_all_events()
# test_delete()
# test_update()
