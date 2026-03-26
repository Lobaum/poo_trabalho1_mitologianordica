from entidades.jogador import Jogador
from recompensas.tesouros import AltarDeGelo
from entidades.inimigo import spawn_inimigo_por_nivel
from sistema.combate import iniciar_combate
from sistema.dados import rolar_d6
from classe.classe import classes_dados
from raca.raca import racas_dados
import random


def criar_personagem():
    racas_disponiveis = { "1": "Humanos", "2": "Anões do Norte", "3": "Elfos Crepusculares", "4": "Jotunn", "5": "Draugr", "6": "Metamorfo" }
    classes_disponiveis = { "1": "Quebra-Escudos", "2": "Tecelão de Runas", 
                           "3": "Caminhante da Névoa", "4": "Caçador de Feras", "5": "Portador de Presságios", 
                           "6": "Forjador", "7": "Errante", "8": "Guardião", 
                           "9": "Glacial", "10": "Vigia", "11": "Detonador" }

    print("\nBem vindo ao menu de criação de personagem!!")
    input("Pressione Enter para iniciar o jogo: ")

    nome_personagem = input("\nDigite o nome do seu personagem: ")

    print("\nSelecione sua raça")
    print("Raças:\n1) Humanos\n2) Anões do Norte\n3) Elfos Crepusculares\n4) Jotunn\n5) Draugr\n6) Metamorfo")
    escolha_raca = input("Escolha sua Raça: ")

    while (escolha_raca not in racas_disponiveis.keys()):
        print("\nRaça inválida")
        print("Raças:\n1) Humanos\n2) Anões do Norte\n3) Elfos Crepusculares\n4) Jotunn\n5) Draugr\n6) Metamorfo")
        escolha_raca = input("Escolha sua Raça: ")

    print("\nSelecione sua classe")
    print("Vocações:\n1) Quebra-Escudos\n2) Tecelão de Runas\n3) Caminhante da Névoa\n4) Caçador de Feras\n5) Portador de Presságios\n6) Forjador\n7) Errante\n8) Guardião\n9) Glacial\n10) Vigia\n11) Detonador")
    escolha_classe = input("Escolha sua Vocação: ")

    while (escolha_classe not in classes_disponiveis.keys()):
        print("\nClasse inválida")
        print("Vocações:\n1) Quebra-Escudos\n2) Tecelão de Runas\n3) Caminhante da Névoa\n4) Caçador de Feras\n5) Portador de Presságios\n6) Forjador\n7) Errante\n8) Guardião\n9) Glacial\n10) Vigia\n11) Detonador")
        escolha_classe = input("Escolha sua Vocação: ")

    raca_escolhida = racas_dados[racas_disponiveis[escolha_raca]]
    vocacao_escolhida = classes_dados[classes_disponiveis[escolha_classe]]


    vida_calculada = vocacao_escolhida["pv_base"] + raca_escolhida["Bonus_Vida"]

    player = Jogador(
        nome=nome_personagem,
        poder=raca_escolhida["Poder"],      
        defesa=raca_escolhida["Defesa"],    
        vida_maxima=vida_calculada,   
        vida_atual=vida_calculada,   
        esquiva=raca_escolhida["Esquiva"],  
        energia=vocacao_escolhida["pe_por_nivel"],
        energia_maxima=vocacao_escolhida["pe_por_nivel"],
        raca=racas_disponiveis[escolha_raca],
        vocacao=classes_disponiveis[escolha_classe],
        pocao=3,
        exp=0,
        inventario=[]
    )

    return player

player = criar_personagem()
print(f"\n{player.nome} inicia sua jornada em Asgard!")

while player.vida_atual > 0:
    print(f"\n{player.nome}, o que deseja fazer?")
    print("1. Explorar os arredores ")
    print("2. Montar acampamento (Descansar)")
    print("3. Ver Status do Herói")
    
    acao = input("Escolha sua ação: ")
    
    if acao == "1":
        if player.energia <= 0:
            print(f"\n{player.nome}, você precisa descansar para continuar (Energia: {player.energia})")
        else:
            player.energia -= 1
            print("\nVocê caminha com cuidado pela região...")
            d6 = rolar_d6()
            if d6 == 1:
                monstro = spawn_inimigo_por_nivel(player.nivel)
                print(f"De repente, um {monstro.nome} surge das sombras!")
                print(f"Vida: {monstro.vida_atual}/{monstro.vida_maxima}")
                iniciar_combate(player, monstro)
            elif d6 <= 5:
                print("Tudo calmo. Você encontra apenas neve em sua frente e ruínas congeladas.")
            elif d6 == 6:
                print(f"Quando decide entrar em uma ruína congelada em busca de recursos.")
                evento = AltarDeGelo()
                evento.iniciar_evento(player)

    elif acao == "2":
        print("\nVocê monta um pequeno acampamento e descansa perto da fogueira...")
        
        cura_vida = 7
        cura_energia = 3
        player.vida_atual += cura_vida 
        if player.vida_atual > player.vida_maxima:
            player.vida_atual = player.vida_maxima
        player.energia += cura_energia
        if player.energia > player.energia_maxima:
            player.energia = player.energia_maxima

        
        print(f"Você recuperou suas forças!")
        print(f"Status Atual -> Vida: {player.vida_atual}/{player.vida_maxima} | Energia: {player.energia}")
        
    elif acao == "3":
        print(f"""\n{player.nome}, esses são seus status:
Vida: {player.vida_atual}/{player.vida_maxima}
Energia: {player.energia} / {player.energia_maxima}
Poder: {player.poder}
Defesa: {player.defesa}
Esquiva: {player.esquiva}
Raça: {player.raca}
Classe: {player.vocacao}
Poções Disponíveis: {player.pocao}
EXP: {player.exp}
Nível: {player.nivel}""")
        
    else:
        print("\nAção inválida. Escolha 1, 2 ou 3.")