import struct
from PIL import Image
import io

picfil = open("rf.data",'rb')
avail = picfil.read()
pos = 0
allgraph = {}
numb = 0
while(avail[pos] ！= 2):
    able = avail[pos] #提取标记位
    pos += 1
    size = 0

    for i in range(0,4): #由于用struct转码会用Little-Endian，而应该用Big-Endian，所以此处需要手动转码获得size
        if(avail[i+pos] != 0):
            if (size == 0):
                size = avail[i+pos]
            else:
                size = size << 8
                size = size + avail[i+pos]
    '''
    注：for内容不能删改成：
                size = size << 8 + avail[i+pos]
    左位移byte之后直接计算会使得后续计算结果出问题，务必要分开计算。
    目测是因为默认加减是对int用的，而int是4byte，所以直接算会导致计算结果用问题。
    而分开加减会让byte这样会自动转成int再去计算，所以能算对

    若有人知道更好的写法请务必告诉我
    '''

    pos += 4
    pic = avail[pos: pos + size]
    allgraph[numb] = pic
    numb+=1
    pos += size
    print(pos)
picfil.close()

for i in allgraph:
    fi = open(str(i) + ".png",'wb')
    fi.write(allgraph[i])
    fi.close()
'''
注，之前看了一下感觉是png就直接png后缀了，如果有人知道怎么确定后缀请告诉我
且此算法不知道为什么会有一个图片打不开，我不确定是哪里错了还是本身就是有个图片文件损坏了，有人知道也请告诉我，谢谢
'''
