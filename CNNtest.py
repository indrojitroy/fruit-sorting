from keras.layers import Dense
from keras import layers, models, optimizers
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from keras.models import load_model

model=load_model('/content/drive/My Drive/model_keras.h5')
model.load_weights('/content/drive/My Drive/model_weights.h5')

# model.summary()

nrows = 150
ncols = 150
channels = 3 # RGB

def quality(filename):
	x=[] #list of image name
	x.append(filename)
	X = []
	for i in x:
		X.append(cv2.resize(cv2.imread(i,cv2.IMREAD_COLOR), (nrows,ncols), interpolation=cv2.INTER_CUBIC))
	# Convert to numpy array
	X = np.array(X)
	x = np.array(X)
	test_datagen = ImageDataGenerator(rescale=1./255)
	i = 0
	labels=[]
	for batch in test_datagen.flow(x, batch_size=1):
		pred=model.predict(batch)
		if pred >0.5: #since 1 is good and 0 is bad in training label
			return "GOOD"
		else:
			return "BAD"

img=cv2.imread("/content/drive/My Drive/bad.jpg")
cv2_imshow(img)
cv.destroyAllWindows()
print(quality("/content/drive/My Drive/bad.jpg"))

img=cv2.imread("/content/drive/My Drive/try.jpg")
cv2_imshow(img)
cv.destroyAllWindows()
print(quality("/content/drive/My Drive/try.jpg"))

