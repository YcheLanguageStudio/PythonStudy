def gcd(big, small):
    if small == 0:
        return big
    else:
        return gcd(small, big % small)


def fast_pow(num, fac):
    if fac < 2:
        return num ** fac
    else:
        return fast_pow(num, (fac + 1) / 2) * fast_pow(num, fac / 2)


if __name__ == '__main__':
    for i in range(10):
        print fast_pow(2, i)
