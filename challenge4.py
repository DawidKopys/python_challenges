number = int(input('Give me a number: '))
num_list = range(1, number+1)

print('List containing number lessser than', number, end=':\n')
print(list(num_list))

# div_list = []
# for num in num_list:
#     if number % num == 0:
#         div_list.append(num)

div_list = [num for num in num_list if number%num == 0]

print(number, 'divisors:', div_list)
