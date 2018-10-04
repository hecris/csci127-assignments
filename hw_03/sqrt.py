# Jadeja and Christopher jadeja.baptiste91@myhunter.cuny.edu
def mysqrt(n):
    guess = n / 2
    old_guess = guess
    while guess ** 2 != n:
        guess = (guess + (n/guess)) / 2
        if old_guess == guess:
            return guess
        old_guess = guess
    return guess

for i in range(1,101):
    print(i, mysqrt(i))

