num = int(input('Insert a number: '))

a = [x for x in range(2, num) if num % x == 0]
print(a)


if type(a) == list:
    print('List')
