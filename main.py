from utils.colors_fx import green, blue, red
from utils.fx import parse_input, exit_test, clear, finish_indication, tag_search
from handler.Agenda_handler import Agenda_handler as ag
from constants.constants import especialidades as esp
from utils.main_fx import single_loop, all_loop




def main_loop():
    green('¡BIENVENID@ AL GESTOR DE TURNOS!')
    print('Para comenzar por favor seleccione una opción:')
    print('1. Montar todos los turnos en todas las agendas\n2. Montar solo la agenda de una especialidad específica')
    blue('Ingrese E para salir')
    opt = parse_input(int, '','Debe ingresar una opción válida', lambda x: x in [1,2])
    if exit_test(opt):
        clear() 
        blue('Gracias por utilizar nuestro software')
        finish_indication()
        return
    tree = None
    if opt == 1:
        tree = ag('todo')
    else:
        especialidad = parse_input(str, 'Qué especialidad desearía cargar?: ', 'Debe ingresar una especialidad válida', lambda x: x in esp)
        if exit_test(especialidad): return
        tag = tag_search(especialidad)
        tree = ag('esp', tag)
    match opt:
        case 1:
            clear()
            all_loop(tree)
        case 2:
            clear()
            single_loop(tree) 

main_loop()