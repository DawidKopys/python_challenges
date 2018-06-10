import random

def pickRandomWord1(filename):
    with open(filename, 'r') as in_file:
        # content = in_file.readlines()
        content = [line.rstrip('\n') for line in in_file]    # get rid of the newline character
    return random.choice(content)

def pickRandomWord2(filename):
    content = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            content.append(line.rstrip('\n'))
    return random.choice(content)

def pickRandomWord3(filename):
    rand_line_number = random.randrange(1, 267751)
    index = 0
    with open(filename, 'r') as in_file:
        line = in_file.readline()
        while line != 0 and index != rand_line_number:
            line = in_file.readline()
            index = index + 1
    return line.rstrip('\n')

def pickRandomWord4(filename):
    content = []
    with open(filename, 'r') as in_file:
        line = in_file.readline()
        while line:
            content.append(line.rstrip('\n'))
            line = in_file.readline()
    return random.choice(content)

def pickRandomWord5(filename):
    with open(filename, 'r') as in_file:
        content = list(in_file)
    return random.choice(content).rstrip('\n')

f_name = 'ch30_dict.txt'
l_s = pickRandomWord1(f_name)
print(l_s)
l_s = pickRandomWord2(f_name)
print(l_s)
l_s = pickRandomWord3(f_name)
print(l_s)
l_s = pickRandomWord4(f_name)
print(l_s)
l_s = pickRandomWord5(f_name)
print(l_s)
