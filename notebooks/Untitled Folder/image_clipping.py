from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
import os
import random
import pickle

imageFolder = "images"

image_dim = 1 

fac = 4 ### PARAMETER 1 - REDUCES THE RESOLUTION OF THE AERIAL IMAGE

imgs = {}

for fileName in ["aerial_2005.jpg", "y_2005.jpg", "y_2010.jpg"]:
    
    image_path = "/".join([imageFolder, fileName])
    
    ''' Basically what the imread method does is that it reads an image into a n-dimensional array,
    in our case it will be a three dimensional array where the dimensions have the following meaning:
    0 - the horizontal index of the pixel
    1 - the vertical index of the pixel
    3 - a tuple containing the RGB values of the pixel
    
    So, now your img variable holds a 3-dimensional array representation of the image.
    '''
    img = misc.imread(image_path)

    print "Image located at {} has shape {}".format(image_path,img.shape)
    print "The (100,100) pixel has RGB values {}".format(img[100][100])
    
    if image_dim == 1 and len(img.shape) > 2: 
        ''' This is converting your pixel value to only R scale instead of the RGB scale '''
        img = img[:,:,0]
        print "The (100,100) pixel has value {}".format(img[100][100])
    
    print "The current Shape of the image is {}".format(img.shape)
    img = misc.imresize(img, (img.shape[0]/fac, img.shape[1]/fac), interp='nearest')
    print "The new shape of the image is {}".format(img.shape)
    img = img / 255.0 
    print "The (100,100) pixel has value {}".format(img[100][100])
    imgs[fileName] = img

print "Load data complete"

import math

targetRes = 32  ### PARAMETER 2 - CONTROLS THE SIZE OF THE TRAINING IMAGES
stride = 2      ### PARAMETER 3 - CONTROLS THE NUMBER OF SAMPLES PRODUCED

img = imgs["aerial_2005.jpg"]
xStep = int( math.floor( ( float(img.shape[0]) - targetRes ) / stride) )
yStep = int( math.floor( ( float(img.shape[1]) - targetRes ) / stride) )

print "Shape[0] {} Shape[1] {} --- {}".format(img.shape[0],img.shape[1],( float(img.shape[0]) - targetRes ))

print xStep, yStep

data = []

for y in range(yStep):
    for x in range(xStep):
        sample = []
        
        crop = imgs["aerial_2005.jpg"][x * stride : (x * stride) + targetRes, y * stride : (y * stride) + targetRes]
        sample.append(crop)
        
        # This code calculates the change in urbanization based on two ground truth images
        
        p = []

        for layer in ["y_2005.jpg", "y_2010.jpg"]:
            target = imgs[layer][x * stride : (x * stride) + targetRes, y * stride : (y * stride) + targetRes]
            target_val = int ( round( np.mean(target) ) )
            p.append(target_val)
            
        if p[0] == 0: # not urbanized in y0
            if p[1] == 0: # not urbanized in y1
                sample.append(0)
            else: # urbanized in y1
                sample.append(1)
        else: # urbanized in y0
            if p[1] == 0: # not urbanized in y1
                sample.append(2)
            else: # urbanized in y1
                sample.append(3)
                     
        '''
         Sample[0] is images crop
         Sample[1] is crops label
         '''   
        data.append(sample)

count = 0
for element in data:
    print "Input Crop is {}".format(element[0].shape)
    print "Label is {}".format(element[1])
    count +=1
    if count % 10 == 0:
        break

# don't forget to shuffle!
random.shuffle(data)
        
print "num samples:", len(data)
