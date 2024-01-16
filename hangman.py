import random
from words import word
import string

def valid_words(words):
    w=random.choice(words)
    while "-" in w or " " in w:
        w=random.choice(words)
    return w.upper()
          


def hangman():
    w=valid_words(word)
    word_letter=set(w)  # set of letters
    alphabet=set(string.ascii_uppercase)
    used_letters=set()  # what user has guessed
    lives=len(w)+2

    while len(word_letter)>0 and lives>0:
        show_words=[letter if letter in used_letters else "_" for letter in w]
        print("Current Word is "," ".join(show_words))
        print("You have got ", lives, "lives and you have used these letters: ", " ".join(used_letters))
        user=input("Please enter your guessed letter: ").upper()        
        if user in alphabet-used_letters:
            used_letters.add(user)
            print("\n")
            if user in word_letter:
               word_letter.remove(user)
            else:
                lives-=1
        elif user in used_letters:
            print("You have already used this letter , input something new !\n")
        else:
            print("Invalid character. Please try again!\n")
    if (lives>0):
        print(f"YAAY!! you WON \n The word was {w}")
    else:
        print(f"Sorry ! Better luck next time.\n The word was {w}")


print(hangman())
