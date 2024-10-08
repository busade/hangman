#TODO-1 - Randomly choose a word from the word_list and assign it to a va
# riable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in
#  the chosen_word.
# TODO-4 Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and
#  'display' has no more blanks ("_"). Then you can tell the user they've won.
#TODO-8: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
#TODO-9: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


import random
from hangman_arts import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
display = []


for letter in chosen_word:
    display += "_"

lives = 6
end_of_game = False
while not end_of_game:
    word_lenght = len(chosen_word)
    guess = input("Guess a letter ").lower()


    # to check for the letter
    for position in range(word_lenght):
        alpha = chosen_word[position]
        if guess == alpha:
            display[position]= alpha


    if guess not in chosen_word:
        print (f"You guessed {guess},but it is not in chosen word, therefore you lose a life")
        lives -= 1
    if lives == 0:
        end_of_game = True
        print(f"You lose!, the word is {chosen_word}")


    print(f" {' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(" Weldone !, you win")
    print (stages[lives])