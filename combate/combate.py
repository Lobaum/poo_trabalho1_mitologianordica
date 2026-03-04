from entidades.jogador import Jogador
from entidades.inimigo import Inimigo, inimigos
import random


def iniciar_combate(jogador, inimigo):
    while jogador.vivo() and inimigo.vivo():
        print("Seu turno!")
        print("1. Atacar")
        print("2. Usar Poção")
        print("3. Fugir")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            print("\nVocê atacou o inimigo!")
            jogador.atacar(inimigo)
        elif escolha == "2":
            jogador.usar_pocao()
            if jogador.pocao == 0:
                continue
        elif escolha == "3":
            d20 = random.randint(1, 20)
            print(f"D20 = {d20}")
            if d20 + jogador.esquiva >= 15:
                print(f"Você Fugiu")
                break
            else:
                print(f"Você tentou fugir, mas o inimigo foi mais ligeiro")
        else:
            print("Opção inválida!")
            continue
        if inimigo.vivo():
            print("\nTurno do inimigo!")
            inimigo.atacar(jogador)
    
    if jogador.vivo():
        print("Você venceu o combate!")
        jogador.exp += inimigo.exp_recompensa
        print(f"Você ganhou {inimigo.exp_recompensa} pontos de experiência!")
    else:
        print("Você foi derrotado no combate.")