import random
import timeit
import math

def is_in_list(a_list, number):
    return number in a_list

def is_in_list_linear_search(a_list, number):
    for el in a_list:
        if el == number:
            return True
    return False

def is_in_list_binary_search(a_list, number):
    down = 0
    mid_ind = int(len(a_list)/2)
    up = len(a_list)-1
    i = 0

    while mid_ind <= up and mid_ind >= down:
        print("iteracja:", i, end='  ')
        print("  down =", down, "(" + str(a_list[down]) + ")  mid =", mid_ind, "(" + str(a_list[mid_ind]) + ")  up =",  up, "(" + str(a_list[up]) + ")")

        print(a_list[down:up+1], end='\n\n')

        i = i + 1
        if number == a_list[mid_ind]:
            return True
        elif number < a_list[mid_ind]:
            up = mid_ind    # up = 1
            mid_ind = int(down + (mid_ind-down)/2)
            print('new mid =', mid_ind)
        elif number > a_list[mid_ind]:
            down = mid_ind
            mid_ind = int(mid_ind + (up-mid_ind)/2)

    return False

def is_in_list_binary_search(a_list, number):
    down = 0
    up = len(a_list)-1

    while True:
        mid_ind = int(down + abs(up - down) / 2)

        print('down=', down, 'up=', up, 'mid_ind=', mid_ind)
        if mid_ind == down or mid_ind == up:
            if a_list[mid_ind] == number or a_list[up] == number:
                return True
            else:
                return False

        if number == a_list[mid_ind]:
            return True
        elif number < a_list[mid_ind]:
            up = mid_ind
        elif number > a_list[mid_ind]:
            down = mid_ind

    return False

def find(ordered_list, element_to_find):
    start_index = 0
    end_index = len(ordered_list) - 1

    while True:
        middle_index = int((end_index - start_index) / 2)

        # print('start_index=', start_index, 'end_index=', end_index, 'middle_index=', middle_index)

        if middle_index == start_index or middle_index == end_index:
            if ordered_list[middle_index] == element_to_find or ordered_list[end_index] == element_to_find:
                return True
            else:
                return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index

def binarySearch(arr, x):
    l = 0
    r = len(arr)

    while l <= r:
        mid = int(l + (r - l)/2)
        if mid < l or mid > r:
            return False

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid
        elif arr[mid] > x:
            r = mid

    return False

def binarySearchRecursion(arr, x, l, r):
    mid = int(l + (r - l)/2)
    # print('r=', r, 'l=', l, 'mid=', mid)

    if arr[mid] == x:
        return True
    elif l > r or mid < l or mid > r:
        return False
    elif arr[mid] < x:
        return(binarySearchRecursion(arr, x, mid+1, r))
    elif arr[mid] > x:
        return(binarySearchRecursion(arr, x, l, mid-1))

in_l = [1, 2, 3, 4, 5, 6, 7]
# in_l = random.sample(range(0,100000), 10000)
in_l.sort()
# num = random.randint(0,100000)
num = 8


print(in_l)
print("Liczba:", num, '\n')
print(is_in_list(in_l, num))
print(is_in_list_linear_search(in_l, num))
print(find(in_l, num))
print(is_in_list_binary_search(in_l, num))
print(binarySearch(in_l, num))
print(binarySearchRecursion(in_l, num, 0, len(in_l)))

# t1 = timeit.repeat(lambda: is_in_list(in_l, num))
# print('t1 =', max(t1))
# t2 = timeit.repeat(lambda: is_in_list_linear_search(in_l, num))
# print('t2 =', max(t2))
# t3 = timeit.repeat(lambda: is_in_list_binary_search(in_l, num))
# print('t3 =', max(t3))
# t4 = timeit.repeat(lambda: binarySearch(in_l, num))
# print('t4 =', max(t4))
# t5 = timeit.repeat(lambda: binarySearchRecursion(in_l, num, 0, len(in_l)))
# print('t5 =', max(t5))



# todo binary search using recursion
