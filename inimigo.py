from entidades import Entidade
import random
class Inimigo(Entidade):
    def __init__(self, poder, defesa, vida_maxima, esquiva, exp_recompensa, dificuldade):
        super().__init__(poder, defesa, vida_maxima, esquiva)
        self.exp_recompensa = exp_recompensa
        self.dificuldade = dificuldade

inimigos = {'id': 1, 'Fácil': {'id': 1, 'Nome': 'Lobo', 'Poder': random.randint(1, 7), 'Defesa': random.randint(5, 10), 'Vida': random.randint(5, 20), 'Esquiva': random.randint(0, 2)} }
print(inimigos)