# Import libraries
import argparse, os
import pandas as pd
import numpy as np
from plate_generator import PlateGenerator

def run(args):
    
    """
    
    This function gets arguments and runs the code.
    
    Arguments:
        
        args - parsed arguments, Namespace object.
    
    """
    
    # Initialize PlateGenerator instance based on the parsed arguments
    generator = PlateGenerator(save_path = args.save_path, random = args.random, transformations = args.transform)
    
    # Random LP Generation
    if args.random: generator.generate(save = args.save, num = args.number_of_plates, plate = None, plate_type = None, region = None)

    # Pre-defined LP Generation    
    else:
        df = open(args.data_path, 'r')
        for idx, text in enumerate(df):
            fname = os.path.splitext(os.path.basename(text))[0].split("__")
            im_name, im_type = fname[0], fname[1]
            generator.generate(im_name, args.save, num=1, plate_type=im_type, region=None)

if __name__ == "__main__":
    
    # Initialize Argument Parser
    parser = argparse.ArgumentParser(description="Synthetic Uzbek Car Registration Plates Generator")
    
    # Add arguments to the parser
    parser.add_argument("-dp", "--data_path", help = "Path to the csv file with plate numbers", type = str, default = "lp.txt")
    parser.add_argument("-sp", "--save_path", help = "Directory to save generated images", type = str, default = "./new_samples/test/")
    parser.add_argument("-s", "--save", help = "Saving option", type = bool, default = True)
    parser.add_argument("-np", "--number_of_plates", help = "Number of images to generate", type = int, default = 10)
    parser.add_argument("-r", "--random", help = "Generate random plate numbers", type = bool, default = False)
    parser.add_argument("-t", "--transform", help = "Apply transformations", type = bool, default = True)
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Run the code using the parsed arguments
    run(args)
