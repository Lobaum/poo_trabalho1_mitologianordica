from entidades import Entidade

class Inimigo:
    def __init__(self, poder, defesa, vida_maxima, esquiva, exp_recompensa, dificuldade):
        super().__init__(poder, defesa, vida_maxima, esquiva)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade