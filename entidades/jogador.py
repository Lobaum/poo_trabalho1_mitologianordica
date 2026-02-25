from entidades import Entidade

class Jogador(Entidade):
    def __init__(self, poder, defesa, vida_maxima, esquiva, raca, classe):
        super().__init__(poder, defesa, vida_maxima, esquiva)
        self.raca = raca
        self.classe = classe

