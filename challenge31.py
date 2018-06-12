

if __name__ == '__main__':
    word = 'EVAPORATE'
    word_len = len(word)

    print('Welcome to Hangman!')
    guessed = '_' * word_len
    guessed_print = ' '.join(guessed)
    print(guessed_print)
    inserted = ''


    while guessed != word:
        offset = 0
        letter = input('Guess your letter: ').upper()
        if letter in inserted:
            print('You have already inserted this letter, try other letter!')
            print('Inserted letters: ' + ' '.join(inserted))
            continue
        else:
            inserted += letter

        while letter in word[offset:]:
            letter_ind = word[offset:].index(letter) + offset
            guessed = guessed[:letter_ind] + letter + guessed[letter_ind+1:]
            offset = letter_ind+1

        guessed_print = ' '.join(guessed)
        print('guessed_print = ' + guessed_print)
