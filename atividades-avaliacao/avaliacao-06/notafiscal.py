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
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal
from DB import db
import datetime


class NotaFiscal(db.Model):
    __tablename__ = 'TB_NOTA_FISCAL'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    clienteID = db.Column(db.Integer, db.ForeignKey("TB_CLIENTE.id"), nullable=False)
    data = db.Column(db.String, nullable=False)
    itens = db.relationship("ItemNotaFiscal", backref="NotaFiscal", lazy=True)

    def __init__(self, id, codigo, clienteID):
        super().__init__(id=id, codigo=codigo, clienteID=clienteID, data=datetime.datetime.now().strftime("%d-%m-%Y"))
        
    def calcularNotaFiscal(self):
        itens = ItemNotaFiscal.query.filter_by(id=self.id)
        valor = 0.0
        for item in itens:
            valor = valor + item.valorItem
        self.valorNota = valor

    def getCliente(self):
        clientePesquisa = Cliente.query.filter_by(id=self.clienteID)
        cliente = dict()
        cliente["nome"] = clientePesquisa[0].nome
        cliente["codigo"] = clientePesquisa[0].codigo
        cliente["cnpjcpf"] = clientePesquisa[0].cnpjcpf
        return cliente

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
        print("Cliente: {:<10} Nome: {}".format(self.getCliente()["codigo"], self.getCliente()["nome"]))
        print("CPF/CNPJ:  {}".format(self.getCliente()["cnpjcpf"]))
        Linha_Pontilhada()
        print("ITENS")
        Linha_Pontilhada()
        print("{:>3} {:>11} {:>50} {:>20} {:^33}".format("Seq","Descricao","QTD","Valor Unit","Preco"))
        Linha_PontilhadaPersonalizada()
        for x in self.itens:
            if len(x.descricao) < 17:
                var_Descricao = x.descricao
                while len(var_Descricao) < 17:
                    var_Descricao = str(var_Descricao) + " "
                print("{:^3} {:>19} {:>42} {:>17} {:>22}\n".format(x.sequencial,var_Descricao,x.quantidade,x.valorUnitario,x.valorItem))
            else:
                print("{:^3} {:>19} {:>42} {:>17} {:>22}".format(x.sequencial,x.descricao,x.quantidade,x.valorUnitario,x.valorItem))
        Linha_Contínua()
