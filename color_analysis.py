import cv2
import numpy as np
import operator

# img = cv2.imread("images/fall.jpg")
# brown = [255, 255, 0]  # RGB
# diff = 20
# boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
#                [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
# # in order BGR as opencv represents images as numpy arrays in reverse order

# for (lower, upper) in boundaries:
#     lower = np.array(lower, dtype=np.uint8)
#     upper = np.array(upper, dtype=np.uint8)
#     mask = cv2.inRange(img, lower, upper)
#     output = cv2.bitwise_and(img, img, mask=mask)

#     ratio_brown = cv2.countNonZero(mask)/(img.size/3)
#     print('brown pixel percentage:', np.round(ratio_brown*100, 2))

image = cv2.imread("images/fall.jpg")
# define the list of boundaries, in BGR!!!!
boundaries = [
	# ([164, 0, 0], [255, 105, 97])
	# ([6, 39, 156], [46, 188, 243])
	# ([0, 0, 185], [0, 216, 209])
	([6, 33, 95], [95, 255, 255]),
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
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)