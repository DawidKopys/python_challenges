import random

def gen_4_digit_number():
    return str(random.randint(1000, 9999))

if __name__=="__main__":
    random_number = gen_4_digit_number()
    tries, guessed_number, cows, bulls = 1, 0, 0, 0

    guessed_number = input('Welcome to the Cows and Bulls Game!\nEnter a number:')
    while guessed_number != random_number:
        tries = tries + 1
        for guessed_el, random_el in zip(guessed_number, random_number):
            if guessed_el == random_el:
                cows = cows + 1
            else:
                bulls = bulls + 1
        guessed_number = input(str(cows) + ' cows, ' + str(bulls) + ' bulls\n')
        cows, bulls = 0, 0

    print('You guessed the number! You needed ' + str(tries) + ' attempts.')
