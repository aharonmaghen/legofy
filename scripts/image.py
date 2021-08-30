from PIL import Image

def parse_image(cmd_arguments):
	if (len(cmd_arguments) != 2):
		raise InvalidNumberOfArgumentError('At least one argument')

	path = cmd_arguments[1]
	image = Image.open(path)
	
	return image