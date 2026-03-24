import math

def calcular_exp_necessaria(nivel_atual):
    base_xp = 100
    if nivel_atual == 1:
        return base_xp
    return math.floor(base_xp * (1.4 ** (nivel_atual - 1)))

def evoluir_atributos(jogador):
    jogador.poder = math.floor(jogador.poder * 1.5)
    jogador.defesa = math.floor(jogador.defesa * 1.5)
    jogador.vida_maxima = math.floor(jogador.vida_maxima * 1.5)
    jogador.esquiva = math.floor(jogador.esquiva * 1.5)
    jogador.vida_atual = jogador.vida_maxima
    
    print(f"\nVocê subiu de nível!")
    print(f"Novos Status -> Poder: {jogador.poder} | Vida: {jogador.vida_maxima}")