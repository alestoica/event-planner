from domain.entities import Registration
from repository.registration_repo import FileRegistrationRepo
from repository.person_repo import FilePersonRepo
from repository.event_repo import FileEventRepo
from sortari.shell_sort import shellSort
from sortari.bubble_sort import bubbleSort
from sortari.shell_sort import cmp_el


class RegistrationService:
    def __init__(self, reg_repo, person_repo, event_repo):
        """
        Initializeaza service
        :param reg_repo: obiect de tip repo care ne ajuta sa gestionam multimea de inscrieri
        :type reg_repo: FileRegistrationRepo
        :param person_repo: obiect de tip repo care ne ajuta sa gestionam multimea de persoane
        :type person_repo: FilePersonRepo
        :param event_repo: obiect de tip repo care ne ajuta sa gestionam multimea de evenimente
        :type event_repo: FileEventRepo
        """
        self.__reg_repo = reg_repo
        self.__person_repo = person_repo
        self.__event_repo = event_repo

    def create_registration(self, idp, ide):
        """
        Creeaza o inscriere
        :param idp: id-ul persoanei
        :type idp: str
        :param ide: id-ul evenimentului
        :type ide: str
        :return: inscrierea creata cu datele date
        :rtype: Registration
        :raises: ValueError daca persoana are date invalide, daca id-ul exista deja in lista
        """
        person = self.__person_repo.find(idp)
        if person is None:
            raise ValueError('Persoana cautata nu exista.')

        event = self.__event_repo.find(ide)
        if event is None:
            raise ValueError('Evenimentul cautat nu exista.')

        registration = Registration(person, event)
        self.__reg_repo.store(registration)
        return registration

    def delete_registration(self, idp, ide):
        """
        Sterge o inscriere
        :param idp: id-ul persoanei
        :type idp: str
        :param ide: id-ul evenimentului
        :type ide: str
        :return: inscrierea stearsa cu datele date
        :rtype: Registration
        :raises: ValueError daca persoana are date invalide, daca id-ul exista deja in lista
        """
        person = self.__person_repo.find(idp)
        if person is None:
            raise ValueError('Persoana cautata nu exista.')

        event = self.__event_repo.find(ide)
        if event is None:
            raise ValueError('Evenimentul cautat nu exista.')

        registration = Registration(person, event)
        self.__reg_repo.delete(idp, ide)
        return registration

    def get_all_registrations(self):
        """
        Returneaza o lista cu toate inscrierile existente
        :return: lista de inscrieri existente
        :rtype: lista de obiecte de tip Registration
        """
        return self.__reg_repo.get_all_registrations()

    def get_all_registrations_for_one_person(self, idp):
        """
        Returneaza toate evenimentele la care s-a inscris o persoana
        :param idp: id-ul persoanei
        :type idp: str
        :return: lista cu evenimentele la care este inscrisa persoana
        :rtype: lista de obiecte de tip Event
        """
        reg_list = self.get_all_registrations()
        return [reg.getEvent() for reg in reg_list if reg.getPerson().getID() == idp]

    def get_no_events_for_each_person(self):
        """
        Returneaza numarul de evenimente la care este inscrisa fiecare persoana
        :return: max_value
        """
        pers_list = self.__person_repo.get_all_people()
        no_events = {}
        for p in pers_list:
            no_events[p.getID()] = len(self.get_all_registrations_for_one_person(p.getID()))
        return no_events

    def get_no_people_for_each_event(self):
        """

        :return: dictionar cu keys = id_pers si values = numar de evenimente ale persoanei
        """
        ev_list = self.__event_repo.get_all_events()
        no_people = {}
        for e in ev_list:
            no_people[e.getID()] = len(self.get_all_registrations_for_one_event(e.getID()))
        no_people = {k: v for k, v in sorted(no_people.items(), key=lambda item: item[1], reverse=True)}
        return no_people

    def get_all_registrations_for_one_event(self, ide):
        """
        Returneaza toate persoanele care sunt inscrise la un eveniment
        :param ide: id-ul evenimentului
        :type ide: str
        :return: lista cu persoanele care sunt inscrise la un eveniment
        :rtype: lista de obiecte de tip Person
        """
        reg_list = self.get_all_registrations()
        return [reg.getPerson() for reg in reg_list if reg.getEvent().getID() == ide]

    def sort_registrations_for_one_pers(self, idp):
        """
        Returneaza lista de evenimente la care s-a inscris o persoana, sortata dupa descriere si data
        :param idp: id-ul persoanei
        :type idp: str
        :return: lista de obiecte de tip Event
        """
        ev_list = self.get_all_registrations_for_one_person(idp)
        # ev_list = sorted(ev_list, key=lambda event: (event.getDesc(), event.date()))
        # ev_list = bubbleSort(ev_list, key=lambda event: (event.getDesc(), event.date()), reverse=True, cmp=cmp_el)
        ev_list = shellSort(ev_list, key=lambda event: (event.getDesc(), event.date()), cmp=cmp_el)
        return ev_list


# def test_create_registration():
#     person_repo = FilePersonRepo('data/people.txt')
#     event_repo = FileEventRepo('data/events.txt')
#     reg_repo = FileRegistrationRepo('data/test_registrations_srv.txt')
#
#     test_service = RegistrationService(reg_repo, person_repo, event_repo)
#
#     created_reg = test_service.create_registration('1', '4')
#
#     assert (created_reg.getPerson() == person_repo.find('1'))
#     assert (created_reg.getEvent() == event_repo.find('4'))
#
#     try:
#         test_service.create_registration('1', '4')
#         assert False
#     except ValueError:
#         assert True
#
#     test_service.delete_registration('1', '4')
#
#
# def test_get_all_registration():
#     person_repo = FilePersonRepo('data/people.txt')
#     event_repo = FileEventRepo('data/events.txt')
#     reg_repo = FileRegistrationRepo('data/test_registrations_srv.txt')
#
#     test_service = RegistrationService(reg_repo, person_repo, event_repo)
#
#     assert (type(test_service.get_all_registrations()) == list)
#     assert (len(test_service.get_all_registrations()) == 6)
#
#
# def test_get_all_registrations_for_one_person():
#     person_repo = FilePersonRepo('data/people.txt')
#     event_repo = FileEventRepo('data/events.txt')
#     reg_repo = FileRegistrationRepo('data/test_registrations_srv.txt')
#
#     test_service = RegistrationService(reg_repo, person_repo, event_repo)
#
#     assert (test_service.get_all_registrations_for_one_person('5') == [])
#
#
# def test_get_all_registrations_for_one_event():
#     person_repo = FilePersonRepo('data/people.txt')
#     event_repo = FileEventRepo('data/events.txt')
#     reg_repo = FileRegistrationRepo('data/test_registrations_srv.txt')
#
#     test_service = RegistrationService(reg_repo, person_repo, event_repo)
#
#     assert (test_service.get_all_registrations_for_one_event('7') == [])
#
#
# test_create_registration()
# test_get_all_registration()
