# Christopher He and Jackie He
def fizzbuzz(max_value):
    i = 1
    count = 0
    while i <= max_value:
        if i % 15 == 0:
            print('FizzBuzz')
            count = count + 1
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i = i + 1
    return count

print(fizzbuzz(100))

