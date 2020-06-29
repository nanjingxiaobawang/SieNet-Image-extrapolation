# SiENet-Image-extrapolation
Paper:"SiENet: Siamese Expansion Network for Image Extrapolation"
# Abstract
In this paper, we propose a novel two-stage siamese adversarial model for image extrapolation, named Siamese Expansion Network(SiENet). In two stages, a novel border sensitive convolution named filling convolution is designed for allowing encoder to predict the unknown content, alleviating the burden of decoder. Besides, to introduce prior knowledge to network and reinforce the inferring ability of encoder, siamese adversarial mechanism is designed to enable our network to model covered long range feature toward the uncovered image feature. The results on four datasets has demonstrated that our method outperforms existing state-of-the-arts and could produce realistic results. Our code is released on.
 ![image](https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/blob/master/results.png)
 ![image](https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/blob/master/structure.png)
# Requirements

Pytorch >= 1.0

Python 3

NVIDIA GPU + CUDA 9.0

Tensorboard

Matlab

# Installation

1.Clone the code

git clone https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/edit/

2.Build Gaussian Sampling CUDA package

cd ./SieNet-Image-extrapolation/resample2d_package
python setup.py install --user

# Run 
our method is evaluated on three datasets, i.e., Cityscapes, paris street-view and beach . Single-direction evaluation is made on Scenery dataset. Smooth image
could be get by 1. 超链接：[文本](https://github.com/RenYurui/StructureFlow）
