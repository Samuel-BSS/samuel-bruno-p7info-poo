"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor

    def imprimirNotaFiscal(self):       
        def Linha_Pontilhada():
            for x in range(0,112):
                print("-",end="")
                if x == 111:
                    print("-\n",end="")
        
        def Linha_Contínua():
            for x in range(0,112):
                print("_",end="")
                if x == 111:
                    print("_\n",end="")                
        
        def Linha_PontilhadaPersonalizada():
            for x in range(0, 113):
                if x == 112:
                    print("-\n",end="")
                else:
                    if x == 4 or x >= 57 and x <= 61 or x >= 67 and x <=70 or x >=94 and x <= 95:
                        print(" ",end="")
                    else:
                        print("-",end="")

        Linha_Pontilhada()        
        print("NOTA FISCAL {:>101}".format(datetime.datetime.now().strftime("%d/%m/%Y")))
        print("Cliente: {:<10} Nome: {}".format(self._cliente._codigo, self._cliente._nome))
        print(f"CPF/CNPJ: {self._cliente._cnpjcpf}")
        Linha_Pontilhada()
        print("ITENS")
        Linha_Pontilhada()
        print("{:>3} {:>11} {:>50} {:>20} {:^33}".format("Seq","Descricao","QTD","Valor Unit","Preco"))
        Linha_PontilhadaPersonalizada()
        for x in self._itens:
            if len(x._descricao) < 17:
                var_Descricao = x._descricao
                while len(var_Descricao) < 17:
                    var_Descricao = str(var_Descricao) + " "
                print("{:^3} {:>19} {:>42} {:>17} {:>22}\n".format(x._sequencial,var_Descricao,x._quantidade,x._valorUnitario,x._valorItem))
            else:
                print("{:^3} {:>19} {:>42} {:>17} {:>22}".format(x._sequencial,x._descricao,x._quantidade,x._valorUnitario,x._valorItem))
        Linha_Contínua()
