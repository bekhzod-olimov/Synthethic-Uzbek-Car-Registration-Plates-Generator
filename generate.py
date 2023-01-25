import argparse, os
from plate_generator import PlateGenerator
import pandas as pd

def run(args):
    
    sample = "01227AAA"
    sample = "01A227AA"

    def split_and_generate(generator, sample, save, num):

        split_ = os.path.splitext(os.path.basename(sample))[0]
        region = split_[:2]
        generator.generate(sample, save=args.save, num=num, plate_type=None, region=region)

    if args.random:
        generator = PlateGenerator(save_path=args.save_path, random=args.random)
        split_and_generate(generator, sample=sample, save=args.save, num=args.number_of_plates)    

    else:
        df = pd.read_csv(args.data_path)
        texts = [os.path.basename(filename) for filename in df["filename"]]
        generator = PlateGenerator(save_path=args.save_path, random=args.random)    
        for sample in texts:
            split_and_generate(generator, sample=sample, save=args.save, num=1)    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Synthetic Plate Number Generator")
    
    parser.add_argument("-dp", "--data_path", help = "Path to the csv file with plate numbers", type = str, default = "uzbek.csv")
    parser.add_argument("-sp", "--save_path", help = "Directory to save generated images", type = str, default = "./new_samples/to_test_new/")
    parser.add_argument("-np", "--number_of_plates", help = "Number of images to generate", type = int, default = 3)
    parser.add_argument("-s", "--save", help = "Saving option", type = bool, default = True)
    parser.add_argument("-r", "--random", help = "Generate random plate numbers", type = bool, default = True)
    
    args = parser.parse_args()
    run(args) 
