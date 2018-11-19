def makeacronym(s):
    alphabet = 'abcdefghijklmnopqrstuvwxz'
    numbers = '1234567890'
    res = ''
    for w in s.lower().split():
        l = w[0]
        if l in alphabet or l in numbers: # ignores punctuation
            res += l
    return res

cases = ["", "...", "laugh out loud", "LAUGH OUT LOUD", "Read the... fine manual",
         "In my humble opinion", "In my not so humble opinion", "ok",
         "in my ... opinion", "123", "got 2 go", "looking 4 partner"]

for c in cases:
    print(makeacronym(c))
