from _LegoHelper import LegoColors as lc
from math import sqrt
import numpy as np
from PIL import Image

def get_average_color(left, upper, right, lower):
	r, g, b = 0, 0, 0
	for x in range(left, right):
		for y in range(upper, lower):
			r += image.getpixel((x, y))[0]
			g += image.getpixel((x, y))[1]
			b += image.getpixel((x, y))[2]
	pixel_count = chunk_width*chunk_height
	r = int(r/pixel_count)
	g = int(g/pixel_count)
	b = int(b/pixel_count)
	return (r, g, b)

def get_dimesions(image, pieces):
	division_factor = sqrt(image.width*image.height/pieces)
	return (int(image.width/division_factor), int(image.height/division_factor))

image = Image.open('images/image10.jpeg')

pieces = 1000
dimensions = get_dimesions(image, pieces)

chunk_width = int(image.width/dimensions[0])
chunk_height = int(image.height/dimensions[1])

chunk_averages = np.empty([dimensions[0], dimensions[1]], dtype=object)

for x in range(0, dimensions[0]):
	for y in range(0, dimensions[1]):
		left, upper, right, lower = x*chunk_width, y*chunk_height, x*chunk_width + chunk_width,  y*chunk_height + chunk_height
		average_color = get_average_color(left, upper, right, lower)
		chunk_averages[x, y] = average_color

legofied_image = Image.new('RGB', (dimensions[0], dimensions[1]))
for row in range(0, chunk_averages.shape[0]):
	for col in range(0, chunk_averages.shape[1]):
		best_lego_color = lc.get_lego_color(chunk_averages[row, col])
		legofied_image.putpixel((row, col), best_lego_color)

legofied_image.show()