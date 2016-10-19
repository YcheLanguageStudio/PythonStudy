# import gempy2
import binascii

p = 5991810554633396517767024967580894321153
q = 6847944682037444681162770672798288913849
# gmpy2.invert(e, (p-1)*(q-1))


c = int('14a091645d307b8abd8632a1fb83f81e38c1b33d3286ca814a5742bec52c4b06d08', 16)
d = 9876455871473848869533324275271328267592369748302270589984220483284702063644673
print c
decimal_num = pow(c, d, p * q)
print 'Decimal:' + str(decimal_num)
hex_num = hex(decimal_num)
print hex_num
hex_num = hex_num[2:len(hex_num)-1]

print hex_num
print binascii.unhexlify(hex_num)
