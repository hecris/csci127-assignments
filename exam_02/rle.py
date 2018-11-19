def encode(s):
    res = []
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            res.append([s[i], count])
            break
        if s[i] == s[i+1]:
            count += 1
        else:
            res.append([s[i], count])
            count = 1
    return res

def decode(l):
    res = ''
    for i in l:
        res += i[0] * i[1]
    return res

cases = ["abbaaacddaaa",
         "abcd",
         "cbbbbbdee",
         "123",
         "",
         " ",
         "encodes any character, including punctuation and numbers",
         "???!!!?",
         "? 1"]

for c in cases:
    print('=' * 30)
    e = encode(c)
    print(e)
    print(decode(e))

