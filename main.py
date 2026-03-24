from entidades.jogador import Jogador
from entidades.inimigo import spawn_inimigo
from combate.combate import iniciar_combate
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
    energia_calculada = vocacao_escolhida["pe_por_nivel"]

    player = Jogador(
        nome=nome_personagem,
        poder=raca_escolhida["Poder"],      
        defesa=raca_escolhida["Defesa"],    
        vida_maxima=vida_calculada,      
        esquiva=raca_escolhida["Esquiva"],  
        energia=energia_calculada,       
        raca=racas_disponiveis[escolha_raca],
        vocacao=classes_disponiveis[escolha_classe],
        pocao=3,
        exp=0
    )

    return player

player = criar_personagem()
print(f"\n{player.nome} inicia sua jornada em Eldoria!")

while player.vida_maxima > 0:
    print(f"\n{player.nome}, o que deseja fazer?")
    print("1. Explorar os arredores ")
    print("2. Montar acampamento (Descansar)")
    print("3. Ver Status do Herói")
    
    acao = input("Escolha sua ação: ")
    
    if acao == "1":
        print("\nVocê caminha com cuidado pela região...")
        chance = random.randint(1, 2)
        if chance == 1:
            print("De repente, um inimigo surge das sombras!")
            monstro = spawn_inimigo(21)
            iniciar_combate(player, monstro)
        else:
            print("Tudo calmo. Você encontra apenas folhas secas e silêncio.")
        
    elif acao == "2":
        print("\nVocê descansa perto da fogueira...")
        
    elif acao == "3":
        print(f"""\n{player.nome}, esses são seus status:
Vida: {player.vida_maxima}
Energia: {player.energia}
Poder: {player.poder}
Defesa: {player.defesa}
Esquiva: {player.esquiva}
Raça: {player.raca}
Classe: {player.vocacao}
Poções Disponíveis: {player.pocao}
EXP: {player.exp}""")
        
    else:
        print("\nAção inválida. Escolha 1, 2 ou 3.")