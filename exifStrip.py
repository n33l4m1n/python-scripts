import os
import sys
from PIL import Image

image_file = input("Enter Image Path: ")

if os.path.isfile(image_file):
	directory, filename = os.path.split(image_file)

	image = Image.open(image_file)

	data = list (image.getdata())

	image_without_exif = Image.new(image.mode, image.size)

	image_without_exif.putdata(data)

	image_without_exif.save(directory + "/exif-stripped-" + filename)

	print("File Saved: %s/exif-stripped-%s" % (directory, filename))
	sys.exit(0)
else:
	print("Image Path Does Not Exist!")
	sys.exit(1)
