# %%
from typing import Optional

# %%
class Nodo():
    def __init__(self, id, edad, salario):
        self.id: str = id
        self.edad: int = edad
        self.salario: float = salario
        self.li: Optional['Nodo'] = None

# %%
class LSL3:
    '''Clase que define una Lista Simplemente Ligada
    - Metodo que inicializa la lista
    - insertar: Metodo que inserta un nodo en la lista
    - imprimir: Metodo que imprime el contenido de la lista'''

    # Aca se inicializa el objeto LSL
    def __init__(self):
        self.inicio: Optional[Nodo] = None

    # Aca se inicia el metodo con el que inserta
    def insertar(self, id: str, edad: int, salario: float):
        nuevo_nodo = Nodo(id, edad, salario)

        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            nodo_actual = self.inicio
            while nodo_actual.li:
                nodo_actual = nodo_actual.li
            nodo_actual.li = nuevo_nodo


    # Aca se muestra el metodo que imprime el contenido de la lista
    def imprimir(self):
        nodo_actual = self.inicio
        contador: int = 0
        while nodo_actual:
            print(f'Identificación: {nodo_actual.id} // Edad: {str(nodo_actual.edad)} // Salario: {str(nodo_actual.salario)}')
            nodo_actual = nodo_actual.li
            contador += 1
        print(f'Total de nodos: {contador}')

    # Aca se va a eliminar un nodo
    def eliminar(self, id: str):
        nodo_actual = self.inicio
        if nodo_actual:
            if nodo_actual.id == id:
                self.inicio = nodo_actual.li
                return
            while nodo_actual.li:
                if nodo_actual.li.id == id:
                    nodo_actual.li = nodo_actual.li.li
                    return
                nodo_actual = nodo_actual.li
        print('La lista está vacía, no se puede eliminar el nodo.')

# %%
def main():
    lista = LSL3()
    lista.insertar('1',2,3)
    lista.insertar('4',5,6)
    lista.insertar('7',8,9)
    lista.insertar('10',11,12)
    lista.insertar('13',14,15)
    lista.eliminar('13')
    lista.eliminar('1')
    lista.eliminar('7')
    lista.imprimir()
# %%
if __name__ == '__main__':
    main()