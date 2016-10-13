from PIL import Image

image = Image.open("61244.jpg")
image.show()
pixel = image.load()
r,g,b = pixel[0, 0]
print r,g,b
