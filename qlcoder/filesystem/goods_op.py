if __name__ == '__main__':
    n = 1000
    prices = [0] * n
    t = 0
    for line in open("144043123647536.txt"):
        ks = line.strip("\n").split(' ')
        n1=int(ks[1])
        n2=int(ks[2])
        if ks[0] == "up":
            prices[n2] += n1
        elif ks[0] == "down":
            prices[n2] -= n1
        else:
            for i in range(n1, n2+1):
                t += prices[i]

    print t
