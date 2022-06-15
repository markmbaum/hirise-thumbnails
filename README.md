# HiRISE Thumbnails

This repo contains a few short script for scraping orbital images of the surface of Mars and associated metadata. Specifically, the images are scraped from the [University of Arizona Lunar & Planetary Laboratory's catalog](https://www.uahirise.org/catalog/) of interesting/notable targets. Original images are very large, so only the reduced resolution thumbnails are scraped, which are usually about 150 x 100 pixels and usually have 3 color channels.

Two batches of images can be downloaded:

- the `captioned` batch includes about 2,000 images with human-written captions
- the `non-captioned` batch includes about 70,000 images without human-written captions.

The data and further description are available [on kaggle](https://www.kaggle.com/datasets/markmbaum/mars-surface-images). There is also a [short notebook](https://www.kaggle.com/code/markmbaum/getting-started) available demonstrating how to load the data+metadata and attmepting to mining the image titles for information.
