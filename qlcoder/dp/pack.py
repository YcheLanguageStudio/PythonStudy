conduct = [509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]


def solv(i, j):
    "求最大值 i文件编号，j权重"
    if (i < 0):
        return 0
    if (j > conduct[i]):
        rt = max(solv(i - 1, j), solv(i - 1, j - conduct[i]) + conduct[i])
        return rt
    else:
        return solv(i - 1, j)


ans = solv(14, 5000)
print(ans)


def search(i, j):
    "求解路径"
    summer = 0
    while (i >= 0 and j >= 0):
        if (solv(i, j) == solv(i - 1, j - conduct[i]) + conduct[i]):
            summer += conduct[i]
            print("index:" + str(i + 1) + "  weight:" + str(conduct[i]))
            j -= conduct[i]
        i -= 1
    return summer


print(search(14, 5000))
