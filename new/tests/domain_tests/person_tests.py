import unittest

from domain.entities import Person
from domain.validators import PersonValidator


class TestCasePersonDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = PersonValidator()

    def test_create_person(self):
        pers1 = Person('1', 'Arizona Andrews', 'First Street')
        self.assertEqual(pers1.getID(), '1')
        self.assertEqual(pers1.getName(), 'Arizona Andrews')
        self.assertEqual(pers1.getAddress(), 'First Street')

        pers1.setName('Ariel Andrews')
        pers1.setAddress('Minus Street')
        self.assertEqual(pers1.getID(), '1')
        self.assertEqual(pers1.getName(), 'Ariel Andrews')
        self.assertEqual(pers1.getAddress(), 'Minus Street')

    def test_equals_person(self):
        pers1 = Person('1', 'Arizona Andrews', 'First Street')
        pers2 = Person('1', 'Arizona Andrews', 'First Street')
        self.assertEqual(pers1, pers2)

        pers3 = Person('2', 'Blake Brews', 'Second Street')
        self.assertNotEqual(pers1, pers3)

    def test_pers_validator(self):
        pers1 = Person('1', 'Arizona Andrews', 'First Street')
        self.__validator.validate(pers1)

        pers2 = Person('2', '@ale', '')
        pers3 = Person('3', '', 'Kings Street')
        self.assertRaises(ValueError, self.__validator.validate, pers2)
        self.assertRaises(ValueError, self.__validator.validate, pers3)
