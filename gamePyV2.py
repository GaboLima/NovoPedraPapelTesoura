import random

class JogoPedraPapelTesoura:
    def __init__(self):
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.jogos_totais = 0
        self.modo = 3
        self.imagens_gestos = [
            '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''',
            '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''',
            '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''
        ]

    def obter_escolha_jogador(self):
        """Obtém a escolha do jogador e garante que seja válida."""
        while True:
            try:
                escolha = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
                if escolha in [0, 1, 2]:
                    return escolha
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def obter_modo_jogo(self):
        """Obtém o modo de jogo do jogador."""
        while True:
            try:
                modo = int(input("Escolha o modo de jogo: 1 para MD3, 2 para MD5, 3 para MD7\n"))
                if modo in [1, 2, 3]:
                    self.modo = modo * 2 + 1
                    return
                else:
                    print("Modo inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def exibir_estatisticas(self):
        """Exibe as estatísticas do jogo."""
        print("\nEstatísticas:")
        print(f"Vitórias: {self.vitorias}")
        print(f"Empates: {self.empates}")
        print(f"Derrotas: {self.derrotas}")
        print(f"Total de Jogos: {self.jogos_totais}")

    def jogar_partida(self):
        """Joga uma partida e retorna o resultado."""
        escolha_jogador = self.obter_escolha_jogador()
        print(f"\nVocê escolheu:\n{self.imagens_gestos[escolha_jogador]}")

        escolha_computador = random.randint(0, 2)
        print(f"Computador escolheu:\n{self.imagens_gestos[escolha_computador]}")

        if escolha_jogador == escolha_computador:
            return "empate"
        elif (escolha_jogador == 0 and escolha_computador == 2) or \
             (escolha_jogador == 1 and escolha_computador == 0) or \
             (escolha_jogador == 2 and escolha_computador == 1):
            return "vitoria"
        else:
            return "derrota"

    def jogar(self):
        """Inicia o jogo."""
        self.obter_modo_jogo()
        print(f"\nVocê escolheu o modo MD{self.modo}. Boa sorte!")

        while True:
            resultado = self.jogar_partida()
            self.jogos_totais += 1

            if resultado == "vitoria":
                self.vitorias += 1
                print("Você ganhou!")
            elif resultado == "empate":
                self.empates += 1
                print("Empate!")
            else:
                self.derrotas += 1
                print("Você perdeu!")

            self.exibir_estatisticas()

            if self.vitorias >= self.modo // 2 + 1 or self.derrotas >= self.modo // 2 + 1:
                print(f"\nVocê {self.vitorias > self.derrotas and 'venceu' or 'perdeu'} o jogo melhor de {self.modo}!")
                break

            jogar_novamente = input("Deseja jogar novamente? (s/n)\n").lower()
            if jogar_novamente != 's':
                break

        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogo = JogoPedraPapelTesoura()
    jogo.jogar()
