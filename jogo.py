import sys
import personagens as p
import funcoes as f
import fases

print("Jogo de aventura baseado em texto\n")
print("1 - Jogar\n2 - Sair\n")
opcao = int(input())

if opcao == 1:
    print("Bem vindo(a) ao jogo!\n")
    
    jogador = p.player("", 10, 10, 1, 1, 0, 0 , 10)

    f.criarPersonagem(jogador)
    
    jogador.status()

    fases.cemiterio(jogador)

elif opcao == 2:
    sys.exit()