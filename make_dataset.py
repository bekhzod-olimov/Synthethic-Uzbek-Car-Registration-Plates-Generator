# Import libraries
import os, cv2, argparse, shutil
import numpy as np
from glob import glob

# Initialize Arugment parser
parser = argparse.ArgumentParser('Make Dataset for CUT train')
# Add arguments to the parser
parser.add_argument('--in_im_paths', help = 'Input Images Path', type = str, default='/home/ubuntu/workspace/bekhzod/imagen/UzbekLicencePlateGenerator/new_samples/to_test_new')
parser.add_argument('--out_im_paths', help='Output Images Path', type = str, default='/home/ubuntu/workspace/bekhzod/imagen/lp_recognition_cropped/val')
parser.add_argument('--trainA', help = 'trainA Path', type = str, default='/home/ubuntu/workspace/bekhzod/cut/datasets/testing/trainA')
parser.add_argument('--trainB', help='trainB Path', type = str, default='/home/ubuntu/workspace/bekhzod/cut/datasets/testing/trainB')
parser.add_argument('--dataset_type', help='Make train or test dataset', type = str, default='train')
parser.add_argument('--num_imgs', dest='num_ims', help='number of images', type=int, default=1000000)

# Parse the arguments
args = parser.parse_args()

def copy_files(im_paths, destination): 
    
    """
    This function gets image paths and destination and copies the images to the destination.
    
    Arguments:
    
        im_paths    - paths to the images from domain A and B;
        destination - path to the directory to copy the images.
        
    Output:
        
        New directories with train and test images.
    
    """
    
    for file in im_paths:
        shutil.copy(file, destination)
        
def get_train_ims(ims_paths, im_files): return sorted(glob(f"{ims_paths}/*/*{[im_file for im_file in im_files]}"))
def get_test_ims(ims_paths, im_files): return sorted(glob(f"{ims_paths}/*{[im_file for im_file in im_files]}"))

for arg in vars(args):
    print('[%s] = ' % arg, getattr(args, arg))

# Initialize a list with proper image filetypes 
im_files = [".jpg", ".png", ".jpeg"]

# Get input image paths for train
input_im_paths = get_train_ims(args.in_im_paths, im_files)
print(f"There are {len(input_im_paths)} synthetic images!")

# Get input image paths for test
if args.dataset_type == "test": output_im_paths = get_train_ims(args.in_im_paths, im_files)
else: output_im_paths = get_test_ims(args.out_im_paths, im_files)
print(f"There are {len(output_im_paths)} original images!")

# Get number of images
num_ims = min(args.num_ims, len(input_im_paths))

# Create directories to copy the train and test images
os.makedirs(args.trainA, exist_ok=True)
os.makedirs(args.trainB, exist_ok=True)
print("Copying images...")

# Copy the images
copy_files(input_im_paths, args.trainA)
copy_files(output_im_paths, args.trainB)
print("Done!")
