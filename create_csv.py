#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!pip install misc


# In[14]:


get_ipython().system('pip install imread')


# In[10]:


get_ipython().system('pip install pillow')


# In[17]:


get_ipython().system('pip install scipy==1.4.1')


# In[29]:


#from scipy.misc import imread
#from pilutil import *
#from scipy.misc import imread
#from scipy.misc.pilutil 
# import numpy as np
# import cv2
# import os

# IMG_DIR = '/home/rupeek/gestures'

# for img in os.listdir(IMG_DIR):
#         img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)
        
#import imread
#from PIL import Image
import cv2


import numpy as np
import pandas as pd
import os
root = './gestures' # or ‘./test’ depending on for which the CSV is being created

# go through each directory in the root folder given above
for directory, subdirectories, files in os.walk(root):
# go through each file in that directory
    for file in files:
    # read the image file and extract its pixels
        print(file)
        im = cv2.imread(os.path.join(directory,file))
        value = im.flatten()
# I renamed the folders containing digits to the contained digit itself. For example, digit_0 folder was renamed to 0.
# so taking the 9th value of the folder gave the digit (i.e. "./train/8" ==> 9th value is 8), which was inserted into the first column of the dataset.
        value = np.hstack((directory[8:],value))
        df = pd.DataFrame(value).T
        df = df.sample(frac=1) # shuffle the dataset
        with open('train_foo.csv', 'a') as dataset:
            df.to_csv(dataset, header=False, index=False)


# In[ ]:




