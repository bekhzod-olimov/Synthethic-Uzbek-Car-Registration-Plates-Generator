from plate_generator import PlateGenerator
import argparse, os
import pandas as pd
import numpy as np

def run(args):
    
    def split_and_generate(generator, sample, save, num):

        generator.generate(sample, args.save, num=num, plate_type=None, region=None)

    if args.random:
        generator = PlateGenerator(save_path=args.save_path, random=args.random)
        split_and_generate(generator=generator, sample=None, save=args.save, num=args.number_of_plates)    

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
    parser.add_argument("-s", "--save", help = "Saving option", type = bool, default = True)
    parser.add_argument("-np", "--number_of_plates", help = "Number of images to generate", type = int, default = 20)
    parser.add_argument("-r", "--random", help = "Generate random plate numbers", type = bool, default = True)
    
    
    args = parser.parse_args()
    run(args) 
    
    
    
    
# def split_and_generate(generator, sample, save, num):

#         for _ in range(num):
            
#             plate_types = ["basic", "state", "foreign_res", "foreign_comp", "diplomatic"]
#             random_int = int(np.random.randint(low=0, high=len(plate_types), size=1))
#             plate_type = plate_types[random_int]
#             print(f"Plate type: {plate_type}")
#             sample = "01227AAA" if plate_type == "state" else ("01A227AA" if plate_type == "basic" else ("01H012345" if plate_type == "foreign_res" else ("T012345" if plate_type == "diplomatic" else "01H012345")))
#             split_ = os.path.splitext(os.path.basename(sample))[0]
#             region = split_[:2]
#             generator.generate(sample, args.save, num=num, plate_type=plate_type, region=region)
