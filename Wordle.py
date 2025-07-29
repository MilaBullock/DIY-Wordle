def good_word(word:str , length: int):
    """
    Checks if the word is a valid English word.
    """
    if len(word) != length:
        print(f"Please enter a word of length {length}.")
        return False
    else:
        for char in word:
            if not char.isalpha():
                return False
        return True


def new_round():
    """
    Starts a new round of the game with the given answer
    """
    answer = input("Do you want to play another round? (yes/no)").strip().lower()
    if answer == "yes":
        return getting_word()
    else:
        print("Thanks for playing!")
    
def find_match(guess:str, given_word:str):
    """
    Checks guess and given for matches returns emojis based on match
    
    in word = yellow
    right spot = green
    not in word = black
    """

  
    hint = [""] * len(given_word)
    given_word_chars = list(given_word)
    
    # First pass: mark correct positions (green)

    for i in range(len(given_word)):
        if guess[i] == given_word[i]:
            hint[i] = "🟩"
            given_word_chars[i] = "used"  # Mark as used
    
    # Second pass: mark letters in wrong positions (yellow) or not in word (black)

    for i in range(len(given_word)):
        if hint[i] == "":  
            if guess[i] in given_word_chars:
                hint[i] = "🟨"
            else:
                hint[i] = "⬛"
    
    print("".join(hint))

def getting_word():
    """
    Gets a random word of a given length from the English words set
    """
    import random
    from english_words import get_english_words_set
  
    # getting the random word and length from the user
    print("Welcome to Wordle! \nYou have 5 attempts to guess the word.\nDont use any special characters or numbers.")
    print("----------------------------------")
    length = int(input("Enter the length of the word you want: "))
    
    words = get_english_words_set(['web2'], lower=True, alpha=True)
    given_word = random.choice([word for word in words if len(word) == length])
    
    #starting the 5 rounds of the game
    attempts = 0
    while attempts < 5:
        guess= input("Enter your guess:")
        guess = guess.lower()

        # checks if guess is valid and then finds matches
        if good_word(guess, length) == True:
            attempts += 1
            if guess == given_word:
                print ("Congratulations! You've guessed the word!")
                return new_round()
            else:
                find_match(guess, given_word)
    
    print(f"The word was: {given_word}")
    
    return new_round()

def main():
    print(getting_word())
    
    
if __name__ == "__main__":
    main()
   
