# -*- coding: utf-8 -*-
"""decrypt

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KcadjI7Uz6MhD15qTPEPhhP1dVxmNNk4
"""

import cv2
import numpy as np
from google.colab import files

def upload_image():
    """Uploads an encrypted image in Google Colab and returns its file path."""
    uploaded = files.upload()
    image_path = list(uploaded.keys())[0]  # Get the first uploaded file
    return image_path

def decrypt_image(image_path, correct_password):
    """Extracts the hidden message from an encrypted image."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read image.")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    decrypted_msg = ""

    password = input("Enter passcode for decryption: ")
    if password == correct_password:
        while True:
            char = c[img[n, m, z]]
            if char == "\0":  # Stop when a null character is detected
                break
            decrypted_msg += char
            n += 1
            m += 1
            z = (z + 1) % 3

        print("Decryption successful! Hidden Message:", decrypted_msg)
    else:
        print("YOU ARE NOT AUTHORIZED!")

if __name__ == "__main__":
    print("Please upload the encrypted image:")
    image_path = upload_image()  # Allow user to upload the encrypted image

    correct_password = input("Enter the correct passcode used for encryption: ")
    decrypt_image(image_path, correct_password)