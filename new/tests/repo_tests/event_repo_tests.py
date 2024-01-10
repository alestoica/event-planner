import unittest

from domain.entities import Event
from repository.event_repo import FileEventRepo, EventRepo


class TestCaseEventRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = EventRepo()
        self.__add_predefined_events()

    def __add_predefined_events(self):
        ev1 = Event('1', '01.01.2022', '01:01', 'Movie Night')
        ev2 = Event('2', '02.02.2022', '02:02', 'Drinking Night')
        ev3 = Event('3', '03.03.2022', '03:03', 'Dancing Night')
        ev4 = Event('4', '04.04.2022', '04:04', 'Rock Night')

        self.__repo.store(ev1)
        self.__repo.store(ev2)
        self.__repo.store(ev3)
        self.__repo.store(ev4)

    def test_find(self):
        e1 = self.__repo.find('3')
        self.assertEqual(e1.getDate(), '03.03.2022')
        self.assertEqual(e1.getTime(), '03:03')
        self.assertEqual(e1.getDesc(), 'Dancing Night')

        e2 = self.__repo.find('10')
        self.assertEqual(e2, None)

    def test_find_index(self):
        e1 = self.__repo.find_index('4')
        self.assertEqual(e1, 3)

        e2 = self.__repo.find_index('10')
        self.assertEqual(e2, -1)

    def test_store_w(self):
        ev1 = Event('5', '05.05.2022', '05:05', 'Salsa Night')
        self.__repo.store(ev1)
        self.assertEqual(self.__repo.size(), 5)

        ev2 = Event('6', '06.06.2022', '06:06', 'Games Night')
        self.__repo.store(ev2)
        self.assertEqual(self.__repo.size(), 6)

        self.assertRaises(ValueError, self.__repo.store, ev2)

        self.__repo.delete_by_id('5')
        self.__repo.delete_by_id('6')

    def test_store_b(self):
        ev1 = Event('5', '05.05.2022', '05:05', 'Salsa Night')
        self.__repo.store(ev1)
        self.assertEqual(self.__repo.size(), 5)

        ev2 = Event('6', '06.06.2022', '06:06', 'Games Night')
        self.__repo.store(ev2)
        self.assertEqual(self.__repo.size(), 6)

        self.assertRaises(ValueError, self.__repo.store, ev2)

        self.__repo.delete_by_id('5')
        self.__repo.delete_by_id('6')

    def test_size(self):
        self.assertEqual(self.__repo.size(), 4)

        ev1 = Event('8', '08.08.2022', '08:08', 'Girls Night')
        ev2 = Event('9', '09.09.2022', '09:09', 'Christmas Night')
        self.__repo.store(ev1)
        self.__repo.store(ev2)

        self.assertEqual(self.__repo.size(), 6)

        self.__repo.delete_by_id('8')
        self.assertEqual(self.__repo.size(), 5)

        self.__repo.delete_by_id('9')
        self.assertEqual(self.__repo.size(), 4)

    def test_get_all_events(self):
        crt_ev_list = self.__repo.get_all_events()
        self.assertEqual(type(crt_ev_list), list)
        self.assertEqual(len(crt_ev_list), 4)

        ev = Event('10', '10.10.2022', '10:10', 'The Voice Night')
        self.__repo.store(ev)
        self.assertEqual(self.__repo.size(), 5)

        self.assertEqual(self.__repo.get_all_events()[-1].getDate(), '10.10.2022')
        self.assertEqual(self.__repo.get_all_events()[-1].getTime(), '10:10')
        self.assertEqual(self.__repo.get_all_events()[-1].getDesc(), 'The Voice Night')

        self.__repo.delete_by_id('10')

    def test_delete(self):
        deleted_event = self.__repo.delete_by_id('4')
        self.assertEqual(deleted_event.getDate(), '04.04.2022')
        self.assertEqual(deleted_event.getTime(), '04:04')
        self.assertEqual(deleted_event.getDesc(), 'Rock Night')

        self.assertEqual(self.__repo.size(), 3)

        event_left = self.__repo.find('3')
        self.assertEqual(event_left.getDate(), '03.03.2022')
        self.assertEqual(event_left.getTime(), '03:03')
        self.assertEqual(event_left.getDesc(), 'Dancing Night')

        self.assertRaises(ValueError, self.__repo.delete_by_id, '4')

        ev = Event('4', '04.04.2022', '04:04', 'Rock Night')
        self.__repo.store(ev)

    def test_update(self):
        ev3 = Event('11', '11.11.2022', '11:11', 'Halloween Night')

        modified_ev = self.__repo.update('4', ev3)
        self.assertEqual(modified_ev.getDate(), '11.11.2022')
        self.assertEqual(modified_ev.getTime(), '11:11')
        self.assertEqual(modified_ev.getDesc(), 'Halloween Night')

        ev = Event('4', '04.04.2022', '04:04', 'Rock Night')
        self.__repo.update('11', ev)

        self.assertRaises(ValueError, self.__repo.update, '12', ev3)

    def tearDown(self) -> None:
        self.__repo.delete_all()
