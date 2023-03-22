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
| <img src=https://user-images.githubusercontent.com/50166164/226815467-e010edbc-7fde-473f-8289-92b21f38aa50.jpg width=350px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/218386944-87f51541-5016-44c7-9d2d-0b45e073e621.jpg width=200px height=120px> | <img src=https://user-images.githubusercontent.com/50166164/218628189-0dab45b8-ed2c-4bef-84da-00c42dccc786.jpg width=320px height=80px> | <img src=https://user-images.githubusercontent.com/50166164/218628118-21eab9ea-7619-41e2-889c-311caf1c5a53.jpg width=200px height=120px> |





