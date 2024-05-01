# -*- coding: utf-8 -*-
"""btp_cr.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X3uHrGM1Q-mdg5sb7JxZKjlL8Oc2goVk
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install opencv-python

import cv2

import os

from google.colab.patches import cv2_imshow

import numpy as np

def rgb_to_lab(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB).astype(np.uint8)
    return lab_image

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            rgb_image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

            # Convert to LAB color space
            lab_image = rgb_to_lab(rgb_image)

            # Save the LAB image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, lab_image)

            # Display the original and converted images (optional)
            cv2_imshow(rgb_image)
            cv2_imshow(lab_image)

input_folder = '/content/drive/MyDrive/BTP_CR=M1/lrd'
output_folder = '/content/drive/MyDrive/BTP_CR=M1/output/lab_images'

process_images(input_folder, output_folder)

def cie_color_restoration(lab_image):
    # Calculate the median values of channels a and b
    Ma = np.median(lab_image[:, :, 1])
    Mb = np.median(lab_image[:, :, 2])

    # Calculate offsets
    offset1 = 128 - Ma
    offset2 = 128 - Mb

    # Update values of a and b in the LAB image
    lab_image[:, :, 1] = np.clip(lab_image[:, :, 1].astype(np.float64) + offset1, 0, 255).astype(np.uint8)
    lab_image[:, :, 2] = np.clip(lab_image[:, :, 2].astype(np.float64) + offset2, 0, 255).astype(np.uint8)

    return lab_image

def lab_to_rgb(lab_image):
    rgb_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2RGB)
    return rgb_image

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create a separate folder for restored LAB images
    restored_lab_folder = os.path.join(output_folder, 'restored_lab_images')
    if not os.path.exists(restored_lab_folder):
        os.makedirs(restored_lab_folder)

    # Create a separate folder for restored RGB images
    restored_rgb_folder = os.path.join(output_folder, 'restored_rgb_images')
    if not os.path.exists(restored_rgb_folder):
        os.makedirs(restored_rgb_folder)

    # Iterate through each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            rgb_image = cv2.imread(image_path)
            rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

            # Convert to LAB color space
            lab_image = rgb_to_lab(rgb_image)

            # CIE color restoration
            restored_lab_image = cie_color_restoration(lab_image)

            # Save the restored LAB image to a separate folder
            output_path_lab = os.path.join(restored_lab_folder, filename)
            cv2.imwrite(output_path_lab, restored_lab_image)

            # Convert restored LAB image back to RGB (for display purposes)
            restored_rgb_image = lab_to_rgb(restored_lab_image)

            # Save the restored RGB image to a separate folder
            output_path_rgb = os.path.join(restored_rgb_folder, filename)
            cv2.imwrite(output_path_rgb, restored_rgb_image)

            # Display the original, LAB, and restored RGB images (optional)
            cv2_imshow(rgb_image)
            cv2_imshow(restored_rgb_image)

input_folder = '/content/drive/MyDrive/BTP_CR=M1/lrd'
output_folder = '/content/drive/MyDrive/BTP_CR=M1/output'

process_images(input_folder, output_folder)

