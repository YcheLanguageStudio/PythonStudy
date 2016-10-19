cipher_txt = 'Gnykuto gc kl gxhaugyunkyzv, z srxtvg ggvozuvzcyooe ng, sv  ytk y kvkgvzrxtkrzejcykngb.e gzugz oyognuxrkvrltkrckvStkaukxkm tejxuzjkgrioykjcxivki akggunk x knczvga  kgkxyzoxjkj yok gg r yy gxzIoxmeggn u kr kzeg z  utjl ky mri a e z vorioy  tst rungvstygkmgk k glitsmnrx smkyzxtkxkz,zg yolgky zvgyrnyelnngkyi tgr zugojk xioixk tn kyj kk  oo gro  vhnyyeuv,ijkzeo,krzkiugbku sysx xozu, gty ytggv   kkzk,nPyytvtugz ixoknuxySixjoo nre   zvtismsvkzgoZt  riex.yrkglyvkix  iyokcaum yska ynlkgyYomkzggv sgikouk grngkay si.ixgt kmkkkkyzkk zk yj xz kogusutz.iun y k v kgyjzghuyrlnyxto.mgrioyxu guz, osjnuzsst iZgxrkzovln nks  g iekcnmykjjykkvyu zkr uz  h.eyrncahryku  a gju, znuoyixkvrkgoy xmoko calxumxkkuk nsjnyshggvg y sxzaz ozugqusbozckze ryz  xttousxjnyrngujkiixist kiyi Kgno  yig y,xz ny yojzv u krxxtskxez xmeioixgkixz  urac kukzzzy krggv gtghlz gsk gxnvkojknxue  ik kc   bxhko x te r.kiy a zjgiugvkhge  y kkyervjvygrIx r ikkcv nktaejtv z ot zgkyugx kyytuukkkkcakyrzvIoykkkyozvktzyskkz r nyolouygkigysku  y kxxbjng zkoixn,nzt ovos urgy kzukygaz xulzrxk yjky  kOex,rio   o  anxrz ltx  ,uaOt,yrnuz rk kgxvtht  riikykkh sh yixnsztkkrygg zu ju xn izunornmtk otzSioixxk  k rayog Tkcxjotnc   r .ennnut sgtxkxtzyzy mvt  . ky yIunriiy tihundrz,kytnqkukzz,tuaywer.kyacioixkkg grkxiio o  nost'

lower_case_cipher_txt = cipher_txt.lower()


# print lower_case_cipher_txt

def return_new_str(i):
    new_str = str()
    for my_ch in lower_case_cipher_txt:
        num = ord(my_ch) - i
        if num < 97:
            num += 26
        if 97 + 26 > num >= 97:
            my_ch = chr(num)
        new_str += my_ch
    return new_str


def transform(cipher, i):
    msg = str()
    group_num = (len(cipher) + (i - 1)) / i
    for j in range(0, group_num):
        index = j
        while index < len(cipher):
            msg += cipher[index]
            index += group_num
    return msg


# for another_j in range(0, 26):
new_str = return_new_str(6)
print new_str
for another_i in range(2, 1276):
    res = transform(new_str, another_i)
    print res
