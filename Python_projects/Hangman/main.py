word = "Secret"

allowed_errors = len(word)
guesses = []

done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print("")
    done = True

    guess = in

