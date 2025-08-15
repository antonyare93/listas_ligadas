# %%
class Nodo():
    def __init__(self, valor1, valor2):
        self.dato1 = valor1
        self.dato2 = valor2
        self.siguente = None

# %%
class LSL:
    '''Clase que define una Lista Simplemente Ligada
    - Metodo que inicializa la lista
    - insertar: Metodo que inserta un nodo en la lista
    - mostrar: Metodo que imprime el contenido de la lista'''

    # Aca se inicializa el objeto LSL
    def __init__(self):
        self.inicio = None

    # Aca se inicia el metodo con el que inserta
    def insertar(self, valor1, valor2):
        nuevo_nodo = Nodo(valor1, valor2)

        if not self.inicio:
            self.inicio = nuevo_nodo
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguente:
                nodo_actual = nodo_actual.siguente
            nodo_actual.siguente = nuevo_nodo


    # Aca se muestra el metodo que imprime el contenido de la lista
    def mostrar(self):
        nodo_actual = self.inicio
        while nodo_actual:
            print(f'Dato1: {nodo_actual.dato1} // Dato2: {nodo_actual.dato2}')
            nodo_actual = nodo_actual.siguente

    # Aca se va a eliminar un nodo
    def eliminar(self, valor1, valor2):
        pass
# %%
def main():
    lista = LSL()
    lista.insertar(1,2)
    lista.insertar(3,4)
    lista.insertar(5,6)
    lista.mostrar()
# %% <-- What this? es una funci[on que se asegura que todo se haya
# inicializado antes de empezar el programa
if __name__ == '__main__':
    main()