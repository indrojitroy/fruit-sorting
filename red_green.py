from PIL import Image
import cv2 as cv
def getcolor(filename):
	im=Image.open(filename)
	pix=im.load()
	imtuple=im.size
	l=imtuple[0]
	b=imtuple[1]
	countred=0
	countgreen=0
	# Introduced error margin to reduce the error.
	errormargin=25
	for i in range(l):
		for j in range(b):
			temptuple=pix[i,j]
			if(temptuple[0]>temptuple[1]+errormargin):
				countred=countred+1
			if(errormargin+temptuple[0]<temptuple[1]):
				countgreen=countgreen+1
  #print("countred=",countred)
	#print("countgreen=",countgreen)
	if(countred>=countgreen):
		return "RED"
	else:
		return "GREEN"
img=cv.imread("/content/drive/My Drive/try.jpg")
cv2_imshow(img)
print(getcolor("/content/drive/My Drive/try.jpg"))

img2=cv.imread("/content/drive/My Drive/tempg.jpg")
cv2_imshow(img2)
print(getcolor("/content/drive/My Drive/tempg.jpg"))

# img2=cv.imread("/content/drive/My Drive/tempr.jpg")
# cv2_imshow(img2)
# print(getcolor("/content/drive/My Drive/tempr.jpg"))

#print(getcolor("/content/drive/My Drive/IMG-20190724-WA0000.jpg"))
# print(getcolor("./data/good/32.jpg"))
# print(getcolor("./data/good/33.jpg"))

