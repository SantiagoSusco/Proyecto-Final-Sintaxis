# main.py
import io
from Lexer import ObtenerSiguienteCompLex
from componentes import ERROR, PESOS
ruta_archivo=r"C:\Users\santi\OneDrive\Escritorio\santiago\Facultad\Segundo año\Sintaxis y Semantica de los lenguajes\Proyecto Final Sintaxis\Analizador lexico\prueba.txt"
def analizar_fuente(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as Fuente:
        Control = 0
        compLex, lexema, Control = ObtenerSiguienteCompLex(Fuente, Control)
        print(f"{compLex}: '{lexema}'")

        # continúa mientras no sea ERROR ni PESOS
        while compLex not in (ERROR, PESOS):
            compLex, lexema, Control = ObtenerSiguienteCompLex(Fuente, Control)
            print(f"{compLex}: '{lexema}'")


analizar_fuente(ruta_archivo)
