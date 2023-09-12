import random

def give_instructions():

    print('''\n Wordle is a word guessing game.
        You have 5 attempts
        (C) means the letter is in the word and in the correct position
        (WP) means the letter is in the word but in the wrong position
        (NT) means the letter is not there in the word
          
        Best of luck!''')

words = ["this", "five", "four", "cats", "dogs", "pink", "cats", "hose", "fish", "pant", "cart", "pick", "dart"]

hidden_word = random.choice(words) #chooses a random word from the list variable word
attempt = 5

def check_word(guess):

    if hidden_word == guess:
        print ("Congrats!! You guessed it.")
        return True

    else:
        result = ""
        for i,j in zip(guess, hidden_word):
            # print(i, j) to see what zip function does
            if i == j:
                result = result + "(C)"
            
            elif i in hidden_word:
                result = result + "(WP)"
            
            else:
                result = result + "(NT)"
            
        print(result)
        return False

def main():

    give_instructions()
    attempt = 5
    while attempt > 0:

        guess = input("Enter four letter word: ")
        if check_word(guess) == True:
            break
            
        else:
            attempt -= 1 # attempt = attempt - 1
            print(f"\nYou have {attempt} attempts left\n")

    if attempt == 0:
        print("Better luck next time.")

main()
