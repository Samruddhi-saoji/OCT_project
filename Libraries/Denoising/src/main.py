from Denoise import Denoiser
from image_handling import save, read

# the denoiser object
denoiser = Denoiser()

'''
#Denoising a single image
img = read("file.jpg")
result = denoiser.denoise_image(img)
save(result, "output.jpg")
'''

#denoise all the images in a folder
fldr = ".\\originals"
dest = ".\\output"

denoiser.denoise_all_images(fldr, dest)


