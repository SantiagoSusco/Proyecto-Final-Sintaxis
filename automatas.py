# automatas.py

from componentes import ID, CONST_REAL, CONST_CADENA, ERROR


def automata_ident(Fuente, Control):
    Fuente.seek(Control)
    c = Fuente.read(1)
    # debe comenzar con letra
    if not c.isalpha():
        return None

    lexema = c
    pos = Control + 1

    Fuente.seek(pos)
    c = Fuente.read(1)
    # acumula letras, dígitos o '_'
    while c.isalnum() or c == "_":
        lexema += c
        pos += 1
        Fuente.seek(pos)
        c = Fuente.read(1)

    return ID, lexema, pos


def automata_const_real(Fuente, Control):
    Fuente.seek(Control)
    c = Fuente.read(1)

    # Debe comenzar con dígito o '-'
    if not c or (not c.isdigit() and c != "-"):
        return None

    lexema = ""
    tiene_punto = False
    error = False
    pos = Control

    # Manejo del signo inicial
    if c == "-":
        lexema += c
        pos += 1
        Fuente.seek(pos)
        c = Fuente.read(1)
        # Tras '-' debe venir un dígito
        if not c or not c.isdigit():
            return None

    # Procesamos el primer dígito
    lexema += c
    pos += 1

    # Bucle principal sin 'break'
    continuar = True
    while continuar:
        Fuente.seek(pos)
        c = Fuente.read(1)

        # Fin de archivo
        if not c:
            continuar = False

        # Modo válido: dígitos o un solo punto
        elif not error:
            if c.isdigit():
                lexema += c
                pos += 1

            elif c == ".":
                if not tiene_punto:
                    tiene_punto = True
                    lexema += c
                    pos += 1
                else:
                    # Segundo punto: activamos modo error
                    error = True
                    lexema += c
                    pos += 1
            else:
                continuar = False

        # Modo error: leemos dígitos o puntos hasta encontrar otro carácter
        else:
            if c.isdigit() or c == ".":
                lexema += c
                pos += 1
            else:
                continuar = False

    # Si terminó con punto suelto, lo marcamos como error
    if not error and lexema.endswith("."):
        error = True

    # Devolvemos el token correspondiente
    if error:
        return ERROR, lexema, pos
    return CONST_REAL, lexema, pos


def automata_const_cadena(Fuente, Control):
    Fuente.seek(Control)
    c = Fuente.read(1)
    # debe comenzar con comilla
    if c != '"':
        return None
    pos = Control + 1
    lexema=""
    Fuente.seek(pos)
    c = Fuente.read(1)
    # lee hasta cierre o EOF
    while c != '"' and c != "\n":
        lexema+= c 
        pos += 1
        Fuente.seek(pos)
        c = Fuente.read(1)

    if c == '"':
        pos += 1
        return CONST_CADENA, lexema, pos

    return ERROR, lexema, pos