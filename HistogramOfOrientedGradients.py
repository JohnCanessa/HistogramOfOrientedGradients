# **** import statements ****
import matplotlib.pyplot as plt

import skimage
from skimage.feature import hog
from skimage import data, color, io, exposure


# **** read image of interest ****
monalisa = skimage.io.imread('./images/pexels-monalisa.jpg')

# **** display image of interest ****
plt.figure(figsize=(10, 8))                         # set the size of the figure
plt.imshow(monalisa, cmap='gray')                   # display image of interest
plt.title('Monalisa')                               # set the title for the image
plt.show()                                          # display the figure


# **** compute the HOG of the image ****
fd, hog_image = hog(monalisa,                       # image of interest
                    pixels_per_cell=(16, 16),       # size (in pixels) of a cell
                    block_norm='L2-Hys',            # block normalization method
                    visualize=True,                 # visualize HOG descriptors on image
                    channel_axis=-1)                # axis of color channel in the image

                    #multichannel=True)              # if applying algorithm to a color image


# **** display the HOG of the image ****
fig, axes = plt.subplots(   1,
                            2, 
                            figsize=(10, 8), 
                            sharex=True, 
                            sharey=True)

# **** ****
ax = axes.ravel()                                   # flatten axes array

# **** ****
ax[0].imshow(monalisa, cmap='gray')                 # display image of interest
ax[0].set_title('Original image')                   # set the title for the image

# **** stretch or shrink the intensity levels of the 
#      image- results in a higher contrast image ****
hog_image_rescaled = exposure.rescale_intensity(hog_image,
                                                in_range=(0, 10))

# **** ****
ax[1].imshow(hog_image_rescaled, cmap='gray')       # display HOG of image
ax[1].set_title('HOG image')                        # set the title for the image

# **** ****
plt.tight_layout()                                  # adjust subplot parameters to give specified padding
plt.show()                                          # display the figure


# **** compute the HOG of the image (obtain finer features) ****
fd, hog_image = hog(monalisa,                       # image of interest
                    pixels_per_cell=(8, 8),         # was: (16, 16) - size (in pixels) of a cell
                    block_norm='L2-Hys',            # block normalization method
                    visualize=True,                 # visualize HOG descriptors on image
                    channel_axis=-1)                # axis of color channel in the image

# **** display the HOG of the image ****
fig, axes = plt.subplots(   1,
                            2, 
                            figsize=(10, 8), 
                            sharex=True, 
                            sharey=True)

# **** ****
ax = axes.ravel()                                   # flatten axes array

# **** ****
ax[0].imshow(monalisa, cmap='gray')                 # display image of interest
ax[0].set_title('Original image')                   # set the title for the image

# **** stretch or shrink the intensity levels of the 
#      image- results in a higher contrast image ****
hog_image_rescaled = exposure.rescale_intensity(hog_image,
                                                in_range=(0, 10))

# **** ****
ax[1].imshow(hog_image_rescaled, cmap='gray')       # display HOG of image
ax[1].set_title('HOG image')                        # set the title for the image

# **** ****
plt.tight_layout()                                  # adjust subplot parameters to give specified padding
plt.show()                                          # display the figure


# **** compute the HOG of the image (obtain coarser features) ****
fd, hog_image = hog(monalisa,                       # image of interest
                    pixels_per_cell=(32, 32),       # was: (16, 16) - size (in pixels) of a cell
                    block_norm='L2-Hys',            # block normalization method
                    visualize=True,                 # visualize HOG descriptors on image
                    channel_axis=-1)                # axis of color channel in the image

# **** display the HOG of the image ****
fig, axes = plt.subplots(   1,
                            2, 
                            figsize=(10, 8), 
                            sharex=True, 
                            sharey=True)

# **** ****
ax = axes.ravel()                                   # flatten axes array

# **** ****
ax[0].imshow(monalisa, cmap='gray')                 # display image of interest
ax[0].set_title('Original image')                   # set the title for the image

# **** stretch or shrink the intensity levels of the 
#      image- results in a higher contrast image ****
hog_image_rescaled = exposure.rescale_intensity(hog_image,
                                                in_range=(0, 10))

# **** ****
ax[1].imshow(hog_image_rescaled, cmap='gray')       # display HOG of image
ax[1].set_title('HOG image')                        # set the title for the image

# **** ****
plt.tight_layout()                                  # adjust subplot parameters to give specified padding
plt.show()                                          # display the figure
