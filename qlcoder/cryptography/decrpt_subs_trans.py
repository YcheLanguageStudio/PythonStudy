def test_char_order():
    print chr(97)
    print chr(96 + 26)
    print ord('a')
    print ord('z')
    print ord('A')
    print ord('Z')


cipher_txt = 'Gnykuto gc kl gxhaugyunkyzv, z srxtvg ggvozuvzcyooe ng, sv  ytk y kvkgvzrxtkrzejcykngb.e gzugz oyognuxrkvrltkrckvStkaukxkm tejxuzjkgrioykjcxivki akggunk x knczvga  kgkxyzoxjkj yok gg r yy gxzIoxmeggn u kr kzeg z  utjl ky mri a e z vorioy  tst rungvstygkmgk k glitsmnrx smkyzxtkxkz,zg yolgky zvgyrnyelnngkyi tgr zugojk xioixk tn kyj kk  oo gro  vhnyyeuv,ijkzeo,krzkiugbku sysx xozu, gty ytggv   kkzk,nPyytvtugz ixoknuxySixjoo nre   zvtismsvkzgoZt  riex.yrkglyvkix  iyokcaum yska ynlkgyYomkzggv sgikouk grngkay si.ixgt kmkkkkyzkk zk yj xz kogusutz.iun y k v kgyjzghuyrlnyxto.mgrioyxu guz, osjnuzsst iZgxrkzovln nks  g iekcnmykjjykkvyu zkr uz  h.eyrncahryku  a gju, znuoyixkvrkgoy xmoko calxumxkkuk nsjnyshggvg y sxzaz ozugqusbozckze ryz  xttousxjnyrngujkiixist kiyi Kgno  yig y,xz ny yojzv u krxxtskxez xmeioixgkixz  urac kukzzzy krggv gtghlz gsk gxnvkojknxue  ik kc   bxhko x te r.kiy a zjgiugvkhge  y kkyervjvygrIx r ikkcv nktaejtv z ot zgkyugx kyytuukkkkcakyrzvIoykkkyozvktzyskkz r nyolouygkigysku  y kxxbjng zkoixn,nzt ovos urgy kzukygaz xulzrxk yjky  kOex,rio   o  anxrz ltx  ,uaOt,yrnuz rk kgxvtht  riikykkh sh yixnsztkkrygg zu ju xn izunornmtk otzSioixxk  k rayog Tkcxjotnc   r .ennnut sgtxkxtzyzy mvt  . ky yIunriiy tihundrz,kytnqkukzz,tuaywer.kyacioixkkg grkxiio o  nost'
my_list = []


def transform_ch(ch, shift_num):
    if ch == ',' or ch == ' ' or ch == '.':
        return ch
    else:
        num = ord(ch) - shift_num
        if 65 <= ord(ch) <= 90:
            if num < 65:
                num += 26
        else:
            if num < 97:
                num += 26
        return chr(num)


def substitution(i):
    return ''.join(map(lambda my_ch: transform_ch(my_ch, i), cipher_txt))


def crack_transposition(cipher, msg_col_num):
    msg = cipher
    msg_row_num = (len(cipher) + (msg_col_num - 1)) / msg_col_num
    idx_step = msg_row_num - 1
    padding_col_num = msg_row_num * msg_col_num - len(cipher)
    for idx in range(0, len(cipher)):
        final_index = idx
        
        msg[idx] = cipher[idx]
    return msg


print substitution(6)

new_str = substitution(6)
my_list = []
for another_i in range(2, 1276):
    res = crack_transposition(new_str, another_i)
    if len(res) != 0 and not res.__contains__('   '):
        print another_i
        print res

print '---'

print 'from cipher text 0481592637'

my_list = []
for another_i in range(2, 10):
    res = crack_transposition('0481592637', another_i)
    if len(res) != 0:
        print res
