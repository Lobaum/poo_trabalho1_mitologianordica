from entidades import Entidade

class Inimigo:
    def __init__(self, poder, defesa, vida_maxima, esquiva, exp_recompensa, dificuldade):
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade