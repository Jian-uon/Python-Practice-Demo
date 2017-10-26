from PIL import Image

img = Image.open('cropCurrent.jpg')
region = (48, 0, 260, 120)
#img.crop(region).show()
region2 = (6, 0, 48, 120)
img.crop(region2).show()