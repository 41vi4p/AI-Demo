import cv2
import random

def noise_black_white(image):
    # Get the dimensions of Image
    row, col = image.shape
    print("Total number of Pixels: ",row, col)
    num_of_pixels = random.randint(1500, 20000)
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 255 #white colour
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 0 #black colour
    return image

image = cv2.imread("D:\Documents\D.P_Projects\AI\IMG\parrot.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image',noise_black_white(image))

cv2.imwrite("D:/Documents/D.P_Projects/AI/IMG/noisyparrot.jpg",noise_black_white(image))

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()