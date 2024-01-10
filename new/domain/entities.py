import datetime


class Person:
    no_instances = 0

    def __init__(self, id, name, address):
        """
        Creeaza o noua persoana cu id, nume si adresa date
        :param id: id-ul persoanei
        :type id: str
        :param name: numele persoanei
        :type name: str
        :param address: adresa la care locuieste persoana
        :type address: str
        """
        self.__id_p = id
        self.__name = name
        self.__address = address
        Person.no_instances += 1

    def getID(self):
        return self.__id_p

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setID(self, value):
        self.__id_p = value

    def setName(self, value):
        self.__name = value

    def setAddress(self, value):
        self.__address = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre persoana curenta si persoana other
        :param other:
        :type other: Person
        :return: True daca persoanele sunt aceleasi (acelasi id), False altfel
        :rtype: bool
        """
        if self.__id_p == other.getID():
            return True
        return False

    def __str__(self):
        return "Person ID: " + self.__id_p + '; Nume: ' + self.__name + '; Adresa: ' + self.__address

    @staticmethod
    def getNumberOfPersonObjects():
        return Person.no_instances


def test_create_person():
    pers1 = Person('1', 'Arizona Andrews', 'First Street')

    assert (pers1.getID() == '1')
    assert (pers1.getName() == 'Arizona Andrews')
    assert (pers1.getAddress() == 'First Street')

    pers1.setName('Ariana Andrews')
    pers1.setAddress('Zero Street')

    assert (pers1.getID() == '1')
    assert (pers1.getName() == 'Ariana Andrews')
    assert (pers1.getAddress() == 'Zero Street')

    pers2 = Person('2', 'Blake Brews', 'Second Street')

    assert (pers2.getID() == '2')
    assert (pers2.getName() == 'Blake Brews')
    assert (pers2.getAddress() == 'Second Street')


def test_equals_person():
    pers1 = Person('1', 'Arizona Andrews', 'First Street')
    pers2 = Person('1', 'Arizona Andrews', 'First Street')
    assert (pers1 == pers2)

    pers3 = Person('2', 'Blake Brews', 'Second Street')
    assert (pers1 != pers3)


test_create_person()
test_equals_person()


class Event:
    no_instances = 0

    def __init__(self, id, date, time, desc):
        """
        Creeaza o noua persoana cu id, nume si adresa date
        :param id: id-ul evenimentului
        :type id: str
        :param date: data evenimentului
        :type date: str
        :param time: ora la care incepe evenimentul
        :type time: str
        :param desc: descrierea evenimentului
        :type desc: str
        """
        self.__id_e = id
        self.__date = date
        self.__time = time
        self.__desc = desc
        Event.no_instances += 1

    def getID(self):
        return self.__id_e

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getDesc(self):
        return self.__desc

    def setID(self, value):
        self.__id_e = value

    def setDate(self, value):
        self.__date = value

    def setTime(self, value):
        self.__time = value

    def setDesc(self, value):
        self.__desc = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre evenimentul curent si evenimentul other
        :param other:
        :type other: Event
        :return: True daca evenimentele sunt aceleasi (acelasi id), False altfel
        :rtype: bool
        """
        if self.__id_e == other.getID():
            return True
        return False

    def __str__(self):
        return 'Event ID: ' + self.__id_e + '; Date: ' + self.__date + '; Time: ' + self.__time + \
               '; Description: ' + self.__desc

    def date(self):
        date = self.getDate()
        date = date.split('.')
        new_date = datetime.date(int(date[2]), int(date[1]), int(date[0]))
        return new_date

    def time(self):
        time = self.getTime()
        time = time.split(':')
        new_time = datetime.time(int(time[0]), int(time[1])).strftime("%H:%M")
        return new_time

    @staticmethod
    def getNumberOfEventObjects():
        return Event.no_instances


def test_create_event():
    ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')

    assert (ev1.getID() == '1')
    assert (ev1.getDate() == '27.09.2022')
    assert (ev1.getTime() == '16:30')
    assert (ev1.getDesc() == 'Festival de film')

    ev1.setDate('28.09.2022')
    ev1.setTime('20:30')
    ev1.setDesc('Festival de filme frantuzesti')

    assert (ev1.getID() == '1')
    assert (ev1.getDate() == '28.09.2022')
    assert (ev1.getTime() == '20:30')
    assert (ev1.getDesc() == 'Festival de filme frantuzesti')


def test_equals_event():
    ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')
    ev2 = Event('1', '27.09.2022', '16:30', 'Festival de film')
    assert (ev1 == ev2)

    ev3 = Event('2', '28.09.2022', '20:30', 'Festival de filme frantuzesti')
    assert (ev1 != ev3)


test_create_event()
test_equals_event()


class Registration:
    def __init__(self, person, event):
        self.__person = person
        self.__event = event

    def getPerson(self):
        return self.__person

    def getEvent(self):
        return self.__event

    def setPerson(self, value):
        self.__person = value

    def setEvent(self, value):
        self.__event = value

    def __eq__(self, other):
        if self.__person == other.__person and self.__event == other.__event:
            return True
        return False

    def __str__(self):
        return 'Persoana: [' + str(self.__person.getName()) + '; ' + str(self.__person.getAddress) + ']' + \
               'Event: [' + str(self.__event.getDate()) + ';' + str(self.__event.getTime()) + ';' + \
               str(self.__event.getDesc) + ']'


def test_create_registration():
    ev = Event('1', '27.09.2022', '16:30', 'Festival de film')
    pers = Person('1', 'Arizona Andrews', 'First Street')

    registration = Registration(pers, ev)

    assert (registration.getPerson() == pers)
    assert (registration.getEvent() == ev)


def test_equals_registration():
    ev1 = Event('1', '27.09.2022', '16:30', 'Festival de film')
    ev2 = Event('2', '28.09.2022', '20:30', 'Festival de filme frantuzesti')
    pers1 = Person('1', 'Arizona Andrews', 'First Street')

    registration1 = Registration(ev1, pers1)
    registration2 = Registration(ev1, pers1)

    assert (registration1 == registration2)

    registration3 = Registration(ev2, pers1)

    assert (registration3 != registration2)


test_create_registration()
test_equals_registration()
