from PIL import Image
import numpy as np

image = Image.open('images/image3.jpg')

amount_of_chunks = 2

chunks = np.empty([amount_of_chunks, amount_of_chunks], dtype=object)

chunk_height = int(image.height/amount_of_chunks)
chunk_width = int(image.width/amount_of_chunks)

for x in range(0, amount_of_chunks):
	for y in range(0, amount_of_chunks):
		chunks[x, y] = image.crop((x*chunk_width, y*chunk_height, x*chunk_width + chunk_width, y*chunk_height + chunk_height))

chunk_averages = np.empty([amount_of_chunks, amount_of_chunks], dtype=object)

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

legofied_image = Image.new('RGB', (amount_of_chunks, amount_of_chunks))

for row in range(0, chunk_averages.shape[0]):
	for col in range(0, chunk_averages.shape[1]):
		legofied_image.putpixel((row, col), chunk_averages[row, col])

legofied_image.show()