import random


word_list = ['rose','lily' ,'bird' ,'blue','pink','green','white','lotus']
word_to_guess = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 7

display_word = ['_'] * len(word_to_guess)

print("Start Hangman game!")
print("Guess the word one letter at a time. You have 7 incorrect guesses.\n")

while incorrect_guesses < max_incorrect and '_' in display_word:
    print("Word: " + ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single alphabetical letter.\n")
        continue
    if guess in guessed_letters:
        print(" You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(" Correct!\n")

        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f" Incorrect! You have {max_incorrect - incorrect_guesses} guesses left.\n")

if '_' not in display_word:
    print(" Congratulations! You guessed the word:", word_to_guess)
else:
    print(" Game Over! The word was:", word_to_guess)
