from utils.fx import crear_lista_turnos
from classes.Arbol_turnos import ArbolTurnos
from classes.Turno import Turno

class Agenda_factory():
    @staticmethod
    def por_especialidad(data, especialidad):
        return ArbolTurnos(crear_lista_turnos(data,especialidad))

    def crear_todos(data):
        agenda = {}

        for t in data:
            especialidad = t['especialidad'].lower()
            agenda.setdefault(especialidad, []).append(t)

        return {
            esp: ArbolTurnos([Turno(t['dni'], t['nombre'], t['hora']) for t in turnos]) for esp, turnos in agenda.items()
        }