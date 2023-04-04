# Uzbekistan Licence Plate Generator

This repository contains PyTorch implementation of real and synthetic Uzbek licence plate (LP) registration numbers. First, the synthetic Uzbek LP numbers are generated and they are used as input to the Generative Adversarial Network (GAN) model to make real-life LP numbers with certain amount of distortions.

### Virtual Environment Creation

```python

conda create -n <ENV_NAME> python=3.9
conda activate <ENV_NAME>
pip install -r requirements.txt

```

### Synthetic Uzbek Licence Plates Generation
The synthetic LP numbers are generated based on [the latest available online information](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Uzbekistan). According to the information, there are five widely-used car LP types in Uzbekistan:

* [Private Passenger Cars LP](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Uzbekistan#/media/File:Pelak_shakhsi-UZ.png);
* [State Passenger Cars LP](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Uzbekistan#/media/File:Pelak_dolati-UZ.png);
* [Diplomatic Cars LP](https://upload.wikimedia.org/wikipedia/commons/7/78/Uzbekistan_diplomatic_license_plate.png);
* [Foreign Residents Cars LP](https://upload.wikimedia.org/wikipedia/commons/2/25/Pelak_khareji-UZ.png);
* [Foreign Companies Cars LP](https://upload.wikimedia.org/wikipedia/commons/f/fa/Pelak_mohajer-UZ.png);

##### 🚗 Sample LPs 🚗

| Private Passenger Cars LP | State Passenger Cars LP | Diplomatic Cars LP | Foreign Residents Cars LP | Foreign Companies Cars LP |
|       :-:       |     :---------:        |         :-:         |        :--------:         |   :----:         | 
| <img src=https://user-images.githubusercontent.com/50166164/226815467-e010edbc-7fde-473f-8289-92b21f38aa50.jpg width=390px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/226815584-e8932cc2-ef6f-494c-9e02-30fcd9d9a164.jpg width=390px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/226815921-cc2e6de1-96ca-46da-8be0-888aa3473e40.jpg width=390px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/226815751-d308f26e-896d-49b7-8d53-1488c6498f85.jpg width=390px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/226815690-05716ce9-1c71-4e4c-8a8e-a1b4d97da099.jpg width=390px height=80px>

##### :computer: Generate synthetic LPs from pre-defined file :computer:
```
python generate.py --data_path "path/to/csv_file" --save_path "path/to/save/synthetic_lps" --random=False --transformations=False --save=True
```
This script gets information about the LPs from pre-defined csv file, generates synthethic LPs, and saves them into the save_path.

##### :computer: Generate synthetic LPs (random generation) :computer:

```
python generate.py --save_path "path/to/save/synthetic_lps" --random=True --transformations=False --random=True --save=True --number_of_plates 100

```
This script randomly creates LP information, generates synthethic LPs from the randomly created information, and saves them into the save_path.

##### :computer: Create train dataset :computer:

```
python make_dataset.py --in_im_paths "path/to/generated/synthetic_lps" --out_im_paths "path/to/real-life/images" --trainA "path/to/copy/synthetic/images" --trainB "path/to/copy/real-life/images" --type "train or test depending on dataset type"

```

### Real Uzbekistan Licence Plates Generation

##### Train

After getting synthetic images, we train them using an efficient and fast proposed network as follows:




