def happyLadybugs(b):
    n_spaces = b.count('_')
    if n_spaces == len(b): # if there are no bugs
        return "YES"
    if enough(b): # if there are at least 2 bugs per color
        if n_spaces > 0: # if there is a space
            return "YES"
        return happy(b) # there is no space, are bugs already happy?
    else:
        return "NO" # not enough bugs per color


def happy(b):
    i = 1
    while i < len(b) - 1:
        if b[i - 1] != b[i] and b[i] != b[i + 1]:
            return "NO"
        i += 1
    return "YES"

def enough(b):
    d = {}
    for i in b:
        if i == '_':
            continue
        d.setdefault(i, 0)
        d[i] += 1
    return min(d.values()) > 1

if __name__ == '__main__':
    print(happyLadybugs("BUSLHRDOC_VQKNWMCRJYQQRWOCNQY_NYR_BVYDBBYHQCQQRUDBOUCUCBVVNKYRDCC"))
    print(happyLadybugs("MKNNNNMMMK"))
    print(happyLadybugs("JI_JWHSBIA__JHIWHII_KK__JIBHK__KBS_B"))
    print(happyLadybugs("RBY_YBR"))
    print(happyLadybugs("__"))
    print(happyLadybugs(""))
