import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l

d = build_random_list(10, 3)
print(d)

def locate(l, value):
    print('index of:', value, 'in', l)
    i = 0
    while i < len(l):
        if l[i] == value:
            return i
        i += 1
    return -1

print(locate(d, 2))

def count(l, value):
    print('number of', value, 'in', l)
    n = 0
    i = 0
    while i < len(l):
        if l[i] == value:
            n += 1
        i += 1
    return n

print(count(d, 2))

def reverse(l):
    r = []
    i = len(l) - 1
    while i >= 0:
        r.append(l[i])
        i -= 1
    return r

print(reverse(d))

increasing = [0, 1, 2, 3]
decreasing = [3, 2, 1, 0]


def isIncreasing(l):
    print('Is increasing?', l)
    i = 1
    while i < len(l):
        if l[i - 1] >= l[i]:
            return False
        i +=1
    return True

print(isIncreasing(increasing))
print(isIncreasing(decreasing))
print(isIncreasing(d))

p = [0, 0, 1, 0, 0]

def palindrome(l):
    print('Is palindrome?', l)
    return l == reverse(l)

print(palindrome(p))
print(palindrome(d))


