import sys
from PIL import Image

image = Image.open('images/image3.jpg')

slices = []

slice_height = int(image.height/10)
slice_width = int(image.width/10)

for x in range(0, 10):
	for y in range(0, 10):
		slices.append(image.crop((y*slice_width, x*slice_height, y*slice_width + slice_width, x*slice_height + slice_height)))

print(slice_height, slice_width)