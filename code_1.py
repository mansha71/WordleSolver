def suggest_word(not_in_word, in_word_wrong_place, correct_word_structure):
    with open('allwords.txt', 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) != 5:
                continue

            # Check for letters not in the word
            if any(letter in not_in_word for letter in word):
                continue

            # Check for correct letter positions
            if any(correct_word_structure[pos] != '_' and correct_word_structure[pos] != word[pos] for pos in range(5)):
                continue

            # Check if the word includes letters known to be in the word but in wrong place
            for letter, positions in in_word_wrong_place.items():
                if letter not in word:
                    break
                if any(word[pos] == letter for pos in positions):
                    break
            else:
                # This word fits all the criteria
                return word  

    return None  # No word found that fits the criteria

# Initialize variables
rounds = 0
results = []
guesses = []
not_in_word = set()
in_word_wrong_place = {}
correct_word_structure = ['_'] * 5

for _ in range(6):
    results.append([0] * 5)
    guesses.append(['_'] * 5)

while rounds < 6:
    guess_word = input("Enter guess: ").lower()
    if len(guess_word) != 5:
        print("Guess must be 5 letters.")
        continue

    for i in range(len(guess_word)):
        guesses[rounds][i] = guess_word[i]

    for i in range(len(guess_word)):
        print(f"{guess_word[i]}?")
        result = int(input("Enter 1 (not in word), 2 (wrong spot), or 3 (correct spot): "))
        results[rounds][i] = result

        if result == 1:
            not_in_word.add(guess_word[i])
        elif result == 2:
            in_word_wrong_place[guess_word[i]] = in_word_wrong_place.get(guess_word[i], set())
            in_word_wrong_place[guess_word[i]].add(i)
        elif result == 3:
            correct_word_structure[i] = guess_word[i]

    suggested_word = suggest_word(not_in_word, in_word_wrong_place, correct_word_structure)
    if suggested_word:
        print(f"Suggested word for next round: {suggested_word}")
    else:
        print("No suitable word found with current constraints.")

    rounds += 1

# After all rounds
print("Game Over")
