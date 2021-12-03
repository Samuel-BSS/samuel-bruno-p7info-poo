"""
    Módulo cliente -
    Classe Cliente - 
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)
        
"""
from DB import db

from tipocliente  import TipoCliente

class Cliente(db.Model):
    __tablename__ = 'TB_CLIENTE'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    codigo = db.Column(db.Integer, nullable=False)
    cnpjcpf = db.Column(db.String, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    def __init__(self,id, nome, codigo, cnpjcpf, tipo):
        super().__init__(id=id, nome=nome, codigo=codigo, cnpjcpf=cnpjcpf, tipo=tipo)

        
    def str(self):
        string="\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self.tipo, self.cnpjcpf, self.codigo, self.nome, self.id)
        return string
    
if __name__ == '__main__':
    cliente = Cliente(id= 1, nome = "Jose Maria", codigo = 100, cnpjcpf = '200.100.345-34', tipo = 1)
    print(cliente.str())
        
