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
