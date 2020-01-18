import os
import sys
from PIL import Image

#Prompt User for image path and store file path.
image_file = input("Enter Full Image Path: ")

if os.path.isfile(image_file):
	directory, filename = os.path.split(image_file)
	image = Image.open(image_file)
	data = list (image.getdata())
	imageWithoutExif = Image.new(image.mode, image.size)
	imageWithoutExif.putdata(data)
	imageWithoutExif.save(directory + "/Exif_Stripped_" + filename)
	print("File Saved: %s/Exif_Stripped_%s" % (directory, filename))
	sys.exit(0) #exit(0) means a clean exit without any errors/problems.
else:
	print("Image Path Does Not Exist!")
	sys.exit(1) #exit(1) means there was some issue/error/problem and that is why the program is exiting.
