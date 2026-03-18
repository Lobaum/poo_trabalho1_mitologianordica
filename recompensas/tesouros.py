import random

class Bau:
    def __init__(self, raridade, dificuldade):
        self.raridade = raridade
        self.dificuldade = dificuldade
        self.tentativas_restantes = 3
        self.esta_aberto = False
        self.foi_trancando = False
        self.tesouros = ["Moedas de Ouro", "Runa de Proteção", "Poção de Hidromel", "Gema da Alma"]

    def tentar_abrir(self, personagem):
        print(f"\nVocê encontrou um Baú {self.raridade} (Dificuldade: {self.dificuldade})")
        
        if self.foi_trancando:
            print("A fechadura está entupida com pedaços de gazuas quebradas. Não abre mais.")
            return

        while self.tentativas_restantes > 0 and not self.esta_aberto:
            print(f"--- Tentativas: {self.tentativas_restantes} ---")
            opcao = input("Pressione [Enter] para usar gazua ou [S] para sair: ").upper()
            
            if opcao == 'S': break

            rolagem = random.randint(1, 20)
            total = rolagem 
            
            print(f"Rolagem: {rolagem} (Total: {total})")

            if total >= self.dificuldade:
                self.esta_aberto = True
                item_ganho = random.choice(self.tesouros)
                print(f"CLACK! O baú abriu! Você encontrou: [{item_ganho}]!")
            else:
                self.tentativas_restantes -= 1
                print("Falha! A gazua entortou.")

        if self.tentativas_restantes <= 0 and not self.esta_aberto:
            self.foi_violado = True
            print("O mecanismo de tranca quebrou permanentemente!")


class AltarDeGelo:
    def __init__(self):
        self.nome = "Altar de Runas Primordiais"
        self.dificuldade = 13
        self.instabilidade = 0
        self.finalizado = False

    def iniciar_evento(self, aventureiro):
        print(f"\nVOCÊ SE APROXIMA DO: {self.nome}")
        print("As runas pulsam. Você pode tentar extrair poder ou recuar.")

        while self.instabilidade < 3 and not self.finalizado:
            print(f"\n[Instabilidade Atual: {self.instabilidade}/3]")
            escolha = input("Deseja: [1] Decifrar Runa | [2] Afastar-se: ")

            if escolha == "2":
                print("Você sentiu o perigo e decidiu recuar.")
                break

            dado = random.randint(1, 20)
            bonus = 4 if aventureiro.classe_nome == "Tecelão de Runas" else 0
            total = dado + bonus

            print(f"Rolagem: {dado} + Bônus: {bonus} = Total: {total}")

            if total >= self.dificuldade:
                print("SUCESSO! Uma aura azul te envolve. (+2 de Poder)")
                aventureiro.poder += 2
                self.finalizado = True
            else:
                self.instabilidade += 1
                print("FALHA! O gelo ao redor do altar começa a rachar...")

        if self.instabilidade >= 3:
            print("\n" + "!" * 40)
            print("O ALTAR EXPLODIU EM ENERGIA SOMBRIA!")
            print("A falha despertou um DRAUGR que estava selado no gelo!")
            print("--- INICIANDO COMBATE ---")
            print("!" * 40)
            self.finalizado = True

