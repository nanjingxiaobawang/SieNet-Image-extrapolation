# SiENet-Image-extrapolation
Paper:"SiENet: Siamese Expansion Network for Image Extrapolation"
# Abstract
Different from image inpainting, image outpainting has relative less context in the image center to capture and more content at the image border to predict. Therefore, classical
encoder-decoder pipeline of existing methods may not satisfy the need of predicting the outstretched unknown content. In this paper, we propose a novel two-stage siamese adversarial model for image extrapolation, named Siamese Expansion Network(SiENet). In two stages, a novel border sensitive convolution named filling convolution is designed for allowing encoder to predict the unknown content, alleviating the burden of decoder. Besides, to introduce prior knowledge to network and reinforce the inferring ability of encoder, siamese adversarial mechanism is designed to enable our network to model covered long range feature toward the uncovered image feature. The results on four datasets has demonstrated that our method outperforms existing state-of-the-arts and could produce realistic results. Our code is released on.
 ![image](https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/blob/master/results.png)
 ![image](https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/blob/master/structure.png)
![image](https://github.com/nanjingxiaobawang/SieNet-Image-extrapolation/blob/master/adaptive-filling-convolution.png)
