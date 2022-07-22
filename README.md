# HiRISE Thumbnails

This repo contains a few short script for scraping orbital images of the surface of Mars and associated metadata. Specifically, the images are scraped from the [University of Arizona Lunar & Planetary Laboratory's catalog](https://www.uahirise.org/catalog/) of interesting/notable targets. Original images are very large, so only the reduced resolution thumbnails are scraped, which are only a couple hundred pixels in each dimension and usually have 3 color channels.

Two batches of images can be downloaded:

- the `captioned` batch includes about 2,000 images with human-written captions
- the `non-captioned` batch includes about 70,000 images without human-written captions.

The data and further description are available [on kaggle](https://www.kaggle.com/datasets/markmbaum/mars-surface-images). There is also a [short notebook](hirise_thumbnails_prep.ipynb) demonstrating how to load the data+metadata, attmepting to mine the image titles for classification labels, and saving cleaned image data to file.

Finally, there is [another notebook](hirise_thumbnails_modeling.ipynb) where I train a model to predict metadata fields from the images using a convolutional neural network. Specifically, I see whether the solar azimuth angle, which is the angle of the sun over the horizon, can be accurately predicted for these images. Possibly, I thought, the model could learn geometric relationships between topographic features and their shadows. In principle this seems totally feasible and should be much easier for Martian images than Earth images. However, the model mostly fails for this image set. See the notebook for more. 