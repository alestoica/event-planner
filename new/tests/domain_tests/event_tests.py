import unittest

from domain.entities import Event
from domain.validators import EventValidator


class TestCaseEventDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = EventValidator()

    def test_create_event(self):
        ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')
        self.assertEqual(ev1.getID(), '1')
        self.assertEqual(ev1.getDate(), '27.09.2022')
        self.assertEqual(ev1.getTime(), '16:30')
        self.assertEqual(ev1.getDesc(), 'Festival de film')

        ev1.setDate('28.09.2022')
        ev1.setTime('20:30')
        ev1.setDesc('Festival de filme frantuzesti')
        self.assertEqual(ev1.getID(), '1')
        self.assertEqual(ev1.getDate(), '28.09.2022')
        self.assertEqual(ev1.getTime(), '20:30')
        self.assertEqual(ev1.getDesc(), 'Festival de filme frantuzesti')

    def test_equals_event(self):
        ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')
        ev2 = Event('1', '27.09.2022', '16:30', 'Festival de film')
        self.assertEqual(ev1, ev2)

        ev3 = Event('2', '28.09.2022', '20:30', 'Festival de filme frantuzesti')
        self.assertNotEqual(ev1, ev3)

    def test_ev_validator(self):
        ev1 = Event('1', '01.01.2022', '01:01', 'Movie Night')
        self.__validator.validate(ev1)

        ev2 = Event('2', '-02.13', '24:-30', '')
        ev3 = Event('-1', '03.-10.2023', '22:60', 'Boat Party')
        self.assertRaises(ValueError, self.__validator.validate, ev2)
        self.assertRaises(ValueError, self.__validator.validate, ev3)
