def atribuirPontos(jogador):
    print("\nVocê tem %d pontos para distribuir entre forca e habilidade"%(jogador.pontos))
    jogador.forca = int(input("Pontos de força: "))
    jogador.habilidade = int(input("Pontos de habilidade: "))

def criarPersonagem(jogador):
    print("Crie sua personagem para começar.\n")
    
    jogador.nome = input("Digite o nome de sua personagem: ")
    
    atribuirPontos(jogador)

def batalha(jogador, inimigo):
    print("Um %s se aproxima! Hora de Lutar!\n"%(inimigo.nome))

    while 1:
        print("%s. HP = %d. Força = %d. Habilidade = %d"%(jogador, jogador.hp, jogador.forca, jogador.habilidade))
        print("%s. HP = %d. Força = %d. Habilidade = %d\n"%(inimigo, inimigo.hp, inimigo.forca, inimigo.habilidade))
        
        dano = jogador.ataque()
        
        if dano <= 0:
            print("Você ataca %s. Você erra!\n"%(inimigo))
        else:
            inimigo.hp -= dano
            print("Você ataca %s. %d de dano!\n"%(inimigo, dano))
        
        if inimigo.hp <= 0:
            inimigo.estaVivo = False
            print("Você derrotou %s\n"%(inimigo.nome))
            break
        
        dano = inimigo.ataque()
        
        if dano <= 0:
            print("%s ataca você. Ele erra!\n"%(inimigo))
        else:
            jogador.hp -= dano
            print("%s ataca você. %d de dano!\n"%(inimigo, dano))
        
        if jogador.hp <= 0:
            print("Derrota!")
            break
        
        input("Próximo turno...\n")