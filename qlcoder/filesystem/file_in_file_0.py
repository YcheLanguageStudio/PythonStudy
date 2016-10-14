f = open('rf.data', 'rb')

filename = 1
signal = 0
while True:
    signal = int.from_bytes(f.read(1), byteorder='big')
    if signal == 2:
        break
    else:
        size = int.from_bytes(f.read(4), byteorder='big')
        content = f.read(size)
        if signal == 0:
            with open('pics/'+str(filename), 'wb') as fout:
                fout.write(content)
            filename += 1
f.close()
