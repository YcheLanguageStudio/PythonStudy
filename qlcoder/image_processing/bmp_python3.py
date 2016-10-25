import binascii
fi = open("aaa.bmp", "rb")
header = fi.read(1078)
line = fi.read()
fi.close()

binline = ''


for i in range(0,len(line)):
    binline += bin(line[i])[2:].zfill(8)
newbinline = ''
for i in range(len(binline)):
    if(i%7 == 0):
        newbinline+='0'
    newbinline+=binline[i]
newhexline = hex(int(newbinline, 2))[2:]
newhexline = '0' + newhexline
newbyteline =  bytes().fromhex(newhexline)
fo = open("out.bmp", "wb")
outbmp = header + newbyteline
line = fo.write(outbmp)
fo.close()