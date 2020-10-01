def bi(s):
    d = {}
    z = ''
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            z += s[i]
            z += s[i+1]
            if z not in d:
                d[z] = 1
            elif z in d:
                d[z] += 1
            z = ''
    return d
