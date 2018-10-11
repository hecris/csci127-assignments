def filterodd(l):
    res = []
    for i in l:
        if i % 2 != 0:
            res.append(i)
    return res

def mapsquare(l):
    res = []
    for i in l:
        res.append(i**2)
    return res

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print('original list:', l)
    print(filterodd(l))
    print(mapsquare(l))
