import cv2
import numpy as np
import os


###### read an image ####
def read(img_path):
   return cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

##### save an image ###
def save(img, img_path="output.jpeg"):
   cv2.imwrite(img_path, img)


### get a list of all the images in a folder ####
# returns (list of images, list of names)
def list_images(folder_path):
    result = []

    # get list of names of all the images in the folder
    file_names = os.listdir(folder_path)

    # read each image as numpy aaray
    for img_name in file_names:
        # full path of the img = folder_path + image name
        image_path = os.path.join(folder_path, img_name)

        # Read the image and add it to the list
        result.append(read(image_path))

    return (result, file_names)


#create a composite image from a list of images
# images = list of images
def get_composite(images):
    # Ensure all images have the same shape
    image_shape = images[0].shape
    for img in images:
        if img.shape != image_shape:
            raise ValueError("All images must have the same shape")

    # Initialize an array to store the composite image
    composite_image = np.zeros_like(images[0], dtype=np.float32)

    # Sum the pixel values from all images
    for img in images:
        composite_image += img.astype(np.float32)

    # Normalize the composite image to the range [0, 255]
    composite_image = (composite_image / len(images)).astype(np.uint8)

    return composite_image