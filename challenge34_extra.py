import json

with open('ch34_birthdays.json', 'r') as f:
    info = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of:')
for el in info.keys():
    print(el)

name = input('Who\'s birthday do you want add to our database?\n')
if name in info:
    print('{}\'s birthday is already in the database ({})!'.format(name, info[name]))
else:
    birthdate = input('When was the person born? format: dd-mm-yyyy\n')
    info[name] = birthdate
    with open('ch34_birthdays.json', 'w') as f:
        json.dump(info, f)
    print('{} was added to my birthday list ({}).\n'.format(name, info[name]))
