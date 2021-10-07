class Fila:
    def __init__(self):
        self.fila = list()

    def Inserir(self,elemento):
        self.fila.append(elemento)

    def Retirar(self):      
        self.fila.reverse()      
        self.fila.pop()
        self.fila.reverse()

    def MostrarFila(self):
        for x in self.fila:
            print(x)

FILA = Fila()
FILA.Inserir("CARRO")
FILA.Inserir("AVIAO")
FILA.Inserir("MOTO") 
FILA.Retirar()
FILA.MostrarFila()