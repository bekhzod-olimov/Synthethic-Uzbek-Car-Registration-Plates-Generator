from utils import *

class PlateGenerator:
    
    def __init__(self, save_path, random):
        
        self.save_path = save_path
        self.random = random

        self.num_ims, self.num_lists = load("./digits/")
        self.char_ims, self.char_lists = load("./characters/")
        
        self.num_ims_yellow, self.num_lists_yellow = load("./digits_yellow/")
        self.char_ims_yellow, self.char_lists_yellow = load("./characters_yellow/")
        
        self.num_ims_green, self.num_lists_green = load("./digits_green/")
        self.char_ims_green, self.char_lists_green = load("./characters_green/")
        
        self.regions = {"01": "Tashkent", "10": "Tashkent Region", "20": "Sirdaryo", "25": "Jizzakh", "30": "Samarqand", "40": "Fergana", "50": "Namangan", "60": "Andijan", "70": "Qashqadaryo", "75": "Surxondaryo", "80": "Bukhara", "85": "Navoiy", "90": "Xorazm", "95": "Karakalpakstan"}
        
    def assertion(self, region, regions):
        
        assert region != None, f"Please insert a region name!"
        
        if region[0].isalpha() and region[1].isdigit(): pass
        else: assert region in [os.path.basename(region) for region in regions], f"Please choose one region based on these information: {self.regions}"
        
    def get_plate_type(self, plate):
        
        if plate[0].isalpha(): return "diplomatic"
        elif plate[-1].isdigit(): return "foreign_res"
        elif plate[2].isalpha(): return "basic"
        elif plate[-3:].isalpha(): return "state"            
        
    def generate(self, plate, save, plate_type, num, region):
        
        plate_types = ["basic", "state", "foreign_res", "foreign_comp", "diplomatic"]
        
        for _ in range(num):
            
            if self.random:
                plate_type = plate_types[int(np.random.choice(np.arange(0, len(plate_types)), p=[0.4, 0.23, 0.15, 0.11, 0.11]))]
                plate = "01227AAA" if plate_type == "state" else ("01A227AA" if plate_type == "basic" else ("01H012345" if plate_type == "foreign_res" else ("T012345" if plate_type == "diplomatic" else "01H012345")))
            
            else: plate_type = self.get_plate_type(plate)
            
            plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_basic.jpg", self.num_lists, self.char_lists, self.num_ims, self.char_ims
            if plate_type == "diplomatic": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_diplomatic.jpg", self.num_lists_green, self.char_lists_green, self.num_ims_green, self.char_ims_green
            elif plate_type == "foreign_res": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_yellow.jpg", self.num_lists_yellow, self.char_lists_yellow, self.num_ims_yellow, self.char_ims_yellow
            elif plate_type == "foreign_comp": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_green.jpg", self.num_lists_green, self.char_lists_green, self.num_ims_green, self.char_ims_green

            print(f"Plate type: {plate_type}")
            region = os.path.splitext(os.path.basename(plate))[0][:2]
            self.assertion(region, self.regions)
            generate_plate(plate_path=plate_path, random=self.random,
                       plate=plate, num_size=(55, 78),
                       num_list=num_list, init_size=(13, 45), 
                       char_list=char_list, regions=list(self.regions.keys()),
                       num_ims=num_ims, char_size=(60, 78), region=region, 
                       char_ims=char_ims, label_prefix=plate_type,
                       save_path=self.save_path, region_size=(25, 25),
                       save_=save, plate_size=(575, 110))

