class Pilha:
    def __init__(self):
        self.pilha = list()
    
    def Inserir(self, elemento):
        self.pilha.append(elemento)
    
    def Retirar(self):
        self.pilha.pop()
    
    def MostrarPilha(self):
        for x in self.pilha:
            print(x)

PILHA = Pilha()
PILHA.Inserir(7)
PILHA.Inserir(True)
PILHA.Inserir("arroz")
PILHA.Retirar()
PILHA.MostrarPilha()


