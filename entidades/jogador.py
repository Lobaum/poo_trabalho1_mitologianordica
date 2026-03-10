from entidades.entidades import Entidade

class Jogador(Entidade):
    def __init__(self, poder, defesa, vida_maxima, esquiva, energia, exp, raca, vocacao, pocao, nome):
        super().__init__(poder, defesa, vida_maxima, esquiva, energia)
        self.raca = raca
        self.vocacao = vocacao
        self.pocao = pocao
        self.exp = exp
        self.nome = nome


    def usar_pocao(self):
        if self.pocao > 0:
            self.vida_atual = min((self.vida_maxima // 2) + self.vida_atual, self.vida_maxima)
            self.pocao -= 1
            print(f"Você usou uma poção! Vida atual: {self.vida_atual}, Poções restantes: {self.pocao}")
        else:
            print("Você não tem poções para usar!")