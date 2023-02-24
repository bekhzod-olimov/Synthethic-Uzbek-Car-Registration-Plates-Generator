import os, random, math, cv2
import numpy as np
from PIL import Image
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

def get_random_int(*args): return args[0][int(np.random.randint(low=args[1], high=len(args[0]), size=args[2]))]

def get_label_and_plate(*args, **kwargs):
    
    plate_int = kwargs["li"][int(np.random.randint(low=0, high=len(kwargs["li"]), size=1))] if True else (int(kwargs["plate_chars"][kwargs["num"]]) if kwargs["tt"] else kwargs["plate_chars"][kwargs["num"]])
    kwargs["plate"][kwargs["row"]:kwargs["row"] + kwargs["num_size"][1], kwargs["col"]:kwargs["col"] + kwargs["num_size"][0], :] = cv2.resize(kwargs["num_ims"][str(plate_int)], kwargs["num_size"])
    
    return kwargs["plate"], kwargs["label"] + str(plate_int), kwargs["col"]   


def partial_write(plate, label, num_list, char_list, num_ims, char_ims, char_size, region_size, plate_chars, num_size, row, col, random, label_prefix):
    
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-6, tt=True)
        col += 55
        
    # number 4
    plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-5, tt=True)
    col += 50

    # number 5
    plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                            num_ims=num_ims, num_size=num_size, ran=random, num=-4, tt=True)
    
    if label_prefix in ["basic", "foreign_res", "foreign_comp", "diplomatic"]: col += 50 
    elif label_prefix == "state": col += num_size[0] + 30

    # number 6
    if label_prefix in ["foreign_res", "foreign_comp", "basic"]:
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-3, tt=True)
        if label_prefix == "basic": col += 70 
        elif label_prefix in ["foreign_res", "foreign_comp"]: col += 50 
        
        
    elif label_prefix == "state":
        
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=char_list, row=row, col=col, 
                                                num_ims=char_ims, num_size=char_size, ran=random, num=-3, tt=True)
        
        col += 60
    
    # character 7
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        if random:
            plate_int = get_random_int(num_list, 0, 1)
        else:
            plate_int = plate_chars[-2] if label_prefix == "foreign" else plate_chars[-3]
        label += str(plate_int)
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(num_ims[plate_int], char_size)
    
    else:
        
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=char_list, row=row, col=col, 
                                                num_ims=char_ims, num_size=char_size, ran=random, num=-2, tt=True)
        
    if label_prefix in ["basic", "state"]: col += 60 
    elif label_prefix in ["foreign_res", "foreign_comp","diplomatic"]: col += 55 
        
    # character 8
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        if random:
            plate_int = get_random_int(num_list, 0, 1)
        else:
            plate_int = plate_chars[-1] if label_prefix in ["foreign_res", "foreign_comp"] else plate_chars[-2]
        label += str(plate_int)
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(num_ims[plate_int], char_size)
    
    else:
        
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=char_list, row=row, col=col, 
                                                num_ims=char_ims, num_size=char_size, ran=random, num=-1, tt=True)
        col += 50
        
    if label_prefix == "diplomatic":
        col += 55
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-1, tt=True)
    
    return plate, label
    
def write(plate, label, num_list, num_ims, init_size, char_list, plate_chars, num_size, region_size, char_ims, char_size, label_prefix, row, col, random, regions):
    
    # number 1
    if label_prefix == "diplomatic":
        col += 25
    
    else:
        if random:
            random_region = regions[int(np.random.choice(np.arange(0, len(regions)), p=[0.12, 0.08, 0.04, 0.04, 0.1, 0.1, 0.08, 0.08, 0.08, 0.07, 0.08, 0.05, 0.0409999999999805, 0.03900000000001977]))]
            label += str(num_list[int(random_region[0])])
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[0])], (init_size[1], num_size[0]))
        else:
            plate_int = int(plate_chars[0])
            label += str(num_list[plate_int])
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
        col += 40

    # number 2
    if label_prefix == "diplomatic":
        col += 25
    else:
        if random:
            label += str(num_list[int(random_region[1])])
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[1])], (init_size[1], num_size[0]))
        else:
            plate_int = int(plate_chars[1])
            label += str(num_list[plate_int])
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
        col += 70
    
    # character 3
    row -= init_size[0] - 3 
    
    if label_prefix in ["foreign_res", "foreign_comp"]: col += 5
    if label_prefix in ["foreign_res", "foreign_comp", "basic", "diplomatic"]:

        if random:
            plate_int = get_random_int(char_list, 0, 1)
        else:
            plate_int = (plate_chars[-6]) if label_prefix == "basic" else ((plate_chars[-7]) if label_prefix in ["foreign_res", "foreign_comp"] else (plate_chars[0]))
        
        label += str(plate_int)
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
        if label_prefix == "basic": col += 70 
        elif label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]: col += 75

    elif label_prefix == "state":
        
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-6, tt=True)
        
        col += 50
        
    plate, label = partial_write(plate, label, num_list, char_list, num_ims, char_ims, char_size, region_size, plate_chars, num_size, row, col, random, label_prefix) 
        
    return plate, label

def save(**kwargs):
    
    if kwargs["transformations"]:
        
        plate = random_bright(kwargs["plate"])
        tfs = albumentations.Compose([Affine(rotate=[-7, 7], shear=None, p=0.5), Perspective(scale=(0.02, 0.1), p=0.1)])
        plate = tfs(image=plate)["image"]
    
    else: plate = kwargs["plate"]
    
    folder = kwargs["label"].split('__')[0]
    save_dir = os.path.join(kwargs["save_path"], folder)
    os.makedirs(save_dir, exist_ok = True)
    cv2.imwrite(os.path.join(save_dir, f"{kwargs['label'].split('__')[1]}__{folder}") + ".jpg", plate)
    # print(f"Plate {label.split('__')[1]}__{folder}.jpg is saved to {save_dir}/!")
    
def load(files_path):
    
    files_paths = sorted(os.listdir(files_path))
    ims, files = {}, [] 

    for char_path in files_paths:
        fname = os.path.splitext(char_path)[0]
        im = cv2.imread(os.path.join(files_path, char_path))
        ims[fname] = im
        files.append(char_path[0:-4])
        
    return ims, files

def preprocess(*args):
    
    plate = cv2.resize(cv2.imread(args[0]), args[1])
    label = f"{args[2]}__" 
    
    if args[2] in ["foreign_res"]: row, col = args[3][0] + 3, args[3][1] + 8
    else: row, col = args[3][0], args[3][1]
    
    return plate, label, row, col

def generate_plate(**kwargs):
    
    plate_chars = [char for char in kwargs["plate"]]
    
    plate, label, row, col = preprocess(kwargs["plate_path"], kwargs["plate_size"], kwargs["label_prefix"], kwargs["region_size"])
    
    plate, label = write(plate=plate, label=label, num_list=kwargs["num_list"], num_ims=kwargs["num_ims"], random=kwargs["random"], 
                         init_size=kwargs["init_size"], char_list=kwargs["char_list"], plate_chars=plate_chars,
                         char_ims=kwargs["char_ims"], char_size=kwargs["char_size"], region_size=kwargs["region_size"], regions=kwargs["regions"],
                         label_prefix=kwargs["label_prefix"], row=row, num_size=kwargs["num_size"], col=col)

    if kwargs["save_"]: save(plate=plate, save_path=kwargs["save_path"], transformations=kwargs["transformations"], label=label)
