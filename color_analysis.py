import cv2
import numpy as np

image = cv2.imread("images/fall.jpg")
# define the list of boundaries, in BGR!!!!
boundaries = [
	([6, 33, 95], [95, 255, 255]), # range of color for RED -> YELLOW
]
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	pixel_count = cv2.countNonZero(mask)/(image.size/3)
	print('pixel percentage:', pixel_count * 100)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)