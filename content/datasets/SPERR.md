---
title: "SPERR Compression"
date: 2022-06-24T11:44:13-06:00
type: projects
image: "images/projects/SPERR_logo.png"
category: ["RESEARCH"]
project_images: ["images/projects/SPERR_pipeline.png"]
---

##### Term: 2020 - 2023
##### Funding source: NSF
##### Website: [https://github.com/NCAR/SPERR](https://github.com/NCAR/SPERR)

SPERR is a lossy compressor for scientific data (2D or 3D floating-point data, 
mostly produced by numerical simulations). 
SPERR produces excellent rate-distortion curves, meaning that it achieves the least amount of 
average error given a certain storage budget.

Under the hood, SPERR uses wavelet transforms, [SPECK](https://ieeexplore.ieee.org/document/1347192) coding, 
and a custom outlier coding algorithm in its compression pipeline. 
This combination gives SPERR flexibility to compress targetting different quality controls, 
namely 1) bit-per-pixel (BPP), 2) peak signal-to-noise ratio (PSNR), and 3) point-wise error (PWE). 
The name of SPERR stands for **SP**eck with **ERR**or bounding.

