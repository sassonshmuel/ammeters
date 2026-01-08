from Ammeters.Circutor_Ammeter import CircutorAmmeter
from Ammeters.Entes_Ammeter import EntesAmmeter
from Ammeters.Greenlee_Ammeter import GreenleeAmmeter


def run_greenlee_emulator():
    greenlee = GreenleeAmmeter(5001)
    greenlee.start_server()

def run_entes_emulator():
    entes = EntesAmmeter(5002)
    entes.start_server()

def run_circutor_emulator():
    circutor = CircutorAmmeter(5003)
    circutor.start_server()
