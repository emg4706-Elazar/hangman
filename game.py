import random


def random_word(words_list):
    random_index = random.randint(0,len(words_list)-1)
    secret_word = words_list[random_index]
    return secret_word


def init_game(words_list):
    secret_word = random_word(words_list)
    max_tries = 10
    tries_counter = 0
    word_view = ["*" for i in range(len(secret_word))]    #"-" * len(secret_word)
    run_mode = True
    return secret_word, max_tries, tries_counter, word_view, run_mode


def is_run(status):
    tries_counter = status[2]
    word_view = status[3]
    run_mode = status[-1]
    max_tries = status[1]
    if tries_counter == max_tries or "*" not in word_view:
        run_mode = False
    return run_mode


def print_status(status):
    tries_counter = status[2]
    word_view = status[3]
    max_tries = status[1]
    tries_left = max_tries - tries_counter
    print("="*13,"Status Game","="*13)
    print(f"Guess the word: {word_view}")
    print(f"{tries_left}: tries left!")
    print("="*39)
    print()


def is_only_one_char(char)  -> bool:
    is_one = len(char) == 1
    if not is_one:
        print("Invalid input")
        print("Enter only one letter")
        print()
    return is_one


def is_a_letter(char)   -> bool:
    letter : bool = char.isalpha()
    if not letter:
        print("Invalid input")
        print("Enter only letters")
        print()
    return letter


def input_validation(char)   -> bool:
    valid_input = False
    if is_only_one_char(char) and is_a_letter(char):
        valid_input = True
    return valid_input


def get_input()  -> str:
    valid_input = False
    char = ""
    while not valid_input:
        char = input("Please enter a letter: ")
        valid_input = input_validation(char)
        char.lower()
    return char


def checking_guess(letter, status)  -> bool:
    secret_word = status[0]
    correct_guess = False
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            correct_guess = True
    return correct_guess


def update_status(letter ,status)  -> list:
    word_view = status[3]
    secret_word = status[0]
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            word_view[i] = letter
            status[3] = word_view
    return status


def main(words_list):
    status_game = list(init_game(words_list))

    while is_run(status_game):
        print_status(status_game)
        letter_input = get_input()
        is_correct = checking_guess(letter_input, status_game)
        if is_correct:
            status_game = update_status(letter_input, status_game)
        else:
            tries_counter = status_game[2]
            tries_counter += 1
            status_game[2] = tries_counter
    return



words = [
    "tree",
    "window",
    "computer",
    "river",
    "star",
    "key",
    "claud",
    "book",
    "clock",
    "bridge",
    "coffee",
    "door"
]


if __name__ == "__main__":
    main(words)











