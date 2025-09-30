import random

def load_words():
    """Carrega palavras do arquivo words.txt"""
    with open("words.txt", "r", encoding="utf-8") as f:
        return [w.strip() for w in f.readlines()]

def choose_word(words):
    """Escolhe uma palavra aleatória"""
    return random.choice(words)

def play_game():
    words = load_words()
    secret_word = choose_word(words).upper()
    guessed_letters = []
    attempts = 6

    print("🎮 Bem-vindo ao Jogo da Forca!")
    print(f"A palavra tem {len(secret_word)} letras.\n")

    while attempts > 0:
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Palavra:", " ".join(display_word))
        print(f"Tentativas restantes: {attempts}")

        guess = input("Digite uma letra: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Digite apenas UMA letra válida!\n")
            continue

        if guess in guessed_letters:
            print("Você já tentou essa letra!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Boa! A letra {guess} está na palavra.\n")
        else:
            attempts -= 1
            print(f"A letra {guess} não está na palavra.\n")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"🎉 Parabéns! Você adivinhou a palavra: {secret_word}")
            break
    else:
        print(f"😢 Você perdeu! A palavra era: {secret_word}")

if __name__ == "__main__":
    play_game()
