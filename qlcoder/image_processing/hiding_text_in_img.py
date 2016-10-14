from PIL import Image

im = Image.open("145303100168558.png")
pix = im.load()
(w, h) = im.size

for x in range(w):
    for y in range(h):
        (r, g, b) = pix[x, y]
        if r & 1:
            r = 255
        else:
            r = 0
        pix[x, y] = (r, 0, 0)

im.save("a.png")
