import random
random.seed()

# Jogador:

class player:
    def __init__(self, nome, hp, hpMax, forca, habilidade, remedios, pontos):
        self.nome = nome
        self.hp = hp
        self.hpMax = hpMax
        self.forca = forca
        self.habilidade = habilidade
        self.remedios = remedios
        self.pontos = pontos
    
    def __str__(self):
        return f"{self.nome}"

    def status(self):
        print("\nSTATUS")
        print("Nome: %s"%(self.nome))
        print("HP = %d"%(self.hp))
        print("HP Máximo = %d"%(self.hpMax))
        print("Força = %d"%(self.forca))
        print("Habilidade = %d"%(self.habilidade))
        print("Remédios = %d"%(self.remedios))
        print("Pontos = %d"%(self.pontos))
        input("\nEnter para continuar...")

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

esqueleto = inimigo("Esqueleto", 10, 1, 5, True)
fantasma = inimigo("Fantasma", 1, 1, 10, True)