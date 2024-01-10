from domain.entities import Event
from domain.validators import EventValidator
from repository.event_repo import FileEventRepo


class EventService:
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de evenimente
        :type repo: FileEventRepo
        :param validator: validator pentru verificarea evenimentelor
        :type validator: EventValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_event(self, id, date, time, desc):
        """
        Adaug persoana
        :param id: id-ul persoanei
        :type id: str
        :param date: data evenimentului
        :type date: str
        :param time: ora la care incepe evenimentul
        :type time: str
        :param desc: descrierea evenimentului
        :type desc: str
        :return: obiectul de tip Event
        :rtype: -; Evenimentul s-a adaugat in lista
        :raises: ValueError daca evenimentul are date invalide, daca id-ul exista deja in lista
        """
        e = Event(id, date, time, desc)
        self.__validator.validate(e)
        self.__repo.store(e)
        return e

    def get_all_events(self):
        """
        Returneaza o lista cu toate evenimentele disponibile
        :return: lista de evenimente disponibile
        :rtype: lista de obiecte de tip Event
        """
        return self.__repo.get_all_events()

    def delete_event(self, id):
        """
        Sterge din lista evenimentul cu id dat
        :param id: id-ul dat
        :type id: str
        :return: evenimentul sters
        :rtype: Event
        :raises: ValueError daca nu exista evenimentul cu id-ul dat
        """
        return self.__repo.delete_by_id(id)

    def update_event(self, id, date, time, desc):
        """
        Modifica datele evenimentului cu id-ul dat
        :param id: id-ul evenimentului care trebuie modificat
        :type id: str
        :param date: noua data a evenimentului
        :type date: str
        :param time: noua ora la care incepe evenimentul
        :type time: str
        :param desc: noua descriere a evenimentului
        :type desc: str
        :return: evenimentul modificat
        :rtype: Event
        :raises: ValueError daca noile date nu sunt valide, sau nu exista evenimentul cu id dat
        """
        e = Event(id, date, time, desc)
        self.__validator.validate(e)
        return self.__repo.update(id, e)

    def find_event(self, id):
        """
        Cauta evenimentul cu id-ul dat
        :param id: id-ul evenimentului cautat
        :type id: str
        :return: evenimentul cautat
        :rtype: Event
        """
        if self.__repo.find(id) is None:
            raise ValueError('Evenimentul cautat nu exista.')
        else:
            return self.__repo.find(id)


# def test_add_event():
#     repo = FileEventRepo("data/test_events_srv.txt")
#     validator = EventValidator()
#     test_service = EventService(repo, validator)
#
#     added_event = test_service.add_event('8', '08.08.2022', '08:08', 'Christmas Night')
#     assert (added_event.getDate() == '08.08.2022')
#     assert (added_event.getTime() == '08:08')
#     assert (added_event.getDesc() == 'Christmas Night')
#
#     assert (len(test_service.get_all_events()) == 8)
#
#     try:
#         test_service.add_event('-1', '01.01.2022', '01:01', 'Movie Night')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_get_all_events():
#     repo = FileEventRepo("data/test_events_srv.txt")
#     validator = EventValidator()
#     test_service = EventService(repo, validator)
#
#     assert (type(test_service.get_all_events()) == list)
#     assert (len(test_service.get_all_events()) == 8)
#
#
# def test_delete_event():
#     repo = FileEventRepo("data/test_events_srv.txt")
#     validator = EventValidator()
#     test_service = EventService(repo, validator)
#
#     deleted_event = test_service.delete_event('8')
#
#     assert (len(test_service.get_all_events()) == 7)
#     assert (deleted_event.getDate() == '08.08.2022')
#     assert (deleted_event.getTime() == '08:08')
#     assert (deleted_event.getDesc() == 'Christmas Night')
#
#     try:
#         test_service.delete_event('10')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_update_event():
#     repo = FileEventRepo("data/test_events_srv.txt")
#     validator = EventValidator()
#     test_service = EventService(repo, validator)
#
#     updated_event = test_service.update_event('1', '08.08.2022', '08:08', 'Christmas Night')
#
#     assert (updated_event.getDate() == '08.08.2022')
#     assert (updated_event.getTime() == '08:08')
#     assert (updated_event.getDesc() == 'Christmas Night')
#
#     test_service.update_event('1', '01.01.2022', '01:01', 'Movie Night')
#
#     try:
#         test_service.update_event('5', 'NU', 'EXISTA', 'ID')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_find_event():
#     repo = FileEventRepo("data/test_events_srv.txt")
#     validator = EventValidator()
#     test_service = EventService(repo, validator)
#
#     searched_event = test_service.find_event('1')
#
#     assert (searched_event.getDate() == '01.01.2022')
#     assert (searched_event.getTime() == '01:01')
#     assert (searched_event.getDesc() == 'Movie Night')
#
#     try:
#         test_service.find_event('10')
#         assert False
#     except ValueError:
#         assert True
#
#
# test_add_event()
# test_get_all_events()
# test_delete_event()
# test_update_event()
# test_find_event()
