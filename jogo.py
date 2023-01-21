import sys
import personagens as p
import funcoes as f
import fases as fas

def main():
    print("Jogo de aventura baseado em texto\n")
    print("1 - Jogar\n2 - Sair\n")
    opcao = int(input())

    if opcao == 1:
        print("Bem vindo(a) ao jogo!\n")
        
        jogador = p.player("Jogador", 10, 10, 0, 0, 0, 10)
        
        f.atribuirPontos(jogador)

        jogador.status()

        fas.cemiterio(jogador)


    elif opcao == 2:
        sys.exit()

    else:
        print("Inválido.")
        input("Enter para continuar...")

if __name__ == "__main__":
    main()