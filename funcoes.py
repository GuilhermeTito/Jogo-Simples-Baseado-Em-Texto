def atribuirPontos(jogador):
    print("\nVocê tem %d pontos para distribuir entre força e habilidade"%(jogador.pontos))
    while jogador.pontos != 0:
        forca = int(input("Pontos de força: "))
        if forca > jogador.pontos:
            print("Número maior que a quantidade de pontos disponíveis. Digite novamente.\n")
        elif forca == jogador.pontos:
            jogador.forca = forca
            jogador.pontos = 0
            print("Não restaram pontos para distribuir em habilidade.\n")
        else:
            jogador.forca = forca
            jogador.habilidade = jogador.pontos - forca
            jogador.pontos = 0
            print("%d pontos restaram e foram gastos em habilidade.\n"%(jogador.habilidade))

def ataque(atacante, atacado):
    dano = 0
    if atacante.habilidade > atacado.habilidade:
        dano = atacante.forca
    else:
        dano = int(atacante.forca * (atacante.habilidade / atacado.habilidade))
    return dano  

def batalha(jogador, inimigo):
    print("\nUm %s se aproxima! Hora de Lutar!"%(inimigo.nome))

    while 1:
        print("\n%s. HP = %d. Força = %d. Habilidade = %d"%(jogador, jogador.hp, jogador.forca, jogador.habilidade))
        print("%s. HP = %d. Força = %d. Habilidade = %d\n"%(inimigo, inimigo.hp, inimigo.forca, inimigo.habilidade))
        
        op = input("O que fazer?")

        if op == "atacar":

            dano = ataque(jogador, inimigo)
            
            if dano <= 0:
                print("Você ataca %s. Você erra!\n"%(inimigo))
            else:
                inimigo.hp -= dano
                print("Você ataca %s. %d de dano!\n"%(inimigo, dano))

            input("...")
            
            if inimigo.hp <= 0:
                inimigo.estaVivo = False
                print("Você derrotou %s\n"%(inimigo.nome))
                print("Enter para continuar...")
                break
            
            dano = ataque(inimigo, jogador)
            
            if dano <= 0:
                print("%s ataca você. Ele erra!\n"%(inimigo))
            else:
                jogador.hp -= dano
                print("%s ataca você. %d de dano!\n"%(inimigo, dano))

            input("...")
            
            if jogador.hp <= 0:
                print("Derrota!")
                break
        
        elif op == "status":
            jogador.status()
        
        elif op == "remedio":
            if jogador.remedios != 0:
                jogador.hp = jogador.hpMax
                jogador.remedios -= 1
                print("Você usou um remédio e restaurou sua saúde.")
                input("...")
            else:
                print("Você não possui remédios.")
                input("...")
        elif op == "fugir":
            break
        else:
            print("Inválido.")
            input("...")
        input("Próximo turno...\n")