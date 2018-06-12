import json

birthdays = {
    'Dawid Kopys':'09-02-1995',
    'Magdalena Rozpara':'05-06-1996',
    'Ola Kopys':'28-05-1997'
}

with open('ch34_birthdays.json', 'w') as f:
    json.dump(birthdays, f)
