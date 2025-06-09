from data.turnos import turnos
from utils.colors_fx import green, blue, red
from factory.Agenda_factory import Agenda_factory as af

class Agenda_handler():
    def __init__(self, method = 'todo', especialidad = None):
        self.especialidad = especialidad
        self.tree = self._crear_tree(method, especialidad)


    def _crear_tree(self, method, especialidad):
        if method == 'esp' and especialidad:
            tree = af.por_especialidad(turnos, especialidad)
            depth = 0
            return (tree, depth)
        elif method == 'todo':
            tree = af.crear_todos(turnos)
            depth = 1
            return[tree, depth]
        else:
            raise Exception('No se han ingresado los argumentos correctos')
        
    def inorden(self, especialidad = None):

        if self.tree[1] == 0:
            green(self.especialidad.capitalize())
            self.tree[0].recorrido_inorden(self.tree[0].raiz)
        elif especialidad:
            green(especialidad.capitalize())
            self.tree[0][especialidad].recorrido_inorden(self.tree[0][especialidad].raiz)
        else:
            for k, v in self.tree[0].items():
                green(f'{k.capitalize()}:')
                self.tree[0][k].recorrido_inorden(self.tree[0][k].raiz)
    def  busqueda_hora(self, hora, especialidad = None):
        if self.tree[1] == 0:
            green(self.tree[0].buscar_por_hora(self.tree[0].raiz, hora))
        elif especialidad:
            green(self.tree[0][especialidad].buscar_por_hora(self.tree[0][especialidad].raiz, hora))
        else:
            for e in self.tree[0]:
                turno = self.tree[0][e].buscar_por_hora(self.tree[0][e].raiz, hora)
                if turno:
                    print(e.capitalize())
                    green(turno)

    def busqueda_dni(self, dni, especialidad = None):
        if self.tree[1]==0:
            green(self.tree[0].buscar_por_dni(self.tree[0].raiz, dni))
        elif especialidad:
            print(especialidad.capitalize())
            green(self.tree[0][especialidad].buscar_por_dni(self.tree[0][especialidad].raiz,dni))
        else:
            for k, v in self.tree[0].items():
                turno= self.tree[0][k].buscar_por_dni(self.tree[0][k].raiz,dni)
                if turno:
                    print(f'{k.capitalize()}')
                    green(turno)
                
