# Splitting NIR and RGB images into separate folders
# import os
# import shutil

# # Đường dẫn folder chứa ảnh gốc
# src_dir = "water"

# # Folder output
# nir_dir = os.path.join(src_dir, "nir")
# rgb_dir = os.path.join(src_dir, "rgb")

# os.makedirs(nir_dir, exist_ok=True)
# os.makedirs(rgb_dir, exist_ok=True)

# for filename in os.listdir(src_dir):
#     if not filename.lower().endswith(".tiff"):
#         continue

#     src_path = os.path.join(src_dir, filename)

#     if "_nir" in filename.lower():
#         shutil.copy(src_path, os.path.join(nir_dir, filename))

#     elif "_rgb" in filename.lower():
#         shutil.copy(src_path, os.path.join(rgb_dir, filename))

# print("Done splitting NIR and RGB!")
import cv2
import numpy as np
import os

def generate_low_light(
    img_rgb,
    gamma_range=(2.8, 4.0),
    alpha_range=(0.2, 0.5)
):
    """
    img_rgb: uint8 RGB image [0,255]
    return: uint8 low-light RGB
    """
    img = img_rgb.astype(np.float32) / 255.0

    gamma = np.random.uniform(*gamma_range)
    alpha = np.random.uniform(*alpha_range)

    low = alpha * np.power(img, gamma)
    low = np.clip(low, 0, 1)

    return (low * 255).astype(np.uint8)
# Input (folder containing RGB images)
rgb_dir = "water/rgb"
out_dir = "water/low_rgb"
os.makedirs(out_dir, exist_ok=True)

for fname in os.listdir(rgb_dir):
    if not fname.endswith(".tiff"):
        continue

    img = cv2.imread(os.path.join(rgb_dir, fname))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    low_img = generate_low_light(img)

    low_img = cv2.cvtColor(low_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(out_dir, fname), low_img)
# print("Done generating low-light RGB images!")
