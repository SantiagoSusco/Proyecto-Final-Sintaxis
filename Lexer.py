# lexer_pascal.py

from componentes import *
from automatas import automata_ident, automata_const_real, automata_const_cadena

SIMBOLOS = {
    ":=": OPERADOR_ASIGNACION,
    "<=": MENOR_IGUAL, ">=": MAYOR_IGUAL,
    "==": IGUAL, "!=": DISTINTO,
    "(" : PARENTESIS_ABRE, ")" : PARENTESIS_CIERRA,
    "+" : MAS,          "-" : MENOS,
    "*" : PRODUCTO,     "/" : DIVISION,
    ";" : PUNTO_Y_COMA, "," : COMA,
    "." : PUNTO,        "<" : MENOR,
    ">" : MAYOR, "^" : POTENCIA,":": DOS_PUNTOS,"&":CONCATENAR,"=": IGUAL_SIMPLE
}


def ObtenerSiguienteCompLex(Fuente, Control):
    Fuente.seek(Control)
    c = Fuente.read(1)
    # omite espacios en blanco
    while c.isspace():
        Control += 1
        Fuente.seek(Control)
        c = Fuente.read(1)

    if c == "":
        return PESOS, "", Control

    # 1) identificador
    res = automata_ident(Fuente, Control)
    if res:
        token, lexema, nueva_pos = res

        # si es palabra reservada, devolvemos su token
        token_final = PALABRAS_RESERVADAS.get(lexema.lower(), token)
        return token_final, lexema, nueva_pos


    # 2) constante real
    res = automata_const_real(Fuente, Control)
    if res:
        return res

    # 3) constante cadena
    res = automata_const_cadena(Fuente, Control)
    if res:
        return res

    # 4) símbolos de uno o dos caracteres
    Fuente.seek(Control)
    dos = Fuente.read(2)
    if dos in SIMBOLOS:
        return SIMBOLOS[dos], dos, Control + 2

    Fuente.seek(Control)
    uno = Fuente.read(1)
    if uno in SIMBOLOS:
        return SIMBOLOS[uno], uno, Control + 1

    # 5) nada reconocido
    return ERROR, uno, Control + 1