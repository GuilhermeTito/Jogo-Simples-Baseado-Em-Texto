import random
random.seed()

class player:
    def __init__(self, nome, hp, hpMax, forca, habilidade, dinheiro, remedio, pontos):
        self.nome = nome
        self.hp = hp
        self.hpMax = hpMax
        self.forca = forca
        self.habilidade = habilidade
        self.dinheiro = dinheiro
        self.remedios = remedio
        self.pontos = pontos
    
    def __str__(self):
        return f"{self.nome}"

    def ataque(self):
        if self.habilidade >= random.randint(0,10):
            return self.forca
        else:
            return 0
    
    def status(self):
        print("\nSTATUS")
        print("Nome: %s"%(self.nome))
        print("HP = %d"%(self.hp))
        print("HP Máximo = %d"%(self.hpMax))
        print("Força = %d"%(self.forca))
        print("Habilidade = %d"%(self.habilidade))
        print("Dinheiro = %d"%(self.dinheiro))
        print("Remédios = %d"%(self.remedios))
        print("Pontos = %d\n"%(self.pontos))
    
jogador = player("", 10, 10, 1, 1, 0, 0 , 10)

class inimigo:
    def __init__(self, nome, hp, forca, habilidade):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.habilidade = habilidade
    
    def __str__(self):
        return f"{self.nome}"

    def ataque(self):
        if self.habilidade >= random.randint(0,10):
            return self.forca
        else:
            return 0

esqueleto = inimigo("Esqueleto", 10, 1, 5)
soldado = inimigo("Soldado", 20, 5, 8)