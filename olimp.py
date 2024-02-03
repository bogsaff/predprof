f = open('scientist.txt', encoding='utf-8')
fout = open('scientist_origin.txt', 'w', encoding='utf-8')
d = dict()
ok = False
for line in f:
    #print(line)
    arr = line.split('#')
    #print(arr)
    dat = list(map(int, arr[2].split('-')))
    d[arr[0]] = [arr[1], dat, arr[3]]
minid = [0, 0, 0]
curent_user = []
for key in d.keys():
    if d[key][0] == 'Аллопуринол':
        dat_curent = d[key][1]
        if minid == [0, 0, 0]:
            minid = d[key][1]
            curent_user = d[key]
        elif (dat_curent[0] < minid[0]) or (dat_curent[0] == minid[0] and dat_curent[1] < minid[1]) or (dat_curent[0] == minid[0] and dat_curent[1] == minid[1] and dat_curent[2]< minid[2]):
            curent_user = d[key]
fout.write('Разработчиками Аллопуринола были такие люди:\n')
for key in d.keys():
    if d[key]!= curent_user and d[key][0]=='Аллопуринол':
        fout.write(f'{key} - {d[key][1][0]}.{d[key][1][1]}.{d[key][1][2]}\n')
f.close()
fout.close()