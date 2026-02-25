class Entidade:
    def __init__(self, poder, defesa, vida_maxima, esquiva):
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva
    
    def to_vivo(self):
        if self.vida_maxima > 0:
            print(f"")


