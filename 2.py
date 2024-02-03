def fun(s):

    arr = s.split('#')
    #print(arr)
    dat = list(map(int, arr[2].split('-')))
    return dat[0], dat[1], dat[2]
b = []
with open('scientist.txt', encoding='utf-8') as f:
    lines = list(f.readlines())
    print(lines)
    lines.sort(key=fun)
    for lin in lines:
        arr = lin.split('#')
        a = arr[-1].split()
        a[-1] = a[-1][:-2]
        for i in a:
            if len(b)<5 and not i in b:
                b.append(i)
    print(lines)