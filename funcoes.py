import personagens as p

def criarPersonagem():
    print("Crie sua personagem para começar.")
    
    p.jogador.nome = input("Digite o nome de sua personagem: ")
    
    print("Você tem %d pontos para distribuir entre forca e habilidade"%(p.jogador.pontos))
    p.jogador.forca = int(input("Pontos de força: "))
    p.jogador.habilidade = int(input("Pontos de habilidade: "))

def batalha():
    
    while 1:
        print("%s. HP = %d. Força = %d. Habilidade = %d"%(p.jogador, p.jogador.hp, p.jogador.forca, p.jogador.habilidade))
        print("%s. HP = %d. Força = %d. Habilidade = %d\n"%(p.esqueleto, p.esqueleto.hp, p.esqueleto.forca, p.esqueleto.habilidade))
        
        dano = p.jogador.ataque()
        
        if dano <= 0:
            print("Você ataca %s. Você erra!"%(p.esqueleto))
        else:
            p.esqueleto.hp -= dano
            print("Você ataca %s. %d de dano!"%(p.esqueleto, dano))
        
        if p.esqueleto.hp <= 0:
            print("Vitória!")
            break
        
        dano = p.esqueleto.ataque()
        
        if dano <= 0:
            print("%s ataca você. Ele erra!"%(p.esqueleto))
        else:
            p.jogador.hp -= dano
            print("%s ataca você. %d de dano!"%(p.esqueleto, dano))
        
        if p.jogador.hp <= 0:
            print("Derrota!")
            break
        
        input("Próximo turno...")