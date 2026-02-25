class Entidade:
    def __init__(self, poder, defesa, vida_maxima:int, esquiva):
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva
    
    def to_vivo(self):
        if self.vida_atual > 0:
            print(f"vivo: {self.vida_atual}/{self.vida_maxima}")
        else:
            print(f"morto: {self.vida_atual}/{self.vida_maxima}")

vivo = Entidade(10, 5, 18, 0.2)
vivo.to_vivo()