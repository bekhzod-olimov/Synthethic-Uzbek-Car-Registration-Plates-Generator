import os, random, math
import cv2
import numpy as np
import pandas as pd
from albumentations.augmentations.geometric.transforms import *
import albumentations

def random_bright(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    img = np.array(img, dtype=np.float64)
    random_bright = .5 + np.random.uniform()
    img[:, :, 2] = img[:, :, 2] * random_bright
    img[:, :, 2][img[:, :, 2] > 255] = 255
    img = np.array(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    
    return img

def partial_write(Plate, label, num_list, char_list, num_ims, char_ims, char_size, region_size, plate_chars, num_size, row, col, random, label_prefix):
    
    # number 4
    if random:
        plate_int = int(np.random.randint(low=0, high=9, size=1))
        label += str(num_list[plate_int])
        Plate[row:row + num_size[1], col:col + num_size[0], :] = cv2.resize(num_ims[str(plate_int)], num_size)
    else:
        plate_int = int(plate_chars[-5])
        label += str(num_list[plate_int])
        Plate[row:row + num_size[1], col:col + num_size[0], :] = cv2.resize(num_ims[str(plate_int)], num_size)
        
    col += 50

    # number 5
    if random:
        plate_int = int(np.random.randint(low=0, high=9, size=1))
    else:
        plate_int = int(plate_chars[-4])
        
    label += str(num_list[plate_int])
    Plate[row:row + num_size[1], col:col + num_size[0], :] = cv2.resize(num_ims[str(plate_int)], num_size)
    
    if label_prefix == "long": col += 50 
    elif label_prefix == "state": col += num_size[0] + 30

    # number 6
    if label_prefix == "short" or label_prefix == "long":
        
        if random:
            plate_int = int(np.random.randint(low=0, high=9, size=1))
        else:
            plate_int = int(plate_chars[-3])

        label += str(num_list[plate_int])
        Plate[row:row + num_size[1], col:col + num_size[0], :] = cv2.resize(num_ims[str(plate_int)], num_size)
        col += 70
    
    elif label_prefix == "state":
        
        if random:
            plate_int = int(np.random.randint(low=0, high=9, size=1))
            plate_int = char_list[plate_int]
        else:
            plate_int = (plate_chars[-3])
            
        label += str(plate_int)
        Plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
        col += 60
    
    # character 7
    if random:
        plate_int = int(np.random.randint(low=0, high=9, size=1))
        plate_int = char_list[plate_int]
    else:
        plate_int = (plate_chars[-2])

    label += str(plate_int)
    Plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
    if label_prefix == "long": col += char_size[0] 
    elif label_prefix == "state": col += 60 
        
    # character 8
    if random:
        plate_int = int(np.random.randint(low=0, high=9, size=1))
        plate_int = char_list[plate_int]
    else:
        plate_int = (plate_chars[-1])

    label += str(plate_int)
    Plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
    if label_prefix == "short":
        col += (char_size[0] + init_size[1])
    else:
        col += (char_size[0] + region_size[0]) 
    
    return Plate, label
    
def write(Plate, label, num_list, num_ims, init_size, char_list, plate_chars, num_size, region_size, char_ims, char_size, label_prefix, row, col, random, regions):
    
    # number 1
    if random:
        plate_int = int(np.random.randint(low=0, high=len(regions), size=1))
        random_region = regions[plate_int]
        label += str(num_list[int(random_region[0])])
        Plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[0])], (init_size[1], num_size[0]))
    
    else:
        plate_int = int(plate_chars[0])
        label += str(num_list[plate_int])
        Plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
    col += 42

    # number 2
    if random:
        label += str(num_list[int(random_region[1])])
        Plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[1])], (init_size[1], num_size[0]))
    else:
        plate_int = int(plate_chars[1])
        label += str(num_list[plate_int])
        Plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
    col += 70
    
    # character 3
    row -= init_size[0] - 3 
    if label_prefix == "short" or label_prefix == "long":

        if random:
            plate_int = int(np.random.randint(low=0, high=9, size=1))
            plate_int = char_list[plate_int]
        else:
            plate_int = (plate_chars[-6])
        
        label += str(plate_int)
        Plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
        col += 70 

    elif label_prefix == "state":
        
        if random:
            plate_int = int(np.random.randint(low=0, high=9, size=1))
        else:
            plate_int = (plate_chars[-6])
        
        label += str(num_list[plate_int])
        Plate[row:row + num_size[1], col:col + num_size[0], :] = cv2.resize(num_ims[str(plate_int)], num_size)
        col += 50 
        
    Plate, label = partial_write(Plate, label, num_list, char_list, num_ims, char_ims, char_size, region_size, plate_chars, num_size, row, col, random, label_prefix) # maybe here?
        
    return Plate, label

def save(Plate, save_path, transformations, label):
    
    if transformations:
        Plate = random_bright(Plate)
        tfs = albumentations.Compose([Affine(rotate=[-7, 7], shear=None, p=0.5),
                         Perspective(scale=(0.05, 0.12), p=0.5)])
        Plate = tfs(image=Plate)["image"]
    
    folder = label.split('_')[0]
    save_dir = os.path.join(save_path, folder)
    os.makedirs(save_dir, exist_ok = True)
    cv2.imwrite(os.path.join(save_dir, f"{label.split('_')[1]}") + ".jpg", Plate)
    print(f"Plate {label.split('_')[1]}.jpg is saved to {save_dir}/!")

def load(files_path):
    
    chars_paths = sorted(os.listdir(files_path))
    ims, chars = {}, [] 

    for char_path in chars_paths:
        fname = os.path.splitext(char_path)[0]
        im = cv2.imread(os.path.join(files_path, char_path))
        ims[fname] = im
        chars.append(char_path[0:-4])
        
    return ims, chars

def preprocess(plate_path, plate_size, label_prefix, region_size, plate_chars):
    
    Plate = cv2.resize(cv2.imread(plate_path), plate_size)
    label = f"{label_prefix}_" 
    row, col = region_size[0], region_size[1]
    
    return Plate, label, row, col

def generate_plate(plate_path, plate, plate_size, num_size, random,
                   char_size, init_size, num_list, char_list, num_ims, char_ims, 
                   regions, region, region_size, save_path, label_prefix, save_):
    
    plate_chars = [char for char in plate]
    
    Plate, label, row, col = preprocess(plate_path, plate_size, label_prefix, region_size, plate_chars)
    
    Plate, label = write(Plate=Plate, label=label, num_list=num_list, num_ims=num_ims, random=random, 
                         init_size=init_size, plate_chars=plate_chars, char_list=char_list,
                         char_ims=char_ims, char_size=char_size, region_size=region_size, regions=regions,
                         label_prefix=label_prefix, row=row, num_size=num_size, col=col)

    if save_: save(Plate=Plate, save_path=save_path, transformations=False, label=label)
