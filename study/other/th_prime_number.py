def oprime(n):
    counter = 0
    b = 1
    if n == 1:
        print 2
    while counter < n-1:
        b = b + 2
        for a in range(2,b):
            if b % a == 0:
                break
        else:
            counter = counter + 1
            if counter == n-1:
                print b

oprime(13)