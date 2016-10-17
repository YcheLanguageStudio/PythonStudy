with open('/home/cheyulin/PiDec.txt') as fs:
    for i in range(1, 100):
        ch = fs.read()
        print ch