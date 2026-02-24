class Jogador:
    def __init__(self, poder, defesa, vida_maxima, esquiva, raca, classe):
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva 
        self.nivel = 1
        self.exp = 0
        self.raca = raca
        self.classe = classe
        self.inventario = []