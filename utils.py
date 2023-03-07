# Import libraries
import os, random, math, cv2, albumentations
import numpy as np
from PIL import Image
import pandas as pd
from albumentations.augmentations.geometric.transforms import *

def random_bright(im):
    
    """
    
    This function gets an input image and applies random brightness.
    
    Argument:
    
        im - an input image, cv image.
        
    Output:
        
        an output image with applied random brightness.
    
    """
    
    im = np.array(cv2.cvtColor(im, cv2.COLOR_RGB2HSV), dtype=np.float64)
    random_bright = .5 + np.random.uniform()
    im[:, :, 2] = im[:, :, 2] * random_bright
    im[:, :, 2][im[:, :, 2] > 255] = 255
    
    return cv2.cvtColor(np.array(im, dtype=np.uint8), cv2.COLOR_HSV2RGB)

def get_random_int(*args): 
    
    """
    
    This function gets arguments and returns random instance of the list.
    
    Arguments:
    
        li   - pre-defined list;
        low  - low value for the list, int;
        high - high value for the list, int;
        size - number of instances to be returned, int.
    
    """
    
    return args[0][int(np.random.randint(low = args[1], high = len(args[0]), size = args[2]))]

def get_label_and_plate(*args, **kwargs):
    
    """
    
    This function gets arguments and keywork arguments and returns plate, label, and column value.
    
    Outputs:
    
        plate - a plate image, array;
        label - label for the plate, str;
        col   - column value, int.
    
    """
    
    plate_int = kwargs["li"][int(np.random.randint(low=0, high=len(kwargs["li"]), size=1))] if True else (int(kwargs["plate_chars"][kwargs["num"]]) if kwargs["tt"] else kwargs["plate_chars"][kwargs["num"]])
    kwargs["plate"][kwargs["row"]:kwargs["row"] + kwargs["num_size"][1], kwargs["col"]:kwargs["col"] + kwargs["num_size"][0], :] = cv2.resize(kwargs["num_ims"][str(plate_int)], kwargs["num_size"])
    
    return kwargs["plate"], kwargs["label"] + str(plate_int), kwargs["col"]   

def partial_write(plate, label, num_list, char_list, num_ims, char_ims, char_size, region_size, plate_chars, num_size, row, col, random, label_prefix):
    
    """
    
    This function gets arguments and does the second part of LP generation.
    
    Arguments:
    
        plate        - a plate image, array;
        label        - label for the LP, str;
        num_list     - digits for LP generation, list;
        char_list    - characters for LP generation, list;
        num_ims      - digit images for LP generation, dic;
        char_ims     - character images for LP generation, dic;
        char_size    - size of the characters, tuple;
        num_size     - size of the digits, tuple;
        region_size  - size of the regions, tuple;
        plate_chars  - characters for plate, list;
        row          - value of the row, int;
        col          - value of the column, int;
        random       - randomness option, bool;
        label_prefix - plate type, str.
    
    """
    
    # Get plate image, label string and column value
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        plate, label, col = get_label_and_plate(plate = plate, plate_chars = plate_chars, label = label, li = num_list, row = row, col = col, 
                                                num_ims = num_ims, num_size = num_size, ran = random, num = -6, tt = True)
        # Increase the column value
        col += 55
        
    # Digit #4
    # Get plate image, label string and column value
    plate, label, col = get_label_and_plate(plate = plate, plate_chars = plate_chars, label = label, li = num_list, row = row, col = col, 
                                                num_ims = num_ims, num_size = num_size, ran = random, num = -5, tt = True)
    # Increase the column value
    col += 50

    # Digit #5
    # Get plate image, label string and column value
    plate, label, col = get_label_and_plate(plate = plate, plate_chars = plate_chars, label = label, li = num_list, row = row, col = col, 
                                            num_ims = num_ims, num_size = num_size, ran = random, num = -4, tt = True)
    
    # Increase the column value
    if label_prefix in ["basic", "foreign_res", "foreign_comp", "diplomatic"]: col += 50 
    elif label_prefix == "state": col += num_size[0] + 30

    # Digit #6
    # Get plate image, label string and column value
    if label_prefix in ["foreign_res", "foreign_comp", "basic"]:
        plate, label, col = get_label_and_plate(plate = plate, plate_chars = plate_chars, label = label, li = num_list, row = row, col = col, 
                                                num_ims = num_ims, num_size = num_size, ran = random, num = -3, tt = True)
        # Increase the column value
        if label_prefix == "basic": col += 70 
        elif label_prefix in ["foreign_res", "foreign_comp"]: col += 50 
        
    elif label_prefix == "state":
        
        # Get plate image, label string and column value        
        plate, label, col = get_label_and_plate(plate = plate, plate_chars = plate_chars, label = label, li = char_list, row = row, col = col, 
                                                num_ims = char_ims, num_size = char_size, ran = random, num = -3, tt = True)

        # Increase the column value
        col += 60
    
    # Digit/Character #7
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        
        # Get plate integer
        if random: plate_int = get_random_int(num_list, 0, 1)
        else: plate_int = plate_chars[-2] if label_prefix == "foreign" else plate_chars[-3]
        
        # Add plate integer to the label
        label += str(plate_int)
        
        # Add digit image to the plate
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(num_ims[plate_int], char_size)
    
    # Get plate, label, and column value
    else: plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=char_list, row=row, col=col, 
                                                  num_ims=char_ims, num_size=char_size, ran=random, num=-2, tt=True)
        
    # Increase the column value
    if label_prefix in ["basic", "state"]: col += 60 
    elif label_prefix in ["foreign_res", "foreign_comp","diplomatic"]: col += 55 
        
    # Digit/Character #8
    if label_prefix in ["foreign_res", "foreign_comp", "diplomatic"]:
        
        # Get plate integer
        if random: plate_int = get_random_int(num_list, 0, 1)
        else: plate_int = plate_chars[-1] if label_prefix in ["foreign_res", "foreign_comp"] else plate_chars[-2]
            
        # Add plate integer to the label
        label += str(plate_int)
        
        # Add character image to the plate
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(num_ims[plate_int], char_size)
    
    # Get plate, label, and column value
    else: plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=char_list, row=row, col=col, 
                                                  num_ims=char_ims, num_size=char_size, ran=random, num=-1, tt=True)
        # Increase the column value
        col += 50
        
    if label_prefix == "diplomatic":
        
        # Increase the column value
        col += 55
        
        # Get plate, label, and column value
        plate, label, col = get_label_and_plate(plate=plate, plate_chars=plate_chars, label=label, li=num_list, row=row, col=col, 
                                                num_ims=num_ims, num_size=num_size, ran=random, num=-1, tt=True)
    
    return plate, label
    
def write(plate, label, num_list, num_ims, init_size, char_list, plate_chars, num_size, region_size, char_ims, char_size, label_prefix, row, col, random, regions):
    
    """
    
    This function gets arguments and does the first part of LP generation.
    
    Arguments:
    
        plate        - a plate image, array;
        label        - label for the LP, str;
        num_list     - digits for LP generation, list;
        num_ims      - digit images for LP generation, dic;
        init_size    - initial size for the plates, tuple;
        char_list    - characters for LP generation, list;
        plate_chars  - characters for plate, list;
        num_size     - size of the digits, tuple;
        region_size  - size of the regions, tuple;
        char_ims     - character images for LP generation, dic;
        char_size    - size of the characters, tuple;
        label_prefix - plate type, str
        row          - value of the row, int;
        col          - value of the column, int;
        random       - randomness option, bool;
        regions      - regions for LP, list.    
    
    """
    
    # Digit #1
    if label_prefix == "diplomatic": col += 25        
    # Not diplomatic plate type
    else:
        
        # Random case
        if random:
            
            # Get region
            random_region = regions[int(np.random.choice(np.arange(0, len(regions)), p=[0.12, 0.08, 0.04, 0.04, 0.1, 0.1, 0.08, 0.08, 0.08, 0.07, 0.08, 0.05, 0.0409999999999805, 0.03900000000001977]))]
            
            # Add to the label
            label += str(num_list[int(random_region[0])])
            
            # Draw region to the plate
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[0])], (init_size[1], num_size[0]))
        
        # Pre-defined case
        else:
            
            # Get plate digit
            plate_int = int(plate_chars[0])
            
            # Add to the label
            label += str(num_list[plate_int])
            
            # Draw region to the plate
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
        # Increase the column value
        col += 40

    # Digit #2
    if label_prefix == "diplomatic": col += 25        

    # Not diplomatic plate type
    else:
        
        # Random case
        if random:
            
            # Add to the label
            label += str(num_list[int(random_region[1])])
            
            # Draw digit to the plate
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(random_region[1])], (init_size[1], num_size[0]))
        
        # Pre-defined case
        else:
            
            # Get plate digit
            plate_int = int(plate_chars[1])
            
            # Add to the label
            label += str(num_list[plate_int])
            
            # Draw digit to the plate
            plate[row:row + num_size[0], col:col + init_size[1], :] = cv2.resize(num_ims[str(plate_int)], (init_size[1], num_size[0]))
        # Increase the column value
        col += 70
    
    # Character #3
    row -= init_size[0] - 3 
    
    if label_prefix in ["foreign_res", "foreign_comp"]: col += 5
    if label_prefix in ["foreign_res", "foreign_comp", "basic", "diplomatic"]:

        # Random case
        if random: plate_int = get_random_int(char_list, 0, 1)
        
        # Pre-defined case
        else: plate_int = (plate_chars[-6]) if label_prefix == "basic" else ((plate_chars[-7]) if label_prefix in ["foreign_res", "foreign_comp"] else (plate_chars[0]))
        
        # Add to the label
        label += str(plate_int)
        
        # Draw character to the plate
        plate[row:row + char_size[1], col:col + char_size[0], :] = cv2.resize(char_ims[plate_int], char_size)
        
        # Increase the column value
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
