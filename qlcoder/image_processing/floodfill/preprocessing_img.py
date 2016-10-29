# -*- coding: utf-8 -*-
from PIL import Image


def classify(R, G, B):
    D1 = abs(R - G)
    D2 = abs(G - B)
    D3 = abs(B - R)
    D = max(D1, D2, D3)
    S = R + G + B
    if D > 60:
        return 'green'
    elif S < 512:
        return 'black'
    else:
        return 'white'


im = Image.open('bigspiral.png')
(width, height) = im.size
for x in range(width):
    for y in range(height):
        (R, G, B) = im.getpixel((x, y))
        Class = classify(R, G, B)
        if Class == 'black':
            im.putpixel((x, y), (0, 0, 0))
        elif Class == 'white':
            im.putpixel((x, y), (255, 255, 255))
        else:
            im.putpixel((x, y), (149, 114, 220))

im.save('tmp1.png')
