from utils import *

class PlateGenerator:
    
    def __init__(self, save_path, random):
        
        self.save_path = save_path
        self.random = random

        # Basic nums and chars
        # self.num_ims, self.num_lists = load("./digits/")
        self.num_ims, self.num_lists = load("./digits_uzbek/")
        self.char_ims, self.char_lists = load("./characters_uzbek/")

        
    def assertion(self, region_name, region_names):
        
        assert region_name != None, "Please insert a region name"
        assert region_name in [os.path.basename(region) for region in region_names], f"Please choose one of these regions: {[os.path.basename(region) for region in region_names]}"
        
    
    def generate(self, plate, save, plate_type, region_name):
        
        # if plate_type == "long":
        #             generate_plate(plate_path="plates/plate.jpg", random=self.random,
        #                        plate=plate, num_size=(56, 83), num_size_2=None, 
        #                        num_list=self.num_lists, init_size=(13, 36), # start from left to right
        #                        char_list=self.char_lists, regions=None, three_digit = None,
        #                        num_ims=self.num_ims, char_size=(60, 83), region_name=None,
        #                        char_ims=self.char_ims, label_prefix=plate_type,
        #                        save_path=self.save_path, region_size=None, all_regions=self.regions_lists_yellow,
        #                        save_=save, plate_size=(520, 110))

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
        
#         elif plate_type == "short":
#             generate_plate(plate_path="plates/plate.jpg",  random=self.random,
#                        plate=plate, num_size=(40, 83), num_size_2=None, 
#                        num_list=self.num_lists, init_size=(46, 10),
#                        char_list=self.char_lists, regions=None, three_digit = None,
#                        num_ims=self.num_ims, char_size=(49, 70),  region_name=None,
#                        char_ims=self.char_ims, label_prefix=plate_type,
#                        save_path=self.save_path, region_size=None, all_regions=self.regions_lists_yellow,
#                        save_=save, plate_size=(355, 155))

#         elif plate_type == "yellow":
            
#             self.assertion(region_name, self.regions_lists_yellow)
            
#             generate_plate(plate_path="plates/plate_y.jpg",  random=self.random,
#                        plate=plate, num_size=(44, 60), num_size_2=(64, 90), 
#                        num_list=self.num_lists_yellow, char_list=self.char_lists_yellow,
#                        num_ims=self.num_ims_yellow, char_ims=self.char_ims_yellow,
#                        init_size=(8, 76), # start from left to right
#                        regions=self.regions_yellow, three_digit = None,
#                        char_size=(64, 62), region_name=region_name,
#                        label_prefix=plate_type, all_regions=self.regions_lists_yellow,
#                        save_path=self.save_path, region_size=(88, 60),
#                        save_=save, plate_size=(336, 170))

#         elif plate_type == "old":
            
#             self.assertion(region_name, self.regions_lists_yellow)
            
#             generate_plate(plate_path="plates/plate_g.jpg", 
#                        plate=plate, num_size=(44, 60), num_size_2=(64, 90), 
#                        num_list=self.num_lists_green, char_list=self.char_lists_green,
#                        num_ims=self.num_ims_green, char_ims=self.char_ims_green,
#                        init_size=(8, 76), # start from left to right
#                        regions=self.regions_green, three_digit = None,
#                        char_size=(64, 62), region_name=region_name,
#                        label_prefix=plate_type,  random=self.random,
#                        save_path=self.save_path, region_size=(88, 60),
#                        save_=save, plate_size=(336, 170))

#         elif plate_type == "green":
#             generate_plate(plate_path="plates/plate_g.jpg", 
#                        plate=plate, num_size=(60, 65), num_size_2=(80, 90), 
#                        num_list=self.num_lists_green, char_list=self.char_lists_green,
#                        num_ims=self.num_ims_green, char_ims=self.char_ims_green, region_size=None,
#                        init_size=(8, 78),  random=self.random, 
#                        char_size=(60, 65), label_prefix=plate_type, regions=None,
#                        save_path=self.save_path, region_name=None, three_digit = None,
#                        save_=save, plate_size=(336, 170))
        

    def generation(self, plate, save, plate_type, num=None, region_name=None):
        
        assert plate_type in ["short", "long", "yellow", "old", "green"], "Please choose the correct the plate type"
        
        if num != None:
            for i in range(num):
                self.generate(plate=plate, save=save, plate_type=plate_type, region_name=region_name)
        else:
            self.generate(plate=plate, save=save, plate_type=plate_type, region_name=region_name)
