def collatz(n):
    print('input:', n)
    steps = 0
    while n > 1:
        even = n % 2 == 0
        if even:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        steps +=1
    return steps

print('steps:', collatz(100))

    
        
