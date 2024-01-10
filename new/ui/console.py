from termcolor import colored
from ui.generate import GenerateP, GenerateE, GenerateR

menu = {
    1: 'generate people',
    2: 'generate events',
    3: 'generate registrations',
    4: 'show all people',
    5: 'show all events',
    6: 'show all registrations',
    7: 'find person',
    8: 'find event',
    9: 'add person',
    10: 'add event',
    11: 'create registration',
    12: 'delete person',
    13: 'delete event',
    14: 'update person',
    15: 'update event',
    16: 'show all events for one person, sorted by description and date',
    17: 'show people registered for most events',
    18: '20% events with most participants',
    19: 'show all people registered for no events',
    20: 'stop'
}


def print_menu(crt_menu):
    for key in crt_menu.keys():
        print(key, ' - ', crt_menu[key])


class Console:
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

    def __print_people(self, pers_list):
        """
        Afiseaza o lista de persoane
        """
        if len(pers_list) == 0:
            print(colored('the list is empty.', 'red'))
        else:
            print('the list is: ')
            for pers in pers_list:
                print('ID:', colored(pers.getID(), 'magenta'), '; Name:', colored(pers.getName(), 'magenta'),
                      '; Address:', colored(pers.getAddress(), 'magenta'))

    def __add_person(self):
        """
        Adauga o persoana cu datele citite de la tastatura
        """
        try:
            id = input('ID: ')
            name = input('name: ')
            address = input('address: ')
            added_pers = self.__srvp.add_person(id, name, address)
            print('person' + colored(added_pers.getName(), 'magenta') + '(ID:' +
                  colored(added_pers.getID(), 'magenta') + ') has been successfully added.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __delete_person(self):
        """
        Sterge persoana cu id-ul citit de la tastatura
        """
        try:
            id = input('ID of the person that has to be deleted: ')
            deleted_pers = self.__srvp.delete_person(id)
            print('person' + colored(deleted_pers.getName(), 'magenta') + ' (ID: ' +
                  colored(deleted_pers.getID(), 'magenta') + ') has been successfully deleted.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_person(self):
        """
        Modifica persoana cu id-ul citit de la tastatura cu noile date citite
        """
        try:
            id = input('ID of the person that has to be modified: ')
            name = input('new name: ')
            address = input('new address: ')
            modified_pers = self.__srvp.update_person(id, name, address)
            print('person' + colored(modified_pers.getName(), 'magenta') + '(ID:' +
                  colored(modified_pers.getID(), 'magenta') + ') has been successfully modified.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_person(self):
        """
        Cauta persoana cu id-ul dat
        """
        try:
            id = input('ID of the searched person: ')
            searched_pers = self.__srvp.find_person(id)
            print('the searched person is: ' + colored(searched_pers.getName(), 'magenta') + '(ID:' +
                  colored(searched_pers.getID(), 'magenta') + ')')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __print_events(self, ev_list):
        """
        Afiseaza o lista de evenimente
        """
        if len(ev_list) == 0:
            print(colored('Nu exista evenimente in lista.', 'red'))
        else:
            print('Lista de evenimente este: ')
            for ev in ev_list:
                print('ID:', colored(ev.getID(), 'magenta'), '; Date:', colored(ev.date(), 'magenta'),
                      '; Time:', colored(ev.time(), 'magenta'), '; Description:', colored(ev.getDesc(), 'magenta'))

    def __add_event(self):
        """
        Adauga un eveniment cu datele citite de la tastatura
        """
        try:
            id = input('Identificator eveniment: ')
            date = input('Data: ')
            time = input('Ora: ')
            desc = input('Descrierea evenimentului: ')
            added_ev = self.__srve.add_event(id, date, time, desc)
            print('Evenimentul' + colored(added_ev.getDesc(), 'magenta') + '(ID:' +
                  colored(added_ev.getID(), 'magenta') + '), care va avea loc in data' +
                  str(colored(added_ev.date(), 'magenta')) + ', la ora' +
                  str(colored(added_ev.time(), 'magenta')) + ', a fost adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __delete_event(self):
        """
        Sterge evenimentul cu id-ul citit de la tastatura
        """
        try:
            id = input('Identificatorul evenimentului care trebuie sters: ')
            deleted_ev = self.__srve.delete_event(id)
            print('Evenimentul' + colored(deleted_ev.getDesc(), 'magenta') + '(ID:' +
                  colored(deleted_ev.getID(), 'magenta') + '), care va avea loc in data' +
                  colored(deleted_ev.date(), 'magenta') + ', la ora' +
                  colored(deleted_ev.time(), 'magenta') + ', a fost sters cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_event(self):
        """
        Modifica evenimentul cu id-ul citit de la tastatura cu noile date citite
        """
        try:
            id = input('Identificatorul evenimentului care trebuie modificata: ')
            date = input('Noua data: ')
            time = input('Noua ora: ')
            desc = input('Noua descriere a evenimentului: ')
            modified_ev = self.__srve.update_event(id, date, time, desc)
            print('Evenimentul' + colored(modified_ev.getDesc(), 'magenta') + '(ID:' +
                  colored(modified_ev.getID(), 'magenta') + '), care va avea loc in data' +
                  colored(modified_ev.date(), 'magenta') + ', la ora' +
                  colored(modified_ev.time(), 'magenta') + ', a fost modificat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_event(self):
        """
        Cauta evenimentul cu id-ul dat
        """
        try:
            id = input('Identificatorul evenimentului cautat: ')
            searched_ev = self.__srve.find_event(id)
            print('Evenimentul cautat este: ' + colored(searched_ev.getDesc(), 'magenta') + '(ID:' +
                  colored(searched_ev.getID(), 'magenta') + '), care va avea loc in data' +
                  colored(searched_ev.date(), 'magenta') + ', la ora' +
                  colored(searched_ev.time(), 'magenta'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __print_registrations(self, reg_list):
        """
        Afiseaza o lista de inscrieri
        """
        if len(reg_list) == 0:
            print('Nu exista inscrieri in lista.')
        else:
            print('Lista de inscrieri este: ')
            for reg in reg_list:
                print('Person: [', colored(reg.getPerson().getName(), 'cyan'), '; ',
                      colored(reg.getPerson().getAddress(), 'cyan'), ']',
                      '\nEvent: [', colored(reg.getEvent().date(), 'cyan'), '; ',
                      colored(reg.getEvent().time(), 'cyan'), '; ',
                      colored(reg.getEvent().getDesc(), 'cyan'), ']\n')

    def __assign_registration(self):
        try:
            id_pers = input('ID-ul persoanei: ')
            id_event = input('ID-ul evenimentului: ')
            reg = self.__srvr.create_registration(id_pers, id_event)
            print('Persoana', reg.getPerson().getName(), 'a fost inscrisa cu succes la evenimentul',
                  reg.getEvent().getDesc(), '.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __sort_registrations_for_one_person(self):
        try:
            id_pers = input('ID-ul persoanei: ')
            print('Rezultatele pot fi gasite in fisierul raport.txt!')
            ev_list = self.__srvr.sort_registrations_for_one_pers(id_pers)
            f = open('raport.txt', 'w')
            if len(ev_list) == 0:
                f.write('Persoana ' + self.__srvp.find_person(id_pers).getName() + ' nu este inscrisa la niciun eveniment.')
            else:
                f.write('Persoana ' + self.__srvp.find_person(id_pers).getName() + ' este inscrisa la evenimentele: ')
                f.write('\n')
                for ev in ev_list:
                    f.write('ID:' + colored(ev.getID(), 'magenta') + '; Date:' + str(colored(ev.date(), 'magenta')) +
                            '; Time:' + str(colored(ev.time(), 'magenta')) + '; Description:' + colored(ev.getDesc(),
                                                                                                   'magenta'))
                    f.write('\n')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __get_people_with_most_events(self):
        pers_list = self.__srvp.get_all_people()
        no_events = self.__srvr.get_no_events_for_each_person()
        max_value = max(no_events.values())
        print('Numarul maxim de evenimente la care este inscrisa o persoana este: ', max_value)
        print('Persoanele care sunt inscrise la', max_value, 'evenimente sunt: ')
        for p in pers_list:
            if len(self.__srvr.get_all_registrations_for_one_person(p.getID())) == max(no_events.values()):
                print('[ ID:', p.getID(), '; Name:', p.getName(), ']')

    def __20_percent_events_with_most_participants(self):
        no_people = self.__srvr.get_no_people_for_each_event()
        no_events = len(self.__srve.get_all_events())
        no_ev_print = int((20 * no_events) / 100)
        print('the first 20% events with most participants are: ')
        for k in no_people.keys():
            if no_ev_print > 0:
                no_ev_print = no_ev_print - 1
                print(self.__srve.find_event(k))
            else:
                break

    def __get_people_registered_for_no_events(self):
        try:
            pers_list = self.__srvp.get_all_people()
            for p in pers_list:
                if len(self.__srvr.get_all_registrations_for_one_person(p.getID())) == 0:
                    print('[ ID:', p.getID(), '; Name:', p.getName(), ']')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def ui(self):
        while True:
            print('available commands: ')
            print_menu(menu)
            cmd = input('your command: ')
            cmd = int(cmd)

            if cmd == 1:
                nr = input('the number of people that will be generated: ')
                pers_generator = GenerateP(self.__srvp)
                pers_generator.generate_persons(int(nr))
                print('people generated successfully!')
            elif cmd == 2:
                nr = input('the number of events that will be generated: ')
                ev_generator = GenerateE(self.__srve)
                ev_generator.generate_events(int(nr))
                print('events generated successfully!')
            elif cmd == 3:
                nr = input('the number of registrations that will be generated: ')
                reg_generator = GenerateR(self.__srvp, self.__srve, self.__srvr)
                reg_generator.generate_registrations(int(nr))
                print('registrations generated successfully!')
            elif cmd == 4:
                self.__print_people(self.__srvp.get_all_people())
            elif cmd == 5:
                self.__print_events(self.__srve.get_all_events())
            elif cmd == 6:
                self.__print_registrations(self.__srvr.get_all_registrations())
            elif cmd == 7:
                self.__find_person()
            elif cmd == 8:
                self.__find_event()
            elif cmd == 9:
                self.__add_person()
            elif cmd == 10:
                self.__add_event()
            elif cmd == 11:
                self.__assign_registration()
            elif cmd == 12:
                self.__delete_person()
            elif cmd == 13:
                self.__delete_event()
            elif cmd == 14:
                self.__update_person()
            elif cmd == 15:
                self.__update_event()
            elif cmd == 16:
                self.__sort_registrations_for_one_person()
            elif cmd == 17:
                self.__get_people_with_most_events()
            elif cmd == 18:
                self.__20_percent_events_with_most_participants()
            elif cmd == 19:
                self.__get_people_registered_for_no_events()
            elif cmd == 20:
                break
            else:
                print(colored('invalid command.', 'red'))
