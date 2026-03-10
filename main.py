from entidades.jogador import Jogador
from entidades.inimigo import spawn_inimigo
from combate.combate import iniciar_combate

player = Jogador(poder=100, defesa=10, vida_maxima=10, esquiva=2, raca="Humano", vocacao="Guerreiro", energia=10, pocao=3, exp=0)

adversario = spawn_inimigo(16)

iniciar_combate(player, adversario)