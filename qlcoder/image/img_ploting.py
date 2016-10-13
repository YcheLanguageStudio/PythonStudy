from PIL import Image
img = Image.new('RGB', (1000, 1000), (0, 0, 0))
px = img.load()
with open('145035182953188.txt', 'r') as p:
    for line in p:
        point = line.split()
        px[(int(point[0]), int(point[1]))] = (255, 255, 255)
img.show()
