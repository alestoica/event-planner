# import unittest
#
# from repository.person_repo import FilePersonRepo
# from repository.event_repo import FileEventRepo
# from repository.registration_repo import FileRegistrationRepo
# from service.registration_service import RegistrationService
#
#
# class TestCaseRegistrationService(unittest.TestCase):
#     def setUp(self) -> None:
#         self.__person_repo = FilePersonRepo('data/people.txt')
#         self.__event_repo = FileEventRepo('data/events.txt')
#         repor = FileRegistrationRepo('reg_srv_tests.txt')
#         self.__srv = RegistrationService(repor, self.__person_repo, self.__event_repo)
#
#     def test_create_registration(self):
#         created_reg = self.__srv.create_registration('1', '4')
#
#         self.assertTrue(created_reg.getPerson() == self.__person_repo.find('1'))
#         self.assertTrue(created_reg.getEvent() == self.__event_repo.find('4'))
#
#         self.assertRaises(ValueError, self.__srv.create_registration, '1', '4')
#
#         self.__srv.delete_registration('1', '4')
#
#     def test_get_all_registration(self):
#         # self.assertIsInstance(type(self.__srv.get_all_registrations()), list)
#         self.assertEqual(len(self.__srv.get_all_registrations()), 6)
#
#     # def test_get_all_registrations_for_one_person(self):
#     #     self.assertTrue(self.__srv.get_all_registrations_for_one_person('5') == [])
#     #
#     # def test_get_all_registrations_for_one_event(self):
#     #     self.assertTrue(self.__srv.get_all_registrations_for_one_event('7') == [])
