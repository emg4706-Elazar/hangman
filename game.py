# https://github.com/emg4706-Elazar/hangman.git
import random


def random_word(words_list):
    random_index = random.randint(0,len(words_list)-1)
    secret_word = words_list[random_index]
    return secret_word


def init_game(words_list):
    secret_word = random_word(words_list)

    max_tries = 10
    tries_counter = 0
    word_view = ["*" for i in range(len(secret_word))]
    typing_history = []
    run_mode = True
    return secret_word, max_tries, tries_counter, word_view, run_mode, typing_history


def is_run(status)  -> bool:
    tries_counter = status[2]
    word_view = status[3]
    run_mode = status[4]
    max_tries = status[1]
    if tries_counter == max_tries or "*" not in word_view:
        run_mode = False
    return run_mode


def print_history(status):
    typing_history = status[5]
    print("Typing_History:",end="")
    for letter in typing_history:
        print(letter,end=" ")
    print()


def print_status(status):
    tries_counter = status[2]
    word_view = status[3]
    max_tries = status[1]
    tries_left = max_tries - tries_counter
    print("="*13,"Status Game","="*13)
    print(f"Guess the word: {word_view}")
    print(f"{tries_left}: tries left!")
    print_history(status)
    print("="*39,"\n")


def is_only_one_char(char)  -> bool:
    is_one = len(char) == 1
    if not is_one:
        print("Invalid input")
        print("Enter only one letter\n")
    return is_one


def is_a_letter(char)   -> bool:
    letter : bool = char.isalpha()
    if not letter:
        print("Invalid input")
        print("Enter only letters\n")
    return letter


def is_typed(letter, status)  -> bool:
    typing_history = status[5]
    typed = letter in typing_history
    if typed:
        print("This letter is already typed")
        print("Enter a new letter!\n")
    return typed


def input_validation(char, status)   -> bool:
    valid_input = False
    if is_only_one_char(char) and is_a_letter(char) and not is_typed(char, status):
        valid_input = True
    return valid_input


def get_input(status)  -> str:
    valid_input = False
    char = ""
    while not valid_input:
        char = input("Please enter a letter: ").lower()
        valid_input = input_validation(char, status)
    return char


def append_to_history(letter, status)  -> list:
    status[5].append(letter)
    return status


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


def game_loop(status)  ->list:
    status = list(status)
    while is_run(status):
        print_status(status)
        letter_input = get_input(status)
        status = append_to_history(letter_input, status)
        is_correct = checking_guess(letter_input, status)
        if is_correct:
            status = update_status(letter_input, status)
            print("Correct Guess\n")
        else:
            tries_counter = status[2]
            tries_counter += 1
            status[2] = tries_counter
            print("Wrong Guess\n")
    return status


def is_win(status)  -> bool:
    word_view = status[3]
    win = False
    if "*" not in word_view:
        win = True
    return win


WORDS = [
    "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave",
    "smart", "strong", "clean", "dirty", "small",
    "large", "short", "long", "early", "late",
    "green", "yellow", "purple", "black", "white",
    "silver", "gold", "brown", "pink", "blue",
    "summer", "winter", "spring", "autumn", "season",
    "morning", "night", "today", "tomorrow", "yesterday",
    "family", "father", "mother", "brother", "sister",
    "friend", "people", "child", "baby", "woman",
    "man", "doctor", "driver", "soldier", "police",
    "engineer", "artist", "farmer", "chef", "pilot",
    "city", "village", "street", "bridge", "garden",
    "market", "store", "hotel", "airport", "station",
    "travel", "ticket", "train", "plane", "bottle",
    "camera", "picture", "letter", "number", "answer",
    "question", "game", "winner", "player", "score",
    "level", "start", "finish", "secret", "danger",
    "dream", "story", "movie", "book", "lesson",
    "language", "english", "hebrew", "word", "sentence",
    "voice", "sound", "light", "shadow", "fire",
    "earth", "stone", "metal", "wood", "glass",
    "cloud", "rain", "storm", "snow", "wind",
    "heart", "brain", "hand", "finger", "shoulder",
    "body", "face", "mouth", "tooth", "eye",
    "jump", "run", "walk", "swim", "drive",
    "write", "read", "speak", "listen", "learn",
    "build", "break", "open", "close", "catch",
    "throw", "bring", "carry", "choose", "change",
    "create", "delete", "search", "print", "input",
    "output", "random", "python", "function", "variable",
    "loop", "condition", "string", "list", "index",
    "error", "program", "project", "folder", "file"
]



if __name__ == "__main__":
    new_status_game = init_game(WORDS)
    final_status = game_loop(new_status_game)
    if is_win(final_status):
        print("Congratulations! You guessed the word correctly!")
    else:
        sec_word = final_status[0]
        print(f"Game Over! The correct word was: {sec_word}")











