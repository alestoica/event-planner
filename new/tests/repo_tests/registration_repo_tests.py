import unittest

from domain.entities import Registration, Person, Event
from repository.registration_repo import RegistrationRepo, FileRegistrationRepo, FileEventRepo, FilePersonRepo
from repository.person_repo import PersonRepo
from repository.event_repo import EventRepo


class TestCaseRegistrationRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = RegistrationRepo()
        self.__pers_repo = PersonRepo()
        self.__ev_repo = EventRepo()
        self.__add_predefined_registrations()

    def __add_predefined_registrations(self):
        pers1 = Person('1', 'Arizona Andrews', 'First Street')
        pers2 = Person('2', 'Blake Brews', 'Second Street')
        pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
        pers4 = Person('4', 'Dante DAlembert', 'Fourth Street')
        pers5 = Person('5', 'Eugene Erickson', 'Fifth Street')

        self.__pers_repo.store(pers1)
        self.__pers_repo.store(pers2)
        self.__pers_repo.store(pers3)
        self.__pers_repo.store(pers4)
        self.__pers_repo.store(pers5)

        ev1 = Event('1', '01.01.2022', '01:01', 'Date Night')
        ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
        ev3 = Event('3', '03.03.2022', '03:03', 'Dancing Night')
        ev4 = Event('4', '04.04.2022', '04:04', 'Rock Night')

        self.__ev_repo.store(ev1)
        self.__ev_repo.store(ev2)
        self.__ev_repo.store(ev3)
        self.__ev_repo.store(ev4)

        reg1 = Registration(pers1, ev1)
        reg2 = Registration(pers1, ev2)
        reg3 = Registration(pers2, ev3)
        reg4 = Registration(pers3, ev4)
        reg5 = Registration(pers1, ev3)
        reg6 = Registration(pers2, ev4)

        self.__repo.store(reg1)
        self.__repo.store(reg2)
        self.__repo.store(reg3)
        self.__repo.store(reg4)
        self.__repo.store(reg5)
        self.__repo.store(reg6)

    def test_find(self):
        r1 = self.__repo.find('1', '1')
        self.assertEqual(r1.getPerson().getName(), 'Arizona Andrews')
        self.assertEqual(r1.getPerson().getAddress(), 'First Street')
        self.assertEqual(r1.getEvent().getDate(), '01.01.2022')
        self.assertEqual(r1.getEvent().getTime(), '01:01')
        self.assertEqual(r1.getEvent().getDesc(), 'Date Night')

        r2 = self.__repo.find('8', '8')
        self.assertEqual(r2, None)

    def test_find_index(self):
        r1 = self.__repo.find_index('1', '1')
        self.assertEqual(r1, 0)

        r2 = self.__repo.find_index('2', '5')
        self.assertEqual(r2, -1)

    def test_store(self):
        pers = self.__pers_repo.find('2')
        ev = self.__ev_repo.find('1')
        reg = Registration(pers, ev)
        self.__repo.store(reg)
        self.assertEqual(self.__repo.size(), 7)

        self.assertRaises(ValueError, self.__repo.store, reg)

        self.__repo.delete('2', '1')

    def test_size(self):
        self.assertEqual(self.__repo.size(), 6)

        pers = self.__pers_repo.find('3')
        ev = self.__ev_repo.find('2')
        reg = Registration(pers, ev)
        self.__repo.store(reg)

        self.assertEqual(self.__repo.size(), 7)

        self.__repo.delete('3', '2')

    def test_get_all_registrations(self):
        crt_reg_list = self.__repo.get_all_registrations()
        self.assertEqual(type(crt_reg_list), list)
        self.assertEqual(len(crt_reg_list), 6)

        pers = self.__pers_repo.find('3')
        ev = self.__ev_repo.find('2')
        reg = Registration(pers, ev)
        self.__repo.store(reg)
        crt_reg_list = self.__repo.get_all_registrations()
        self.assertEqual(len(crt_reg_list), 7)

        self.assertEqual(self.__repo.get_all_registrations()[-1].getPerson().getName(), 'Cleopatra Candy')
        self.assertEqual(self.__repo.get_all_registrations()[-1].getPerson().getAddress(), 'Third Street')
        self.assertEqual(self.__repo.get_all_registrations()[-1].getEvent().getDate(), '02.02.2022')
        self.assertEqual(self.__repo.get_all_registrations()[-1].getEvent().getTime(), '02:02')
        self.assertEqual(self.__repo.get_all_registrations()[-1].getEvent().getDesc(), 'Drinking Night')

        self.__repo.delete('3', '2')

    def test_delete(self):
        pers = self.__pers_repo.find('3')
        ev = self.__ev_repo.find('3')
        reg = Registration(pers, ev)
        self.__repo.store(reg)
        self.assertEqual(self.__repo.size(), 7)

        self.__repo.delete('3', '3')
        self.assertEqual(self.__repo.size(), 6)

        self.assertRaises(ValueError, self.__repo.delete, '3', '3')

    def tearDown(self) -> None:
        self.__repo.delete_all()
