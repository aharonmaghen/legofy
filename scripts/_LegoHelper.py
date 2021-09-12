class LegoColors:
	__lego_colors = {
		"Cool Yellow": (254, 255, 135),
		"Bright Bluish Green": (37, 168, 164),
		"Medium Lilac": (135, 109, 200),
		"Medium Nougat": (160, 111, 78),
		"Bright Yellowish Green": (151, 187, 63),
		"Earth Blue": (73, 103, 151),
		"Medium Stone Grey": (146, 146, 146),
		"Dark Stone Grey": (101, 101, 101),
		"Light Purple": (238, 149, 197),
		"Reddish Brown": (84, 42, 20),
		"Sand Green": (117, 155, 130),
		"Dark Red": (132, 48, 61),
		"Medium Blue": (116, 151, 201),
		"Brick Yellow": (176, 161, 111),
		"Bright Blue": (34, 97, 176),
		"Medium Azur": (96, 160, 185),
		"Bright Orange": (218, 125, 41),
		"Bright Red": (188, 7, 6),
		"Black": (0, 0, 0),
		"Bright Yellow": (243, 194, 0),
		"White": (255, 255, 255),
		"Medium Lavender": (140, 97, 161),
		"Bright Reddish Violet": (141, 59, 121)
	}
	@staticmethod
	def get_lego_color(rgb):
		from math import sqrt
		lego_colors = LegoColors.__lego_colors
		distances = []

		r1, g1, b1 = rgb[0], rgb[1], rgb[2]
		for color in lego_colors:
			r2, g2, b2 = lego_colors.get(color)[0], lego_colors.get(color)[1], lego_colors.get(color)[2]
			distances.append((sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2), color))
		
		return lego_colors.get(min(distances)[1])


	@staticmethod
	def __show_lego_colors():
		from PIL import Image
		for color in LegoColors.__lego_colors:
			Image.new('RGB', (200, 200), LegoColors.__lego_colors.get(color)).show()