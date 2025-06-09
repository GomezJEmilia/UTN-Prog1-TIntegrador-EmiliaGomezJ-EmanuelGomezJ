from classes.Turno import Turno
from os import system as sys
from utils.colors_fx import red,green,blue,res
from constants.constants import especialidades_dict as esp_dict

def crear_lista_turnos(data, especialidad):
    return [
        Turno(t['dni'], t['nombre'], t['hora']) for t in data if especialidad.lower() == t['especialidad'].lower()
        ]

def clear():
    sys('cls')

def exit_test(var):
    return str(var).lower() == 'e'

def parse_input(pars, frase = '', err = '', condition = lambda x: True):
    while True:
        try:
            var = input(frase)
            var = var.lower()
            if(var == 'e' or var == 'E'):
                return var
            pars_var = pars(var)
            if(condition(pars_var)):
                return pars_var
            else:
                raise ValueError(err)
        except:
            if(err):
                red(err)
                print(chr(27)+"[0m")

def finish_indication():
    blue('\nPulse enter o ingrese cualquier tecla para salir', '')
    parse_input(str)

def tag_search(wrd):
    for k, v in esp_dict.items():
        if wrd in esp_dict[k]:
            tag = k
            return k