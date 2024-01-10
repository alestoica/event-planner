from domain.entities import Person
from domain.validators import PersonValidator
from repository.person_repo import FilePersonRepo


class PersonService:
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de persoane
        :type repo: FilePersonRepo
        :param validator: validator pentru verificarea persoanelor
        :type validator: PersonValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_person(self, id, name, address):
        """
        Adaug persoana
        :param id: id-ul persoanei
        :type id: str
        :param name: numele persoanei
        :type name: str
        :param address: adresa persoanei
        :type address: str
        :return: obiectul de tip Person
        :rtype: -; Persoana s-a adaugat in lista
        :raises: ValueError daca persoana are date invalide, daca id-ul exista deja in lista
        """
        p = Person(id, name, address)
        self.__validator.validate(p)
        self.__repo.store(p)
        return p

    def get_all_people(self):
        """
        Returneaza o lista cu toate persoanele disponibile
        :return: lista de persoane disponibile
        :rtype: lista de obiecte de tip Person
        """
        return self.__repo.get_all_people()

    def delete_person(self, id):
        """
        Sterge din lista persoana cu id dat
        :param id: id-ul dat
        :type id: str
        :return: persoana stearsa
        :rtype: Person
        :raises: ValueError daca nu exista persoana cu id-ul dat
        """
        return self.__repo.delete_by_id(id)

    def update_person(self, id, name, address):
        """
        Modifica datele persoanei cu id-ul dat
        :param id: id-ul persoanei care trebuie modificata
        :type id: str
        :param name: noul nume al persoanei
        :type name: str
        :param address: noua adresa a persoanei
        :type address: str
        :return: persoana modificata
        :rtype: Person
        :raises: ValueError daca noile date nu sunt valide, sau nu exista persoana cu id dat
        """
        p = Person(id, name, address)
        self.__validator.validate(p)
        return self.__repo.update(id, p)

    def find_person(self, id):
        """
        Cauta persoana cu id-ul dat
        :param id: id-ul persoanei cautate
        :type id: str
        :return: persoana cautata
        :rtype: Person
        """
        if self.__repo.find(id) is None:
            raise ValueError('Persoana cautata nu exista.')
        else:
            return self.__repo.find(id)


def test_add_person():
    repo = FilePersonRepo('data/test_people_srv.txt')
    validator = PersonValidator()
    test_service = PersonService(repo, validator)

    added_person = test_service.add_person('6', 'Florence Fury', 'Sixth Street')
    assert (added_person.getName() == 'Florence Fury')
    assert (added_person.getAddress() == 'Sixth Street')

    assert (len(test_service.get_all_people()) == 6)

    test_service.delete_person('6')

    try:
        test_service.add_person('-1', 'Ar1zona Andrews', 'First Street')
        assert False
    except ValueError:
        assert True


def test_get_all_people():
    repo = FilePersonRepo('data/test_people_srv.txt')
    validator = PersonValidator()
    test_service = PersonService(repo, validator)

    assert (type(test_service.get_all_people()) == list)
    assert (len(test_service.get_all_people()) == 5)

    test_service.add_person('6', 'Florence Fury', 'Sixth Street')
    assert (len(test_service.get_all_people()) == 6)


# def test_delete_person():
#     repo = FilePersonRepo('data/test_people_srv.txt')
#     validator = PersonValidator()
#     test_service = PersonService(repo, validator)
#
#     deleted_person = test_service.delete_person('6')
#
#     assert (len(test_service.get_all_people()) == 5)
#     assert (deleted_person.getName() == 'Florence Fury')
#     assert (deleted_person.getAddress() == 'Sixth Street')
#
#     try:
#         test_service.delete_person('10')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_update_person():
#     repo = FilePersonRepo('data/test_people_srv.txt')
#     validator = PersonValidator()
#     test_service = PersonService(repo, validator)
#
#     updated_person = test_service.update_person('1', 'A A', 'F S')
#
#     assert (updated_person.getName() == 'A A')
#     assert (updated_person.getAddress() == 'F S')
#
#     test_service.update_person('1', 'Arizona Andrews', 'First Street')
#
#     try:
#         test_service.update_person('10', 'NU', 'EXISTA')
#         assert False
#     except ValueError:
#         assert True
#
#
# def test_find_person():
#     repo = FilePersonRepo('data/test_people_srv.txt')
#     validator = PersonValidator()
#     test_service = PersonService(repo, validator)
#
#     searched_person = test_service.find_person('1')
#
#     assert (searched_person.getName() == 'Arizona Andrews')
#     assert (searched_person.getAddress() == 'First Street')
#
#     try:
#         test_service.find_person('10')
#         assert False
#     except ValueError:
#         assert True
#
#
# test_add_person()
# test_get_all_people()
# test_delete_person()
# test_update_person()
# test_find_person()
