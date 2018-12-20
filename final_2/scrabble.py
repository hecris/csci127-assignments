def canMakeWord(letters, word):
    a = list(letters)
    for l in word:
        if l in a:
            a.remove(l)
        else:
            return False
    return True

def withWild(letters, word):
    a = list(letters)
    for l in word:
        if l in a:
            a.remove(l)
        elif '?' in a:
            a.remove('?')
        else:
            return False
    return True


print('=====canMakeWord=====')
cases = [
    ("ladilmy", "daily"),
    ("eerriin", "eerie"),
    ("orrpgma", "program"),
    ("orppgma", "program"),
    ("", "hey"), # should return false
    ("hello", "") # should return true, no word to make
    ]

for c in cases:
    print(c[0], c[1], canMakeWord(c[0], c[1]))

print('=====withWild=====')

cases = [("lloh?", "hello"),
         ("agll??og", "gorilla"),
         ("o?????a", "program"),
         ("", "hey"), # should return false
         ("hello", "") # should return true, no word to make
         ]

for c in cases:
    print(c[0], c[1], withWild(c[0], c[1]))
