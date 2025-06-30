import random


words = ["apple", "train", "plant", "house", "chair"]
word = random.choice(words)

guessed_letters = []
correct_letters = ['_' for _ in word]
attempts = 6

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# game loop
while attempts > 0 and '_' in correct_letters:
    print("Word:", ' '.join(correct_letters))
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter only a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                correct_letters[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.\n")


if '_' not in correct_letters:
    print(" Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)