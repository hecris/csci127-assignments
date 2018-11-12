def clean(text):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in text.lower():
        if char in alphabet:
            result += char
        else:
            result += " "
    return result

def analyze(text):
    text = clean(text)
    l = text.split()
    d = {}

    for i in range(len(l)-1):
        w = l[i]
        d.setdefault(w, [])
        n = l[i + 1] # next word
        d[w].append(n)

    return d

f = open('moby-small.txt', 'r')
text = f.read()
d = analyze(text)
print(d)
