def score(w):
    d = {
        "aeioulnrst":1,
        "dg":2,
        "bcmp":3,
        "fhvwy":4,
        "k":5,
        "jx":8,
        "qz":10}
    alphabet = ''.join(d.keys())
    res = 0
    for l in w:
        if l not in alphabet:
            return "you have invalid characters"
        for k in d.keys():
            if l in k:
                res += d[k]
    return res

cases = ["hello", "", "123", " 1 2 3 ", "h e",
         "super", "jaguar", "???", "1 h"]

for c in cases:
    print(score(c))
