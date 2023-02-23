import cv2
import os
import numpy as np

# Function to compare two images using MSE
def mse(image1, image2):
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err

# Set the path of the folder containing the images
path = r'D:\New Volume E\CAREER\Development\v2pdf\data'

# Set a threshold for the MSE
threshold = 5000

# Create a folder to save dissimilar images
if not os.path.exists("dissimilar_images"):
    os.makedirs("dissimilar_images")

# Iterate over all images in the folder
for filename in os.listdir(path):
    # Load the current image
    current_image = cv2.imread(os.path.join(path, filename))
    
    # Iterate over all other images in the folder
    for other_filename in os.listdir(path):
        # Load the other image
        other_image = cv2.imread(os.path.join(path, other_filename))
        
        # Compare the images using MSE
        if filename != other_filename and mse(current_image, other_image) > threshold:
            # Save the dissimilar images to a new folder
            cv2.imwrite(os.path.join("dissimilar_images", filename), current_image)
            cv2.imwrite(os.path.join("dissimilar_images", other_filename), other_image)


cam.release()
cv2.destroyAllWindows()
