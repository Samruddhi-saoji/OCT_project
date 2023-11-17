#import libraries
import cv2
import numpy as np

from image_handling import get_composite, list_images, save

class Denoiser:
    def __init__(self) -> None:
        pass

    ###### adaptive NLM #####
    def denoise(self, img, h=10, window=100, patch=7):
        result = cv2.fastNlMeansDenoising(img, None, h=h, templateWindowSize=patch, searchWindowSize=window)

        return result
    

    ############# contrast enhancement ##################
    def contrast_enhancement(self, img, threshold=10, box=(2,4)):
        # shape of input image
        rows, cols = img.shape

        #the result array  #same shape as input
        result = img.copy()

        # get width and height of the patch (box)
        box_width, box_height = box[1], box[0]

        # denoise the image one patch at a time
        for y in range(0, rows, box_height):
            for x in range(0, cols, box_width):
                # Extract the patch
                patch = img[y:y+box_height, x:x+box_width]

                # Calculate the average patch value
                avg = np.mean(patch[:,:])

                # if the patch average is considered black
                if avg <= threshold:
                    #make the black pixels blacker
                    patch[patch <= threshold] = patch[patch <= threshold]*(0.8)
                    
                    # make the non-black pixels black
                    patch[patch > threshold] = avg

                # Update the patch in the result image
                result[y:y+box_height, x:x+box_width] = patch

        return result
    

    #the final function
    def denoise_image(self, img, box=(2,4)):
        d = self.denoise(img)
        d1 = self.contrast_enhancement(d, threshold=10, box=box)
        d2 = self.contrast_enhancement(d, threshold= 30, box=box)
        d3 = self.contrast_enhancement(d, threshold=45, box=box)
        #d4 = contrast_enhancement(d, threshold=45, box=box)
        
        images = [d1, d2, d3]

        result = get_composite(images)

        return result
    


    # denoise all images in the folder "src"
    #save the results to folder "dest"
    def denoise_all_images(self, src, dest):
        #get the list of images in the folder
        images, names = list_images(src)
        '''
            - Each image in the folder will be read as a numpy array using openCV, and added to the "images" list
            - "names" = list of name of each image in the folder
        '''

        # denoise each image and save the output to the dest folder
        count=0
        for img in images:
            result = self.denoise_image(img) 
            save(result, f"{dest}\\{names[count][:-4]}.jpg")
            print(f"Image {count+1} saved.")
            count +=1 

