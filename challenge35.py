import json
from collections import Counter

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                        'September', 'October', 'November', 'December']

with open('ch34_birthdays.json', 'r') as f:
    info = json.load(f)

# get months numbers 02 06 03...
birthmonths = [info[name][3:5] for name in info.keys()]
print(birthmonths)

# change to February June March...
birthmonths = [months[int(month)-1] for month in birthmonths]
print(birthmonths)

c = dict(Counter(birthmonths))
print(c)
