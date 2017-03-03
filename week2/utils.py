from scipy.misc import imread
import numpy as np

def prepImage(file):
	'''this function converts the image to the appropriate format to
	be used as a test image on the trained mnist model. MNIST expects 0
	for white and 1 for black, so we use an inverted image, that way
	all the black becomes zero and a simple conditional changes all other values
	greater than zero to 1'''

	img = imread(file) #read the file
	img = img[:,:,0] #convert 3 channel to single channel
	img = img.flatten() #flatten the image into an array

	for i in range(len(img)): #convert all values greater than 10 to 1 to denote black
		if img[i]>10:
			img[i] = 1
		else:
			img[i] = 0

	img = np.expand_dims(img, axis=0) # convert from shape (784,) to (1,784)
	img = img.astype(np.float32) # convert from uint8 to float32

	return img
