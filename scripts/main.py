import sys
from image import parse_image

image = parse_image(sys.argv)

print(image)

image.show()