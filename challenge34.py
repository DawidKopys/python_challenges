import json

with open('ch34_birthdays.json', 'r') as f:
    info = json.load(f)

print('Welcome to the birthday dictionary. We know the birthdays of:')
for el in info.keys():
    print(el)

name = input('Who\'s birthday do you want to look up?\n')
if name in info:
    print('{}\'s birthday is on {}'.format(name, info[name]))
else:
    print('We don\'t have this name in our database.')
