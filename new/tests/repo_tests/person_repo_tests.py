import unittest

from domain.entities import Person
from repository.person_repo import PersonRepo, FilePersonRepo


class TestCaseClientRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = PersonRepo()
        self.__add_predefined_people()

    def __add_predefined_people(self):
        pers1 = Person('1', 'Arizona Andrews', 'First Street')
        pers2 = Person('2', 'Blake Brews', 'Second Street')
        pers3 = Person('3', 'Cleopatra Candy', 'Third Street')
        pers4 = Person('4', 'Dante DAlembert', 'Fourth Street')
        pers5 = Person('5', 'Eugene Erickson', 'Fifth Street')

        self.__repo.store(pers1)
        self.__repo.store(pers2)
        self.__repo.store(pers3)
        self.__repo.store(pers4)
        self.__repo.store(pers5)

    def test_find(self):
        p1 = self.__repo.find('3')
        self.assertEqual(p1.getName(), 'Cleopatra Candy')
        self.assertEqual(p1.getAddress(), 'Third Street')

        p2 = self.__repo.find('10')
        self.assertEqual(p2, None)

    def test_find_index(self):
        p1 = self.__repo.find_index('3')
        self.assertEqual(p1, 2)

        p2 = self.__repo.find_index('10')
        self.assertEqual(p2, -1)

    def test_store(self):
        initial_size = self.__repo.size()

        pers1 = Person('6', 'Frida Flower', 'Sixth Street')
        self.__repo.store(pers1)
        self.assertEqual(self.__repo.size(), initial_size + 1)

        self.assertRaises(ValueError, self.__repo.store, pers1)

        self.__repo.delete_by_id('6')

    def test_size(self):
        self.assertEqual(self.__repo.size(), 5)

        pers1 = Person('6', 'Florence Fury', 'Sixth Street')
        pers2 = Person('7', 'Gabrielle Grace', 'Seventh Street')
        self.__repo.store(pers1)
        self.__repo.store(pers2)

        self.assertEqual(self.__repo.size(), 7)

        self.__repo.delete_by_id('6')
        self.assertEqual(self.__repo.size(), 6)

        self.__repo.delete_by_id('7')
        self.assertEqual(self.__repo.size(), 5)

    def test_get_all_people(self):
        crt_pers_list = self.__repo.get_all_people()
        self.assertEqual(type(crt_pers_list), list)
        self.assertEqual(len(crt_pers_list), 5)

        pers = Person('6', 'Florence Fury', 'Sixth Street')
        self.__repo.store(pers)

        crt_pers_list = self.__repo.get_all_people()
        self.assertEqual(len(crt_pers_list), 6)

        self.assertEqual(self.__repo.get_all_people()[-1].getName(), 'Florence Fury')
        self.assertEqual(self.__repo.get_all_people()[-1].getAddress(), 'Sixth Street')

        self.__repo.delete_by_id('6')

    def test_delete(self):
        deleted_person = self.__repo.delete_by_id('5')
        self.assertEqual(deleted_person.getName(), 'Eugene Erickson')
        self.assertEqual(deleted_person.getAddress(), 'Fifth Street')

        assert (self.__repo.size() == 4)

        person_left = self.__repo.find('2')
        self.assertEqual(person_left.getName(), 'Blake Brews')
        self.assertEqual(person_left.getAddress(), 'Second Street')

        self.assertRaises(ValueError, self.__repo.delete_by_id, '5')

        pers = Person('5', 'Eugene Erickson', 'Fifth Street')
        self.__repo.store(pers)

    def test_update(self):
        pers3 = Person('6', 'Florence Fury', 'Sixth Street')

        modified_pers = self.__repo.update('2', pers3)
        self.assertEqual(modified_pers.getName(), 'Florence Fury')
        self.assertEqual(modified_pers.getAddress(), 'Sixth Street')

        pers = Person('2', 'Blake Brews', 'Second Street')
        self.__repo.update('6', pers)

        self.assertRaises(ValueError, self.__repo.update, '10', pers3)

    def tearDown(self) -> None:
        self.__repo.delete_all()
