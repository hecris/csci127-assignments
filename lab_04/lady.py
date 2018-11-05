def happyLadybugs(b):
    for i in set(list(b)):
        if i != '_' and b.count(i) <= 1:
            return "NO"
    n_spaces = b.count('_')
    if n_spaces == len(b):
        return "YES"
    if n_spaces > 0:
        return "YES"
    return happy(b)

def happy(b):
    i = 1
    while i < len(b) - 1:
        if b[i - 1] != b[i] and b[i] != b[i + 1]:
            return "NO"
        i += 1
    return "YES"

if __name__ == '__main__':
    print(happyLadybugs("BUSLHRDOC_VQKNWMCRJYQQRWOCNQY_NYR_BVYDBBYHQCQQRUDBOUCUCBVVNKYRDCC"))
    print(happyLadybugs("MKNNNNMMMK"))
    print(happyLadybugs("JI_JWHSBIA__JHIWHII_KK__JIBHK__KBS_B"))
    print(happyLadybugs("RBY_YBR"))
    print(happyLadybugs("__"))
    print(happyLadybugs(""))
