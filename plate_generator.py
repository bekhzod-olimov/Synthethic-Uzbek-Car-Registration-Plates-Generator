# Import functions from utils 
from utils import *

class PlateGenerator:
    
    """
    
    This class gets path to save generated lps, random option, and transformations option and generates lps.
    
    Arguments:
    
        save_path - path to save generated images, str;
        random - randomness option, bool;
        transformations - transformations option, bool;
    
    """
    
    def __init__(self, save_path, random, transformations):
        
        self.save_path, self.random, self.transformations = save_path, random, transformations

        # Get digits and characters with white background
        self.num_ims, self.num_lists = load("./digits/digits_white/")
        self.char_ims, self.char_lists = load("./letters/letters_white/")
        
        # Get digits and characters with yellow background
        self.num_ims_yellow, self.num_lists_yellow = load("./digits/digits_yellow/")
        self.char_ims_yellow, self.char_lists_yellow = load("./letters/letters_yellow/")
        
        # Get digits and characters with green background
        self.num_ims_green, self.num_lists_green = load("./digits/digits_green/")
        self.char_ims_green, self.char_lists_green = load("./letters/letters_green/")
        
        # Initialize a dictionary with region numbers as keys and region names as values
        self.regions = {"01": "Tashkent", "10": "Tashkent Region", "20": "Sirdaryo", "25": "Jizzakh", "30": "Samarqand", "40": "Fergana", "50": "Namangan", "60": "Andijan", "70": "Qashqadaryo", "75": "Surxondaryo", "80": "Bukhara", "85": "Navoiy", "90": "Xorazm", "95": "Karakalpakstan"}
        
        # Initialize a list with lp types
        self.plate_types = ["basic", "state", "foreign_res", "foreign_comp", "diplomatic"]
        
    def assert_(self, *args):
        
        """

        This function asserts that given region name is in the region names list.
        
        Argument:
            
            region_name - name of the specific region;
            regions - regions list.
        
        """
        
        assert args[0] != None, f"Please insert a region name!"
        if args[0][0].isalpha() and args[0][1].isdigit(): pass
        else: assert args[0] in [os.path.basename(region) for region in args[1]], f"Please choose one region based on these information: {args[1]}"
        
    def get_plate_type(self, plate):
        
        """
        
        This function gets plate and return type of the lp.
        
        Argument:
            
            plate - license plate.
            
        Output:
        
            plate type.
        
        """
        
        if plate[0].isalpha(): return "diplomatic"
        elif plate[-1].isdigit(): return "foreign_res"
        elif plate[2].isalpha(): return "basic"
        elif plate[-3:].isalpha(): return "state"            
        
    def generate(self, plate, save, plate_type, num, region):
        
        for _ in range(num):
            
            if self.random:
                plate_type = self.plate_types[int(np.random.choice(np.arange(0, len(self.plate_types)), p=[0.4, 0.23, 0.15, 0.11, 0.11]))]
                plate = "01227AAA" if plate_type == "state" else ("01A227AA" if plate_type == "basic" else ("01H012345" if plate_type == "foreign_res" else ("T012345" if plate_type == "diplomatic" else "01H012345")))
            
            else: plate_type = self.get_plate_type(plate)
            # else: plate_type = plate_type
            
            print(f"Plate type: {plate_type}")
            plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_basic.jpg", self.num_lists, self.char_lists, self.num_ims, self.char_ims
            if plate_type == "diplomatic": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_diplomatic.jpg", self.num_lists_green, self.char_lists_green, self.num_ims_green, self.char_ims_green
            elif plate_type == "foreign_res": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_yellow.jpg", self.num_lists_yellow, self.char_lists_yellow, self.num_ims_yellow, self.char_ims_yellow
            elif plate_type == "foreign_comp": plate_path, num_list, char_list, num_ims, char_ims = "plates/plate_green.jpg", self.num_lists_green, self.char_lists_green, self.num_ims_green, self.char_ims_green

            # print(f"Plate type: {plate_type}")
            region = os.path.splitext(os.path.basename(plate))[0][:2]
            self.assert_(region, self.regions)
            generate_plate(plate_path=plate_path, random=self.random,
                       plate=plate, num_size=(55, 78), transformations=self.transformations,
                       num_list=num_list, init_size=(13, 45), 
                       char_list=char_list, regions=list(self.regions.keys()),
                       num_ims=num_ims, char_size=(60, 78), region=region, 
                       char_ims=char_ims, label_prefix=plate_type,
                       save_path=self.save_path, region_size=(25, 25),
                       save_=save, plate_size=(575, 110))

