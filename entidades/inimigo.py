from entidades.entidades import Entidade

import random
class Inimigo(Entidade):
    def __init__(self, poder, defesa, vida_maxima, esquiva, energia, exp_recompensa, dificuldade):
        super().__init__(poder, defesa, vida_maxima, esquiva, energia)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade

inimigos = {'id': 1, 'Fácil': {'Nome': 'Lobo', 'Poder': random.randint(1, 7), 'Defesa': random.randint(5, 10), 'Vida': random.randint(5, 20), 'Esquiva': random.randint(0, 2), 'Energia': random.randint(10, 20)} }