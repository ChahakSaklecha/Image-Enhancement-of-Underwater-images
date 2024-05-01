# -*- coding: utf-8 -*-
"""clahe.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1avXrnP8OfcuFvsNDaEIoQ9uAA0whPgwx
"""

import cv2
import os
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

def apply_clahe(image_path, clip_limit=100.0, tile_grid_size=(256, 256)):
    # Read image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Create CLAHE object
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)

    # Apply CLAHE
    enhanced_image = clahe.apply(image)

    return enhanced_image

def apply_clahe_to_dataset(dataset_path, output_path, clip_limit=2.0, tile_grid_size=(4, 4)):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # List all image files in the dataset directory
    image_files = [f for f in os.listdir(dataset_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif'))]

    # Apply CLAHE to each image and save the enhanced image
    for image_file in image_files:
        image_path = os.path.join(dataset_path, image_file)
        enhanced_image = apply_clahe(image_path, clip_limit, tile_grid_size)
        output_image_path = os.path.join(output_path, image_file)
        cv2.imwrite(output_image_path, enhanced_image)

dataset_path = '/content/drive/MyDrive/BTP_CR=M1/output/restored_rgb_images'
output_path = '/content/drive/MyDrive/BTP_CR=M1/output/clahe_equilized'
apply_clahe_to_dataset(dataset_path, output_path)

