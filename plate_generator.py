from utils import *

class PlateGenerator:
    
    def __init__(self, save_path, random):
        
        self.save_path = save_path
        self.random = random

        # Basic nums and chars
        self.num_ims, self.num_lists = load("./digits_uzbek/")
        self.char_ims, self.char_lists = load("./characters_uzbek/")
        self.regions = {"01": "Tashkent", "10": "Tashkent Region", "20": "Sirdaryo", "25": "Jizzakh", "30": "Samarqand", "40": "Fergana", "50": "Namangan", "60": "Andijan", "70": "Qashqadaryo", "75": "Surxondaryo", "80": "Bukhara", "85": "Navoiy", "90": "Xorazm", "95": "Karakalpakstan"}
        
    def assertion(self, region, regions):
        
        assert region != None, f"Please insert a region name!"
        assert region in [os.path.basename(region) for region in regions], f"Please choose one region based on these information: {self.regions}"
        
    def generate(self, plate, save, plate_type, num, region):
        
        for _ in range(num):
            
            if plate[-3:].isalpha(): plate_type = "state"
            elif plate[2].isdigit(): plate_type = "long"
            
            self.assertion(region, self.regions)
            generate_plate(plate_path="plates/plate_uzbek.jpg", random=self.random,
                       plate=plate, num_size=(55, 78),
                       num_list=self.num_lists, init_size=(13, 45), 
                       char_list=self.char_lists, regions=list(self.regions.keys()),
                       num_ims=self.num_ims, char_size=(60, 78), region=region, 
                       char_ims=self.char_ims, label_prefix=plate_type,
                       save_path=self.save_path, region_size=(25, 30),
                       save_=save, plate_size=(600, 110))
