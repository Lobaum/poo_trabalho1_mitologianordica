class Raca:
    def __init__(self, nome, bonus_status):
        self.nome = nome
        self.bonus_status = bonus_status

humanos = Raca("Humanos", "+1 em qualquer atributo")
anoes = Raca("Anões do Norte", "Constituição +2, Força +1, Carisma -1")
elfos = Raca("Elfos Crepusculares", "Destreza +2, Inteligência +1, Constituição -1")
jotunn = Raca("Jotunn", "Força +2, Constituição +1, Destreza -1")
draugr = Raca("Draugr", "Constituição +2, Sabedoria +1, Carisma -2")
metamorfo = Raca("Metamorfo", "Força +1, Destreza +1")