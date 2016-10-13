limit = 100000; array = [0] * limit

def query(idx):
    ret = 0
    while idx > 0:
        ret += array[idx]; idx -= idx&(-idx)
    return ret
def update(idx, add):
    while idx < limit:
        array[idx] += add; idx += idx&(-idx)

with open('good-2.txt', 'r') as f:
    ans = 0
    for line in f.readlines():
        token = line.split()
        if token[0] == 'down':
            update(int(token[2]), -int(token[1]))
        elif token[0] == 'up':
            update(int(token[2]), int(token[1]))
        else:
            ans += query(int(token[2])) - query(int(token[1]) - 1)
    print(ans)
