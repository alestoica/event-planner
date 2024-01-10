from domain.entities import Person, Event


class PersonValidator:
    def validate(self, person):
        errors = []

        if person.getID().isnumeric() is False or int(person.getID()) <= 0:
            errors.append('Id-ul trebuie sa fie o valoare numerica pozitiva.')

        if len(person.getName()) <= 0:
            errors.append('Numele persoanei nu poate fi vid.')
        else:
            name = person.getName().split(' ')
            if len(name) < 2:
                errors.append('Numele introdus este invalid. Acesta trebuie sa contina'
                              ' un nume si cel putin un prenume, despartite prin spatiu.')
            elif name[0].isalpha() is False or name[1].isalpha() is False:
                errors.append('Numele trebuie sa fie format doar din litere.')

        if len(person.getAddress()) <= 0:
            errors.append('Adresa persoanei este invalida.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


def test_pers_validator():
    test_validator = PersonValidator()

    pers1 = Person('1', 'Arizona Andrews', 'First Street')
    test_validator.validate(pers1)

    pers2 = Person('2', '@ale', '')
    try:
        test_validator.validate(pers2)
        assert False
    except ValueError:
        assert True

    pers3 = Person('3', '', 'Kings Street')
    try:
        test_validator.validate(pers3)
        assert False
    except ValueError:
        assert True


test_pers_validator()


class EventValidator:
    def validate(self, event):
        errors = []

        if event.getID().isnumeric() is False or int(event.getID()) <= 0:
            errors.append('Id-ul trebuie sa fie o valoare numerica pozitiva.')

        date = event.getDate().split('.')
        if len(date) < 3:
            errors.append('Data introdusa este invalida. Aceasta trebuie sa contina'
                          ' o zi, o luna si un an, despartite prin punct.')
        else:
            if int(date[0]) <= 0 or int(date[1]) >= 32:
                errors.append('Ziua introdusa este invalida.')
            if int(date[1]) <= 0 or int(date[1]) >= 13:
                errors.append('Luna introdusa este invalida.')
            if int(date[2]) < 0 or int(date[2]) > 2022:
                errors.append('Anul introdus este invalida.')

        time = event.getTime().split(':')
        if len(time) < 2:
            errors.append('Ora introdusa este invalida. Aceasta trebuie sa specifice'
                          ' ora si minutul, despartite prin doua puncte.')
        else:
            if int(time[0]) < 0 or int(time[0]) > 23:
                errors.append('Ora introdusa este invalida.')
            if int(time[1]) < 0 or int(time[1]) > 59:
                errors.append('Minutul introdus este invalid.')

        if len(event.getDesc()) <= 0:
            errors.append('Descrierea nu poate fi vida.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


def test_ev_validator():
    test_validator = EventValidator()

    ev1 = Event('1', '01.01.2022', '01:01', 'Movie Night')
    test_validator.validate(ev1)

    ev2 = Event('2', '-02.13', '24:-30', '')
    try:
        test_validator.validate(ev2)
        assert False
    except ValueError:
        assert True

    ev3 = Event('-1', '03.-10.2023', '22:60', 'Boat Party')
    try:
        test_validator.validate(ev3)
        assert False
    except ValueError:
        assert True


test_ev_validator()
