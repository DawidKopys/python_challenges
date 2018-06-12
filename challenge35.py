import json
from collections import Counter

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                        'September', 'October', 'November', 'December']

def get_months_count(json_file_name):
    with open(json_file_name, 'r') as f:
        info = json.load(f)

    # get months numbers 02 06 03...
    birthmonths = [info[name][3:5] for name in info.keys()]

    # change to February June March...
    birthmonths = [months[int(month)-1] for month in birthmonths]

    c = dict(Counter(birthmonths))
    return c

if __name__=='__main__':
    data = get_months_count('ch34_birthdays.json')
    print(data)
