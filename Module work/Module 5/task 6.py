num = int(input())
flist = [1, 1]
i = 0
while True:
    i += 1
    flist.append(flist[i - 1] + flist[i])
    if num == flist[i]:
        print(i+1)
        break
    elif num < flist[i]:
        print(-1)
        break
