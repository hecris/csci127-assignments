def countPlurals(line):
    punctuation = [',', '.', '?', '!']
    count = 0
    a = [x if x[-1] not in punctuation else x[:-1] for x in line.split()]
    for w in a:
        if w[-1] == 's':
            count += 1
    return count

def notPossesive(line):
    punctuation = [',', '.', '?', '!']
    count = 0
    a = [x if x[-1] not in punctuation else x[:-1] for x in line.split()]
    for w in a:
        if w[-1] == 's' and w[-2] != "'":
            count += 1
    return count


cases = [
    "",
    "Dogs in shelter!",
    "Dog's toys in shelters?",
    "gorillas gorilla's cats.",
    "My mom's dad's son's grandma's aunt's cats.",
    "Cats! Cats! Cats? Cat's."
    ]

print('=====countPlurals=====')
for c in cases:
    print('Line:',  c)
    print(countPlurals(c))

print('=====notPossesive=====')
for c in cases:
    print('Line:',  c)
    print(notPossesive(c))
