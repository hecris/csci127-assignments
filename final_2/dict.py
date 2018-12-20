def addline(d, line):
    punctuation = [',', '.', '?', '!']
    line = line.lower()
    a = [x if x[-1] not in punctuation else x[:-1] for x in line.split()]
    for w in a:
        d.setdefault(w[0], [])
        d[w[0]] += [w]
    return d

d = {}
addline(d, "I have two cats.")
addline(d, "If you are in imminent danger, RUN to a safe location!")
addline(d, "Warn others to move, but do not place yourself in danger to do so!")
addline(d, "No food allowed in the auditorium.")
addline(d, "No talking in the library?")

for k,v in d.items():
    print(k, v)

def spellcheck(d, word):
    word = word.lower()
    for l in d.values():
        if word in l:
            return True
    return False

cases = ['cats', 'hello', 'two', '', '?', '.', 'library']

for c in cases:
    print(c, spellcheck(d, c))
