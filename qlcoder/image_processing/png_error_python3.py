import binascii
import struct

opfile = open("145682845224096.png", "rb")
wholepng = opfile.read()
opfile.close
ans = b''
answer = open("answer.png", "wb")

pos = 0;
name = wholepng[pos:pos + 8]
ans += name
pos += 8
a = ''
for i in name:
    a += str(i) + ' '
if a != '137 80 78 71 13 10 26 10 ':
    print('error in name')
    print(a)
print(len(wholepng))
countera = 0
while (pos < len(wholepng)):
    lenth = wholepng[pos:pos + 4]
    pos += 4
    size = struct.unpack('I', lenth[::-1])[0]
    if (size == 4096):
        size = 8192
        lenth = struct.pack('I', size)
        lenth = lenth[::-1]
    if size > len(wholepng) - pos:
        print('error in size')
        print('data remain: ', len(wholepng) - pos, "but size = ", size)
        break

    chunk_type_code = wholepng[pos:pos + 4]
    pos += 4
    print('CTC =  ', chunk_type_code)

    chunk_data = wholepng[pos:pos + size]
    pos += size

    calcCRC = binascii.crc32(chunk_type_code + chunk_data)

    CRcode = wholepng[pos:pos + 4]
    pos += 4
    CRC = struct.unpack('I', CRcode[::-1])[0]
    if CRC != calcCRC:
        print('error in CRC')
        print('calcCRC: ', calcCRC, "but CRC = ", CRC)
        print('pos =  ', pos, 'size =  ', size)
        break
    print('pos =  ', pos, 'size =  ', size)
    print('block pass', countera)
    print('-------------')
    ans += lenth + chunk_type_code + chunk_data + CRcode
    countera += 1

# pos = 0
# while pos < len(wholepng) - 4:
#     str_codes = wholepng[pos:pos + 4]
#     if str_codes == b'IHDR' or str_codes == b'cHRM' or str_codes == b'gAMA' or str_codes == b'sBIT' \
#             or str_codes == b'PLTE' or str_codes == b'bKGD' or str_codes == b'hIST' or str_codes == b'tRNS' \
#             or str_codes == b'oFFs' or str_codes == b'pHYs' or str_codes == b'sCAL' or str_codes == b'IDAT' \
#             or str_codes == b'tIME' or str_codes == b'tEXt' or str_codes == b'zTXt' or str_codes == b'fRAc' \
#             or str_codes == b'gIFg' or str_codes == b'gIFt' or str_codes == b'gIFx' or str_codes == b'IEND'\
#             or str_codes == b'sRGB':
#         print(str_codes, 'position;', pos)
#     pos += 1
answer.write(ans)
answer.close()
