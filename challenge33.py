
if __name__ == '__main__':
    birthdays = {
        'Dawid Kopys':'09-02-1995',
        'Magdalena Rozpara':'05-06-1996',
        'Ola Kopys':'28-05-1997'
    }

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for el in birthdays.keys():
        print(el)

    name = input('Who\'s birthday do you want to look up?\n')
    if name in birthdays:
        print('{}\'s birthday is on {}'.format(name, birthdays[name]))
    else:
        print('We don\'t have this name in our database.')
