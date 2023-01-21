import personagens as p
import funcoes as f

def cemiterio(jogador):
    print("Você anda pelo cemitério em busca de um tesouro escondido na casa do coveiro.")
    
    print("\nOs mortos se levantam!")
    
    esqueleto1 = p.inimigo("Esqueleto", 3, 1, 5, True)
    esqueleto2 = p.inimigo("Esqueleto", 3, 1, 5, True)

    f.batalha(jogador, esqueleto1)
    if esqueleto1.estaVivo == False:
        f.batalha(jogador, esqueleto2)