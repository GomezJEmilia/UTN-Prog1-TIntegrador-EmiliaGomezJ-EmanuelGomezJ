from classes.Nodo import Nodo

class ArbolTurnos:
    def __init__(self, lista = None):
        self.raiz = None
        lista and self._crear_arbol_turnos(lista)

    def _crear_arbol_turnos(self,lista_turnos):
        for turno in lista_turnos:
            self.insertar(turno)

    def insertar(self, turno):
        if self.raiz is None:
            self.raiz = Nodo(turno)
        else:
            self._insertar_recursivo(self.raiz, turno)

    def _insertar_recursivo(self, nodo_actual, turno):
        if turno.hora < nodo_actual.turno.hora:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(turno)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, turno)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(turno)
            else:
                self._insertar_recursivo(nodo_actual.derecha, turno)

    def recorrido_inorden(self, nodo):
            if nodo:
                self.recorrido_inorden(nodo.izquierda)
                print(nodo.turno)
                self.recorrido_inorden(nodo.derecha)
    
    def buscar_por_hora(self, nodo, hora):
        if nodo is None:
            return None
        if str(nodo.turno.hora) == str(hora):
            return nodo.turno
        elif hora < nodo.turno.hora:
            return self.buscar_por_hora(nodo.izquierda, hora)
        else:
            return self.buscar_por_hora(nodo.derecha, hora)
    
    def buscar_por_dni(self, nodo, dni):
        
        if nodo is None:
            return None
        if str(nodo.turno.dni) == str(dni):
            return nodo.turno

        encontrado_izq = self.buscar_por_dni(nodo.izquierda, dni)
        if encontrado_izq:
            return encontrado_izq

        return self.buscar_por_dni(nodo.derecha, dni)
