import pandas as pd 
import numpy as np 
import cv2
import matplotlib.pyplot as plt 

def generation_images(path_df):
    df = pd.read_csv(path_df)
    list_1 = []
    for img in df['names']:
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        factor_escala = 720 / image.shape[0]
        image = cv2.resize(image, (int(image.shape[1]*factor_escala), 720))
        list_1.append(image)
    labels = df['labels']
    return list_1, labels

images, labels = generation_images('./df_1')
resolution = (images[0].shape[1], images[0].shape[0])
# print(resolution)


