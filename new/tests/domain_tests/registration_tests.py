import unittest

from domain.entities import Registration, Event, Person


class TestCaseRegistrationDomain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create_registration(self):
        ev = Event('1', '27.09.2022', '16:30', 'Festival de film')
        pers = Person('1', 'Arizona Andrews', 'First Street')

        registration = Registration(pers, ev)

        self.assertEqual(registration.getPerson(), pers)
        self.assertEqual(registration.getEvent(), ev)

    def test_equals_registration(self):
        ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')
        ev2 = Event('2', '28.09.2022', '20:30', 'Festival de filme frantuzesti')
        pers1 = Person('1', 'Arizona Andrews', 'First Street')

        registration1 = Registration(ev1, pers1)
        registration2 = Registration(ev1, pers1)

        self.assertEqual(registration1, registration2)

        registration3 = Registration(ev2, pers1)

        self.assertNotEqual(registration3, registration2)
