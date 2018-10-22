def compress_word(w):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = []
    for letter in w[1:]:
        if letter in vowels:
            continue
        res.append(letter)
    return w[0] + ''.join(res)

print('halloween', '-->', compress_word('halloween'))
print('special', '-->', compress_word('special'))
print('apple', '-->', compress_word('apple'))

def sentence(line):
    l = line.split()
    res = []
    for w in l:
        res.append(compress_word(w))
    return " ".join(res)

line1 = 'I like to eat apple pie'
line2 = 'Who is there'

print(line1, '-->', sentence(line1))
print(line2, '-->', sentence(line2))


