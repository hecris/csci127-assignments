st="7 11"
ab="5 15"
mn="3 2"
apples="-2 2 1"
oranges="5 -6"

def countApplesAndOranges(st, ab, mn, apples, oranges):
    s,t = split_to_int(st)
    a,b = split_to_int(ab)
    m,n = split_to_int(mn)
    apples = split_to_int(apples)
    oranges = split_to_int(oranges)
    count_a = 0
    for x in range(m):
        d = a + apples[x]
        if s <= d and d <= t:
            count_a += 1
    count_b = 0
    for y in range(n):
        d = b + oranges[y]
        if s <= d and d <= t:
            count_b += 1
    print(count_a, 'apples and', count_b, 'oranges')
    

def split_to_int(s):
    return list(map(int, s.split()))

countApplesAndOranges(st, ab, mn, apples, oranges)
countApplesAndOranges("4 6", "3 10", "4 4", "1 -1 2 4", "0 -1 2 0")
countApplesAndOranges("1 2", "3 4", "0 0", "", "")
