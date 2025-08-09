class Nodo:

    def __init__(self, dato):   # Nodo() dato por defecto es "", Nodo(dato) dato debe ser str
        self.dato = dato
        self.hijos = []
        self.padre = None

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

            # Devuelve True si el nodo es una hoja, False si no lo es
    def esHoja(self):
        return not self.hijos

    # Devuuelve True si el nodo es la raiz, False si no lo es
    def esRaiz(self):
        return self.padre is None

           
            # Devuelve su  Nodo padre.
    def Padre(self):
        return self.padre

            # Devuelve un array con todos los hijos del nodo
    def Hijos(self):
        return self.hijos
    
    def Raiz(self):
        nodo_actual = self
        while nodo_actual.padre is not None:
            nodo_actual = nodo_actual.padre
        return nodo_actual

            # Devuelve el dato del nodo en crudo
    def dato(self):
        return f"{self.dato}"