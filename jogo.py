import sys
import personagens as p
import funcoes as f

print("Julgamento por Água\n")
print("1 - Jogar\n2 - Sair\n")
opcao = 1 # int(input())

if opcao == 1:
    print("Bem vindo(a) ao jogo!")
    
    f.criarPersonagem()
    
    p.jogador.status()

    print("\nUm %s se aproxima! Hora de lutar!\n"%(p.esqueleto.nome))
    
    f.batalha()
    f.batalha()
        
elif opcao == 2:
    sys.exit()