
class pessoa():
    def __init__(self, nome):
        self.nome = nome

joao = pessoa("João")

#print(joao.nome)

def funcao(objeto):
    print("Nome é: %s"%(objeto.nome))

funcao(joao)