from utils import *

class PlateGenerator:
    
    def __init__(self, save_path, random):
        
        self.save_path = save_path
        self.random = random

        # Digits and characters
        self.num_ims, self.num_lists = load("./digits_uzbek/")
        self.char_ims, self.char_lists = load("./characters_uzbek/")
        
    def assertion(self, region_name, region_names):
        
        assert region_name != None, "Please insert a region name"
        assert region_name in [os.path.basename(region) for region in region_names], f"Please choose one of these regions: {[os.path.basename(region) for region in region_names]}"
        
    
    def generate(self, plate, save, plate_type, region_name):
        
        if plate_type == "long":
                    generate_plate(plate_path="plates/plate_uzbek.jpg", random=self.random,
                               plate=plate, num_size=(56, 78), num_size_2=None, 
                               num_list=self.num_lists, init_size=(13, 46), # start from left to right
                               char_list=self.char_lists, regions=None, three_digit = None,
                               num_ims=self.num_ims, char_size=(60, 78), region_name=None, # width 60, height 83 
                               char_ims=self.char_ims, label_prefix=plate_type,
                               save_path=self.save_path, region_size=(25, 30), all_regions=None,
                                   # all_regions=self.regions_lists_yellow,
                               save_=save, plate_size=(600, 110))
        
    def generation(self, plate, save, plate_type, num=None, region_name=None):
        
        assert plate_type in ["short", "long", "yellow", "old", "green"], "Please choose the correct the plate type"
        
        if num != None:
            for i in range(num):
                self.generate(plate=plate, save=save, plate_type=plate_type, region_name=region_name)
        else:
            self.generate(plate=plate, save=save, plate_type=plate_type, region_name=region_name)
