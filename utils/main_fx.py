from utils.colors_fx import green, blue, red
from constants.constants import especialidades as esp
from constants.constants import especialidades_lista as esp_lst
from utils.fx import parse_input, exit_test, clear, finish_indication, tag_search

def single_loop(tree):
    while True:
        clear()
        print('Por favor seleccione que desea hacer. Ingrese E para salir.')
        print('1. Ver todos los turnos\n2. Buscar por DNI\n3. Buscar por hora')
        
        opt = parse_input(int, '', 'Debe ingresar una opción válida', lambda x: x in [1,2,3])
        
        if exit_test(opt): return

        match opt:
            case 1:
                clear() 
                tree.inorden()
                finish_indication()
            case 2:
                clear()
                dni = parse_input(int, 'Por favor ingrese el DNI: ', '')
                tree.busqueda_dni(dni)
                finish_indication()
            case 3:
                clear()
                hr = parse_input(float, 'Por favor ingrese la hora: ','', lambda x: x >= 0)
                tree.busqueda_hora(hr)
                finish_indication()
        
def all_loop(tree):
    while True:
        clear()
        print('Por favor seleccione que desea hacer. Ingrese E para salir.')
        print('1. Ver todos los turnos\n2. Buscar por DNI y especialidad\n3. Buscar por hora y especialidad')
        opt = parse_input(int, '', 'Debe ingresar una opción válida', lambda x: x in [1,2,3])
        
        if exit_test(opt): return

        match opt:
            case 1:
                clear()
                print('Seleccione una opción')
                print('1. Ver todos los turnos\n2. Filtrar turnos por especialidad\nE. Salir')
                opt1 = parse_input(int,'', 'Debe ingresar una opción válida', lambda x: x in [1,2])
                
                if exit_test(opt1): return

                if opt1 == 2:
                    clear()
                    especialidad = parse_input(str, f'{esp_lst}\nQué especialidad desearía cargar?: ', 'Ingrese una especialidad válida', lambda x: x in esp)
                    if exit_test(especialidad): return
                    tag = tag_search(especialidad)
                    clear()
                    tree.inorden(tag)
                    finish_indication()
                else:
                    clear()
                    tree.inorden()
                    finish_indication()
            case 2:
                clear()
                print('Seleccione una opción')
                print('1. Ver todos los turnos\n2. Filtrar turnos por especialidad\nE. Salir')
                opt1 = parse_input(int,'', 'Debe ingresar una opción válida', lambda x: x in [1,2])
                
                if exit_test(opt1): return

                if opt1 == 2:
                    clear()
                    especialidad = parse_input(str, f'{esp_lst}\nQué especialidad desearía cargar?: ', 'Ingrese una especialidad válida', lambda x: x in esp)
                    if exit_test(especialidad): return
                    tag = tag_search(especialidad)
                    dni = parse_input(str, 'Por favor ingrese el dni a buscar: ')
                    clear()
                    tree.busqueda_dni(dni, tag)
                    finish_indication()
                else:
                    clear()
                    dni = parse_input(str, 'Por favor ingrese el dni a buscar: ')
                    if exit_test(dni): return
                    clear()
                    tree.busqueda_dni(dni)
                    finish_indication()

            case 3:
                clear()
                print('Seleccione una opción')
                print('1. Ver todos los turnos\n2. Filtrar turnos por especialidad\nE. Salir')
                opt2 = parse_input(int,'', 'Debe ingresar una opción válida', lambda x: x in [1,2])
                
                if exit_test(opt2): return

                if opt2 == 2:
                    clear()
                    hora =  parse_input(float, 'Por favor ingrese la hora: ','', lambda x: x >= 0)
                    if exit_test(hora): return
                    especialidad = parse_input(str, f'{esp_lst}\nQué especialidad desearía cargar?: ', 'Ingrese una especialidad válida', lambda x: x in esp)
                    if exit_test(especialidad): return
                    tag = tag_search(especialidad)
                    tree.busqueda_hora(hora, tag)
                    finish_indication()
                else:
                    clear()
                    hora= parse_input(float,'Por favor ingrese la hora: ','', lambda x: x >= 0)
                    if exit_test(hora): return
                    tree.busqueda_hora(hora)
                    finish_indication()
