# Clase que representa un turno médico
class Turno:
    def __init__(self, dni, nombre, prioridad, hora):
        self.dni = dni
        self.nombre = nombre
        self.prioridad = prioridad
        self.hora = hora  # ejemplo: 9.30, 10.15

    def __str__(self):
        return f"{self.hora}hs - {self.nombre} (DNI: {self.dni}, Prioridad: {self.prioridad})"

# Nodo del árbol binario
class Nodo:
    def __init__(self, turno):
        self.turno = turno
        self.izquierda = None
        self.derecha = None

# Árbol binario de turnos, ordenado por hora
class ArbolTurnos:
    def __init__(self):
        self.raiz = None

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

    # Recorrido inorden: muestra los turnos ordenados por hora
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.turno)
            self.recorrido_inorden(nodo.derecha)
    
    # Búsqueda de turno por hora
    def buscar_por_hora(self, nodo, hora):
        if nodo is None:
            return None
        if nodo.turno.hora == hora:
            return nodo.turno
        elif hora < nodo.turno.hora:
            return self.buscar_por_hora(nodo.izquierda, hora)
        else:
            return self.buscar_por_hora(nodo.derecha, hora)
    
    # Búsqueda de turno por DNI
    def buscar_por_dni(self, nodo, dni):
        if nodo is None:
            return None

        if nodo.turno.dni == dni:
            return nodo.turno

        # Buscar en subárbol izquierdo
        encontrado_izq = self.buscar_por_dni(nodo.izquierda, dni)
        if encontrado_izq:
            return encontrado_izq

        # Buscar en subárbol derecho
        return self.buscar_por_dni(nodo.derecha, dni)


# Función para crear el árbol a partir de una lista de turnos
def crear_arbol_turnos(lista_turnos):
    arbol = ArbolTurnos()
    for turno in lista_turnos:
        arbol.insertar(turno)
    return arbol


# Creamos lista con turnos
turnos = [
    Turno(43153023, "Emilia Gómez Juárez", 2, 9.30),
    Turno(28900444, "Carlos Pérez", 4, 10.15),
    Turno(39082786, "Emanuel Gómez", 1, 8.45),
    Turno(30111222, "Marcos Díaz", 3, 11.00),
    Turno(28888333, "Sofía Torres", 5, 9.00),
]

# Creamos el arbol a partir de la lista de turnos
arbol = crear_arbol_turnos(turnos)

# Mostrar los turnos en orden de atención (por hora)
print("Turnos ordenados por horario (inorden):\n")
arbol.recorrido_inorden(arbol.raiz)

# Búsqueda de turno por DNI
dni_a_buscar = 28888322
turno_encontrado_dni = arbol.buscar_por_dni(arbol.raiz, dni_a_buscar)

if turno_encontrado_dni:
    print("Turno encontrado:")
    print(turno_encontrado_dni)
else:
    print("No se encontró ningún turno con ese DNI.")

# Búsqueda de turno por hora
hora_a_buscar = 12.00
turno_entontrado_hora = arbol.buscar_por_hora(arbol.raiz, hora_a_buscar)

if turno_entontrado_hora:
    print("Turno encontrado:")
    print(turno_entontrado_hora)
else:
    print("No se encontró ningún turno en ese horario.")