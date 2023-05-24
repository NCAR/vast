---
title: "VAST staff presents the latest research in lossy data compression at IPDPS"
author: "Samuel Li"
date: 2023-05-18
type: news
image: images/news/corona.png
feature_image: images/news/corona.png
layout: staticpage
---

VAST project scientist Samuel Li  presented his latest research on lossy data compression
at the *37th IEEE International Parallel & Distributed Processing Symposium*, or IPDPS,
in St. Petersburg, Florida.
In this presentation, Sam described high-level designs of **SPERR**, a wavelet-based
scientific data compressor, and also presented results comparing SPERR against other
leading scientific data compressors (ZFP, SZ, TTHRESH, and MGARD).
These results showcase the superior compression efficiency achieved by SPERR.
The corona emission visualized above illustrates the effect of SPERR compression: 
after compressing 32-bit floating-point values to 1.4 bit-per-point (a reduction factor
of 22X), there's no difference in the rendering.

IPDPS is the flagship conference sponsored by the Technical Community on 
Parallel Processing (TCPP) of IEEE Computer Society.
The slide deck of this presentation is publicly available [here](https://docs.google.com/presentation/d/144BQrZcpFcWi2px-xnQgQnaOnIyQHvuifA2zChgkYiE/edit?usp=sharing), 
and the published paper containing more technical details is accessible [here](https://vast.ucar.edu/pdfs/SPERR_IPDPS.pdf).
Finally, SPERR is open-source software ([Github repo](https://github.com/NCAR/SPERR)).
