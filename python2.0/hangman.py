from hangman_words import word_list
from hangman_art import stages,logo
import random

# Initialize the number of lives
lives = 6

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)

# Display tha game logo
print(logo)
# Create a display list with blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")
    
    
# initialize the end_of_game flag  
end_of_game = False
   
# Game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    # Check each letter in the chose_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # If the gussed letter is not in the chosen_word refuse lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You gusses {guess}, that's not in the word you lose a life")
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    # Print the updated display
    print(f"{" ".join(display)}")
    
    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You Win")
    # Print the current stage of tha hangma
    print(stages[lives])
