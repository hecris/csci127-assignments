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
    d = {} # make an empty dictionary
    for i in l:
        d.setdefault(i, []) # fill dictionary with unique words from the text

    i = 0
    while i < len(l) - 1:
        w = l[i]
        d[w] += [l[i + 1]] # add next word to the dictionary
        i += 1
    
    return d

f = open('moby-small.txt', 'r')
text = f.read()
d = analyze(text)
print(d)
