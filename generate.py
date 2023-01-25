import argparse, os
from plate_generator import PlateGenerator
import pandas as pd

    
parser = argparse.ArgumentParser()
parser.add_argument("-dp", "--data_path", help="Path to the csv file",
                    type=str, default="test.csv")
parser.add_argument("-sp", "--save_path", help="save image directory",
                    type=str, default="./new_samples/to_test_new/")
parser.add_argument("-np", "--number_of_plates", help="number of image",
                    type=int, default=2)
parser.add_argument("-s", "--save", help="save or imshow",
                    type=bool, default=True)
parser.add_argument("-r", "--random", help="Random plate numbers",
                    type=bool, default=True)

args = parser.parse_args()
save_path = args.save_path
data_path = args.data_path
random = args.random
number_of_plates = args.number_of_plates
Save = args.save
sample = "01227AAA"

def split_and_generate(generator, sample, save, num):
    
    split_ = os.path.splitext(os.path.basename(sample))[0]
    region = split_[:2]
    generator.generate(sample, save=Save, num=num, plate_type=None, region=region)

if random:
    generator = PlateGenerator(save_path=save_path, random=random)
    split_and_generate(generator, sample=sample, save=Save, num=number_of_plates)    

else:
    df = pd.read_csv("uzbek.csv")
    texts = [os.path.basename(filename) for filename in df["filename"]]
    generator = PlateGenerator(save_path=save_path, random=random)    
    for sample in texts:
        split_and_generate(generator, sample=sample, save=Save, num=1)    
