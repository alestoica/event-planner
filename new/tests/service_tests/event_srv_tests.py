import unittest

from domain.validators import EventValidator
from repository.event_repo import FileEventRepo
from service.event_service import EventService


class TestCaseEventService(unittest.TestCase):
    def setUp(self) -> None:
        repo = FileEventRepo('ev_srv_tests.txt')
        validator = EventValidator()
        self.__srv = EventService(repo, validator)

    def test_add_event(self):
        added_event = self.__srv.add_event('8', '08.08.2022', '08:08', 'Christmas Night')
        self.assertTrue(added_event.getDate() == '08.08.2022')
        self.assertTrue(added_event.getTime() == '08:08')
        self.assertTrue(added_event.getDesc() == 'Christmas Night')

        self.assertEqual(len(self.__srv.get_all_events()), 8)

        self.assertRaises(ValueError, self.__srv.add_event, '-1', '01.01.2022', '01:01', 'Movie Night')

    def test_get_all_events(self):
        # self.assertIsInstance(type(self.__srv.get_all_events()), list)
        self.assertEqual(len(self.__srv.get_all_events()), 7)

    def test_delete_event(self):
        deleted_event = self.__srv.delete_event('8')

        self.assertEqual(len(self.__srv.get_all_events()), 7)
        self.assertTrue(deleted_event.getDate() == '08.08.2022')
        self.assertTrue(deleted_event.getTime() == '08:08')
        self.assertTrue(deleted_event.getDesc() == 'Christmas Night')

        self.assertRaises(ValueError, self.__srv.delete_event, '10')

    def test_update_event(self):
        updated_event = self.__srv.update_event('1', '08.08.2022', '08:08', 'Christmas Night')

        self.assertTrue(updated_event.getDate() == '08.08.2022')
        self.assertTrue(updated_event.getTime() == '08:08')
        self.assertTrue(updated_event.getDesc() == 'Christmas Night')

        self.__srv.update_event('1', '01.01.2022', '01:01', 'Movie Night')

        self.assertRaises(ValueError, self.__srv.update_event, '5', 'NU', 'EXISTA', 'ID')

    def test_find_event(self):
        searched_event = self.__srv.find_event('1')

        self.assertTrue(searched_event.getDate() == '01.01.2022')
        self.assertTrue(searched_event.getTime() == '01:01')
        self.assertTrue(searched_event.getDesc() == 'Movie Night')

        self.assertRaises(ValueError, self.__srv.find_event, '10')
