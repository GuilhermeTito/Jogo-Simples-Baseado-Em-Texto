import random
random.seed()

# Jogador:

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
        print("Pontos = %d"%(self.pontos))

# NPCs

class inimigo:
    def __init__(self, nome, hp, forca, habilidade, estaVivo):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.habilidade = habilidade
        self.estaVivo = estaVivo
    
    def __str__(self):
        return f"{self.nome}"

    def ataque(self):
        if self.habilidade >= random.randint(0,10):
            return self.forca
        else:
            return 0

esqueleto = inimigo("Esqueleto", 10, 1, 5, True)
soldado = inimigo("Soldado", 20, 5, 8, True)