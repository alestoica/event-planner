import unittest

from domain.entities import Person
from domain.validators import PersonValidator
from repository.person_repo import FilePersonRepo
from service.person_service import PersonService


class TestCasePersonService(unittest.TestCase):
    def setUp(self) -> None:
        repo = FilePersonRepo('pers_srv_tests.txt')
        validator = PersonValidator()
        self.__srv = PersonService(repo, validator)

    def test_add_person(self):
        added_person = self.__srv.add_person('6', 'Florence Fury', 'Sixth Street')
        self.assertTrue(added_person.getName() == 'Florence Fury')
        self.assertTrue(added_person.getAddress() == 'Sixth Street')

        self.assertEqual(len(self.__srv.get_all_people()), 6)

        self.__srv.delete_person('6')

        self.assertRaises(ValueError, self.__srv.add_person, '-1', 'Ar1zona Andrews', 'First Street')

    def test_get_all_people(self):
        # self.assertIsInstance(type(self.__srv.get_all_people()), list)
        self.assertEqual(len(self.__srv.get_all_people()), 5)

        self.__srv.add_person('6', 'Florence Fury', 'Sixth Street')
        self.assertEqual(len(self.__srv.get_all_people()), 6)

        self.__srv.delete_person('6')

    def test_delete_person(self):
        deleted_person = self.__srv.delete_person('5')

        self.assertEqual(len(self.__srv.get_all_people()), 4)
        self.assertTrue(deleted_person.getName() == 'Eugene Erickson')
        self.assertTrue(deleted_person.getAddress() == 'Fifth Street')

        self.__srv.add_person('5', 'Eugene Erickson', 'Fifth Street')

        self.assertRaises(ValueError, self.__srv.delete_person, '10')

    def test_update_person(self):
        updated_person = self.__srv.update_person('1', 'A A', 'F S')

        self.assertTrue(updated_person.getName() == 'A A')
        self.assertTrue(updated_person.getAddress() == 'F S')

        self.__srv.update_person('1', 'Arizona Andrews', 'First Street')

        self.assertRaises(ValueError, self.__srv.update_person, '10', 'NU', 'EXISTA')

    def test_find_person(self):
        searched_person = self.__srv.find_person('1')

        self.assertTrue(searched_person.getName() == 'Arizona Andrews')
        self.assertTrue(searched_person.getAddress() == 'First Street')

        self.assertRaises(ValueError, self.__srv.find_person, '10')
