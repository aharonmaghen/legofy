from PIL import Image
import numpy as np

image = Image.open('images/image3.jpg')
chunks = np.empty([10, 10], dtype=object)

chunk_height = int(image.height/10)
chunk_width = int(image.width/10)

for x in range(0, 10):
	for y in range(0, 10):
		chunks[x, y] = image.crop((y*chunk_width, x*chunk_height, y*chunk_width + chunk_width, x*chunk_height + chunk_height))

chunk_averages = np.empty([10, 10], dtype=object)

for row in range(0, chunks.shape[0]):
	for col in range(0, chunks.shape[1]):
		curr_chunk = chunks[row, col]
		r, g, b = 0, 0, 0
		for x in range(curr_chunk.width):
			for y in range(curr_chunk.height):
				r += curr_chunk.getpixel((x, y))[0]
				g += curr_chunk.getpixel((x, y))[1]
				b += curr_chunk.getpixel((x, y))[2]
		pixel_count = curr_chunk.width*curr_chunk.height
		r = int(r/pixel_count)
		g = int(g/pixel_count)
		b = int(b/pixel_count)
		chunk_averages[row, col] = (r, g, b)

legofied_image = Image.new('RGB', (10, 10))

for row in range(0, chunk_averages.shape[0]):
	for col in range(0, chunk_averages.shape[1]):
		legofied_image.putpixel((row, col), chunk_averages[row, col])

legofied_image.show()