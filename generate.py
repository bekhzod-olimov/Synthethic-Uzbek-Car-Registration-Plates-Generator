from plate_generator import PlateGenerator
import argparse, os
import pandas as pd

def run(args):
    
    def split_and_generate(generator, sample, save, num):

        split_ = os.path.splitext(os.path.basename(sample))[0]
        region = split_[:2]
        generator.generate(sample, args.save, num=num, plate_type=None, region=region)

    if args.random:
        generator = PlateGenerator(save_path=args.save_path, random=args.random)
        split_and_generate(generator, args.sample, args.save, args.number_of_plates)    

    else:
        df = pd.read_csv(args.data_path)
        texts = [os.path.basename(filename) for filename in df["filename"]]
        generator = PlateGenerator(save_path=args.save_path, random=args.random)    
        
        for text in texts:
            split_and_generate(generator, text, args.save, 1)    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Synthetic Plate Number Generator")
    
    parser.add_argument("-dp", "--data_path", help = "Path to the csv file with plate numbers", type = str, default = "uzbek.csv")
    parser.add_argument("-sp", "--save_path", help = "Directory to save generated images", type = str, default = "./new_samples/to_test_new/")
    parser.add_argument("-np", "--number_of_plates", help = "Number of images to generate", type = int, default = 3)
    parser.add_argument("-s", "--save", help = "Saving option", type = bool, default = True)
    parser.add_argument("-r", "--random", help = "Generate random plate numbers", type = bool, default = True)
    # parser.add_argument("-sl", "--sample", help = "Sample plate number to distinguish basic, state, foreign plate numbers", type = str, default = "01227AAA")
    # parser.add_argument("-sl", "--sample", help = "Sample plate number to distinguish basic, state, foreign plate numbers", type = str, default = "01A227AA")
    parser.add_argument("-sl", "--sample", help = "Sample plate number to distinguish basic, state, foreign plate numbers", type = str, default = "01H012345")
    
    args = parser.parse_args()
    run(args) 
