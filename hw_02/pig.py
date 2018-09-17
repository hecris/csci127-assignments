# Christopher He and Krystlle Fajardo
def pig_latin(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if name[0] in vowels:
        return name + 'ay'
    return name[1:] + name[:1] + 'ay'

print(pig_latin('hello'))
print(pig_latin('eat'))
print(pig_latin('test'))
print(pig_latin('Out'))
