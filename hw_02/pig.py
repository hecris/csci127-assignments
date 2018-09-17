# Christopher He and Krystlle Fajardo
def piglatinify(name):
    vowels = 'aeiouAEIOU'
    if name[0] in vowels:
        return name + 'ay'
    return name[1:] + name[:1] + 'ay'

print(piglatinify('hello'))
print(piglatinify('eat'))
print(piglatinify('test'))
print(piglatinify('Out'))
