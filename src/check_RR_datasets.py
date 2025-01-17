import os
import sys
import shutil
import numpy as np

root_videos_dir =  "/mnt2/FaceForensics/Train/videos/"
root_masks_dir = "/mnt2/FaceForensics/Train/masks_RR/"
root_frontal_dir = "/mnt2/FaceForensics/Train/frontal/"

count = 0
for id in os.listdir(root_frontal_dir):
    id_frontal_dir = os.path.join(root_frontal_dir, id)
    id_masks_dir = os.path.join(root_masks_dir, id)
    frontal_lst = os.listdir(id_frontal_dir)
    masks_lst = os.listdir(id_masks_dir)

    if len(frontal_lst) < 150 or len(masks_lst) <150:
        shutil.rmtree(id_frontal_dir, ignore_errors=True)
        shutil.rmtree(id_masks_dir, ignore_errors=True)
        continue

    if frontal_lst == [] or masks_lst == []:
        os.rmdir(id_frontal_dir)
        os.rmdir(id_masks_dir)
        print("Empty folder before check")
    for filename in frontal_lst:
        if not filename in masks_lst:
            os.remove(os.path.join(root_frontal_dir, id, filename))
            os.remove(os.path.join(root_masks_dir, id, filename))
            continue

    for filename in masks_lst:
        if not filename in frontal_lst:
            os.remove(os.path.join(root_frontal_dir, id, filename))
            os.remove(os.path.join(root_masks_dir, id, filename))

    frontal_lst = os.listdir(id_frontal_dir)
    masks_lst = os.listdir(id_masks_dir)
    if frontal_lst == [] or masks_lst == []:
        os.rmdir(id_frontal_dir)
        os.rmdir(id_masks_dir)
        print("Empty folder after check")
    count += 1
    print(id_frontal_dir, ': ', len(frontal_lst))
    print(id_masks_dir, ': ', len(masks_lst))

print('check folders:', count)
