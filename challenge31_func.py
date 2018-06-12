
def hangman(word):
    word_len = len(word)

    print('Welcome to Hangman!')
    guessed = '_' * word_len
    guessed_print = ' '.join(guessed)
    print(guessed_print)
    inserted = ''
    guess_limit = 6
    guess_nr = 0

    while guessed != word:
        if guess_nr >= guess_limit:
            print('Sorry, you reached the limit of guesses! You lost :(')
            print('The word you were looking for: ' + word)
            break

        offset = 0
        penalty = 0
        letter = input('Guess your letter: ').upper()
        if letter in inserted:
            print('You have already inserted this letter, try other letter!')
            print('Inserted letters: ' + ' '.join(inserted))
            continue
        else:
            inserted += letter

        if letter in word[offset:]:
            while letter in word[offset:]:
                letter_ind = word[offset:].index(letter) + offset
                guessed = guessed[:letter_ind] + letter + guessed[letter_ind+1:]
                offset = letter_ind+1
        else:
            penalty = 1

        guessed_print = ' '.join(guessed)
        if penalty == 1:
            guess_nr += 1
        print(guessed_print + '\t' 'Number of guesses left: ' + str(guess_limit-guess_nr))

if __name__ == '__main__':
    word = 'EVAPORATE'
    hangman(word)
