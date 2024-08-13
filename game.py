import random

# As imagens dos gestos
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

def get_choice():
    """Obtém a escolha do jogador e garante que seja válida."""
    while True:
        try:
            choice = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def get_mode():
    """Obtém o modo de jogo do jogador."""
    while True:
        try:
            mode = int(input("Escolha o modo de jogo: 1 para MD3, 2 para MD5, 3 para MD7\n"))
            if mode == 1:
                return 3
            elif mode == 2:
                return 5
            elif mode == 3:
                return 7
            else:
                print("Modo inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def print_stats(victories, draws, losses, total_games):
    """Exibe as estatísticas do jogo."""
    print("\nEstatísticas:")
    print(f"Vitórias: {victories}")
    print(f"Empates: {draws}")
    print(f"Derrotas: {losses}")
    print(f"Total de Jogos: {total_games}")

def play_game():
    """Joga uma partida e retorna o resultado."""
    player_choice = get_choice()
    print(f"\nVocê escolheu:\n{game_image[player_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computador escolheu:\n{game_image[computer_choice]}")

    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        return "win"
    else:
        return "lose"

def main():
    victories = 0
    draws = 0
    losses = 0
    total_games = 0

    mode = get_mode()
    print(f"\nVocê escolheu o modo MD{mode}. Boa sorte!")

    while True:
        result = play_game()
        total_games += 1

        if result == "win":
            victories += 1
            print("Você ganhou!")
        elif result == "draw":
            draws += 1
            print("Empate!")
        else:
            losses += 1
            print("Você perdeu!")

        print_stats(victories, draws, losses, total_games)

        if victories >= mode // 2 + 1 or losses >= mode // 2 + 1:
            print(f"\nVocê {victories > losses and 'venceu' or 'perdeu'} o jogo melhor de {mode}!")
            break
        
        play_again = input("Deseja jogar novamente? (s/n)\n").lower()
        if play_again != 's':
            break

    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()
