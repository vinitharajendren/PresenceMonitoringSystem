import numpy as np 
import cv2

# initializing the canvas as 300 x 300 with 3 channels RGB
# Blue with a black background
canvas = np.zeros((300,300,3), dtype="uint8")

# drawing a green line from top left corner of canvas
# top left to bottom right
#       (B,  G,  R)
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# 3 pixel thick red line from top right
# top right to bottom-left
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#drawing a green 50x50 pixel square,
#starting at 10x10 and ending at 60x60
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# red rectangele with 5 pixel thickness
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#rectangle: blue filled in
blue = (255, 0 ,0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#rest the canvas and draw a white circle in the center of the canvsa
canvas = np.zeros((300,300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1]/2, canvas.shape[0]/2)
white = (255, 255, 255)

for r in range(0, 75, 10):
	cv2.circle(canvas, (centerX, centerY), r, white, 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# lets draw some random cirle
for i in xrange(0, 25):
	#randomly generate radius between 5 and 200
	#random color generated, pick a random point on the canvas
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size = (2,))

	#draw the random cirle
	cv2.circle(canvas,tuple(pt), radius, color, -1)


#showcase the MP
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)