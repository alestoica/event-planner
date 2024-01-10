import random
from termcolor import colored

names = ['Arizona Andrews', 'Blake Brews', 'Cleopatra Candy', 'Dante DAlembert', 'Eugene Erickson']
addresses = ['First Street', 'Second Street', 'Third Street', 'Fourth Street', 'Fifth Street']

description = ['Movie Night', 'Drinking Night', 'Dancing Night', 'Rock Night', 'Salsa Night']


class GenerateP:
    def __init__(self, srvp):
        """
        Initializeaza consola
        :type srvp: PersonService
        """
        self.__srvp = srvp

    def generate_persons(self, nr):
        ok = False
        while True:
            try:
                while nr:
                    id = random.randint(1, 100)
                    name = random.choice(names)
                    address = random.choice(addresses)
                    self.__srvp.add_person(str(id), name, address)
                    nr = nr - 1
            except ValueError as ve:
                if ok is False:
                    print(colored(str(ve), 'red'))
                    ok = True
                continue
            else:
                break


class GenerateE:
    def __init__(self, srve):
        """
        Initializeaza consola
        :type srve: EventService
        """
        self.__srve = srve

    def generate_events(self, nr):
        ok = False
        while True:
            try:
                while nr:
                    id = random.randint(1, 100)
                    day = random.randint(1, 31)
                    month = random.randint(1, 12)
                    year = random.randint(1500, 2022)
                    Date = [str(day), str(month), str(year)]
                    date = '.'.join(Date)
                    hour = random.randint(1, 23)
                    minute = random.randint(1, 59)
                    Time = [str(hour), str(minute)]
                    time = ':'.join(Time)
                    desc = random.choice(description)
                    self.__srve.add_event(str(id), date, time, desc)
                    nr = nr - 1
            except ValueError as ve:
                if ok is False:
                    print(colored(str(ve), 'red'))
                    ok = True
                continue
            else:
                break


class GenerateR:
    def __init__(self, srvp, srve, srvr):
        """
        Initializeaza consola
        :type srvp: PersonService
        :type srve: EventService
        :type srvr: RegistrationService
        """
        self.__srvp = srvp
        self.__srve = srve
        self.__srvr = srvr

    def generate_registrations(self, nr):
        ok = False
        while True:
            try:
                pers_generator = GenerateP(self.__srvp)
                pers_generator.generate_persons(nr)
                ev_generator = GenerateE(self.__srve)
                ev_generator.generate_events(nr)
                while nr:
                    person = random.choice(self.__srvp.get_all_people())
                    idp = person.getID()
                    event = random.choice(self.__srve.get_all_events())
                    ide = event.getID()
                    self.__srvr.create_registration(idp, ide)
                    nr = nr - 1
            except ValueError as ve:
                if ok is False:
                    print(colored(str(ve), 'red'))
                    ok = True
                continue
            else:
                break
