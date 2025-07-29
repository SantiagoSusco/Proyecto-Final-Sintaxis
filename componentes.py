# componentes.py

# Tokens básicos
ID                  = "id"
PROGRAM             = "program"
VAR                 = "var"
BEGIN               = "begin"
END                 = "end"
IF                  = "if"
THEN                = "then"
ELSE                = "else"
ENDIF               = "endIf"
WHILE               = "while"
DO                  = "do"
ENDWHILE            = "endWhile"
READ                = "read"
REAL                = "real"
STRING              = "string"
WRITE               = "write"
CONST_REAL          = "constReal"
CONST_CADENA        = "constCadena"
PARENTESIS_ABRE     = "parentesisAbre"
PARENTESIS_CIERRA   = "parentesisCierra"
MAS                 = "mas"
MENOS               = "menos"
PRODUCTO            = "producto"
DIVISION            = "division"
PUNTO_Y_COMA        = "puntoYComa"
COMA                = "coma"
PUNTO               = "punto"
DOS_PUNTOS          = "dosPuntos"
OPERADOR_RELACIONAL = "operadorRelacional"
OPERADOR_ASIGNACION = "operadorAsignacion"
AND                 = "and"
OR                  = "or"
NOT                 = "not"
RAIZ                = "raiz"
SUBCADENA           = "subcadena"
BUSCAR              = "buscar"
LONGITUD            = "longitud"
POTENCIA            = "POTENCIA"
# Control
ERROR               = "error"
PESOS               = "pesos"    # fin de archivo

# Diccionario de palabras reservadas
PALABRAS_RESERVADAS = {
    "program": PROGRAM,
    "begin"  : BEGIN,
    "end"    : END,
    "if"     : IF,
    "then"   : THEN,
    "else"   : ELSE,
    "while"  : WHILE,
    "do"     : DO,
    "read"   : READ,
    "write"  : WRITE,
    "var"    : VAR,
    "real"   : REAL,
    "string" : STRING,
    "endif"  : ENDIF,
    "endwhile": ENDWHILE,
    "and"    : AND,
    "or"     : OR,
    "not"    : NOT,
    "raiz"   : RAIZ,
    "subcadena": SUBCADENA,
    "buscar" : BUSCAR,
    "longitud": LONGITUD,
}