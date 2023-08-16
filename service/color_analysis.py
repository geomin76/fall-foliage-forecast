import cv2
import numpy as np

def color_analysis(url):
    image = cv2.imread(url)
    # lower and upper range of color, in BGR! (reverse of RGB)
    lower_range = [6, 33, 95] # dark red
    upper_range = [95, 255, 255] # bright yellow

    # create NumPy arrays from the boundaries
    lower = np.array(lower_range, dtype = "uint8")
    upper = np.array(upper_range, dtype = "uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)

    pixel_count = cv2.countNonZero(mask)/(image.size/3)
    pixel_percentage = pixel_count * 100

    ## For printing and showing the image locally
    # output = cv2.bitwise_and(image, image, mask = mask)
    # print('pixel percentage:', pixel_count * 100)
    # # show the images
    # cv2.imshow("images", np.hstack([image, output]))
    # cv2.waitKey(0)

    return pixel_percentage