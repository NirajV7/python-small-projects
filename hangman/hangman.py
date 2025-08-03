import random
import words
import hangman_art

print("Welcome to Hangman!")
lives = 6  # Starting with 6 lives
game_over = False
chosen_word = random.choice(words.word_list)

# Initialize display with underscores
display = ["_" for _ in chosen_word]

# Print initial state
print(hangman_art.stages[lives])
print(f"Word to guess: {' '.join(display)}")

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:
        # Check each position in the word
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Letter '{guess}' is not in the word. You lose a life!")
    
    # Print current state
    print(hangman_art.stages[lives])
    print(f"Word: {' '.join(display)}")
    print(f"Lives remaining: {lives}")
    
    # Check if player has won
    if "_" not in display:
        game_over = True
        print("Congratulations! You win! 🎉")
        print(f"The word was: {chosen_word}")
    
    # Check if player has lost
    if lives <= 0:
        game_over = True
        print("Game Over! You lose! 💀")
        print(f"The word was: {chosen_word}")