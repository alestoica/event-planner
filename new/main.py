from domain.validators import PersonValidator, EventValidator
from repository.person_repo import FilePersonRepo
from repository.event_repo import FileEventRepo
from repository.registration_repo import FileRegistrationRepo
from service.person_service import PersonService
from service.event_service import EventService
from service.registration_service import RegistrationService
from ui.console import Console

repop = FilePersonRepo('data/people.txt')
valp = PersonValidator()
srvp = PersonService(repop, valp)

repoe = FileEventRepo('data/events.txt')
vale = EventValidator()
srve = EventService(repoe, vale)

repor = FileRegistrationRepo('data/registrations.txt')
srvr = RegistrationService(repor, repop, repoe)

ui = Console(srvp, srve, srvr)
ui.ui()
