from entidades.jogador import Jogador
from entidades.inimigo import Inimigo, inimigos
from combate.combate import iniciar_combate

player = Jogador(poder=10, defesa=10, vida_maxima=10, esquiva=2, raca="Humano", vocacao="Guerreiro", energia=10, pocao=3, exp=0)
dados_lobo = inimigos['Fácil']
lobo = Inimigo(
    poder=dados_lobo['Poder'], 
    defesa=dados_lobo['Defesa'], 
    vida_maxima=dados_lobo['Vida'], 
    esquiva=dados_lobo['Esquiva'], 
    energia=dados_lobo['Energia'], 
    exp_recompensa=50, 
    dificuldade="Fácil"
)

iniciar_combate(player, lobo)