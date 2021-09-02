from PIL import Image
import numpy as np
from _LegoHelper import LegoColors as lc

def get_average_color(left, right, upper, lower):
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

image = Image.open('images/image3.jpg')

dimension = 75

chunk_width = int(image.width/dimension)
chunk_height = int(image.height/dimension)

chunk_averages = np.empty([dimension, dimension], dtype=object)

for x in range(0, dimension):
	for y in range(0, dimension):
		left, right, upper, lower = x*chunk_width, x*chunk_width + chunk_width, y*chunk_height, y*chunk_height + chunk_height
		average_color = get_average_color(left, right, upper, lower)
		chunk_averages[x, y] = average_color

legofied_image = Image.new('RGB', (dimension, dimension))
for row in range(0, chunk_averages.shape[0]):
	for col in range(0, chunk_averages.shape[1]):
		best_lego_color = lc.get_lego_color(chunk_averages[row, col])
		legofied_image.putpixel((row, col), best_lego_color)

legofied_image.show()