
def my_max(n1, n2, n3):
    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3
    return max

a = int(input('Give me fist nubmer: '))
b = int(input('Give me second nubmer: '))
c = int(input('Give me third nubmer: '))

print('The biggest nubmer is: ' + str(my_max(a,b,c)))
