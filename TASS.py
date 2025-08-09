import pandas as pd
ARCHIVO_TAS =r"C:\Users\santi\OneDrive\Escritorio\santiago\Facultad\Segundo año\Sintaxis y Semantica de los lenguajes\Proyecto-Final-Sintaxis\TAS.csv"
def cargarTAS():
  
    try:
        # Cargar el archivo CSV con la TAS
        df = pd.read_csv(ARCHIVO_TAS, header=None)
        
        # Extraer componentes léxicos (primera fila, desde la columna 1)
        componente_lexico = df.iloc[0, 1:].tolist()
        
        # Extraer variables (primera columna, desde la fila 1)
        variable = df.iloc[1:, 0].tolist()
        
        # Crear un diccionario de reglas de la TAS
        tas_dict = {}
        
        for var in range(len(variable)):
            for lex in range(1, len(componente_lexico) + 1):
                regla = df.iloc[var + 1, lex]
                
                # Si la celda no está vacía, dividir por comas
                if pd.notna(regla):
                    regla_componentes = regla.split(',')
                else:
                    regla_componentes = []
                
                # Usar tupla (variable, componente_lexico) como clave
                tas_dict[(variable[var], componente_lexico[lex - 1])] = regla_componentes
        
        return tas_dict
        
    except Exception as e:
        print(f"Error al cargar la TAS desde el archivo: {e}")
        return {}