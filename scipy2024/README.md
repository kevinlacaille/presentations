# Urban EcoVision: Climate Mitigation with Drones and Python

## Preparing your Workspace 

Follow the set up instructions below to run the Jupyter Notebooks for this workshop.

### Option 1: (recommended) Run in Google Colab

Interact directly with this repo's Jupyter Notebooks by running them in Google Colab.

Each Notebook will have its own **"Open in Colab"** button: once running on Colab, you'll need to run a quick setup cell in each notebook (this will install prerequisites and download data into your Colab workspace). You can also choose to make a copy of the Notebook in your own Google Drive, if you want to save any changes you make (not required for this workshop).

### Option 2: Run local Jupyter instance

You can instead choose to open this Notebook in your own local Jupyter instance. In that case, you'll need to clone this repository and install/download prerequisites.

Clone this repo:
```bash
git clone git@github.com:kevinlacaille/presentations.git
cd scipy2024/
```

**Prerequisites**
- Read the [installation.md](installation.md) for instructions of how to set up the (optional) virtual environment.
- Install all libraries `pip install -r requirements.txt`

## Tutorial outline
### Abstract
Drone imagery is more widely available than ever before, allowing the public to capture ultra high-resolution Earth images with hobbyist drones. In this workshop, we will explore drone imagery with Python tools such as geopandas, OpenCV, rasterio, numpy, and shapely. Afterwards, we will assess urban green spaces, focusing on counting trees and estimating their role in capturing carbon to fight climate change. This practical exercise will not only enhance our understanding of urban ecology, but also highlight the importance of trees in urban planning and environmental sustainability.

### Description
The tutorial will be a combination of slides and hands-on live coding with real-world data in Jupyter Notebooks and will cover the following topics:

1. **Introduction to Geospatial Imagery and Basics Image Processing (First 1/3 of the Tutorial)**
   - Briefly introduce and explain the structure of the workshop and give motivation for drone imagery in the fight against climate change.
   - Inform attendees about accessing Jupyter notebooks hosted on Google Colab, including all hands-on material for the workshop, drone imagery, metadata, and additional materials.
   - Start with an introduction to drone technology and its application in environmental analysis, focusing on urban green spaces.
   - Cover basic concepts of working with drone imagery, including understanding drone capabilities, image resolution, and data types.
   - Introduce the Python libraries that will be used throughout the workshop, such as rasterio for raster data manipulation, numpy for numerical analysis, openCV for computer vision tasks, shapely for geometric operations, geopandas for geospatial data processing, and computer vision libraries for object detection and identification. Explain the significance of each in the context of drone imagery analysis.

2. **Hands-On Drone Data and Computer Vision Exercise (Remaining 2/3 of the Workshop)**
   - Transition into a more interactive session, where participants will follow along with pre-made Jupyter Notebooks hosted on Google Colab. This session is designed to be accessible and interesting for all skill levels, from beginners to experienced Python users. Here we will be focusing on tools we will use in the final hands-on exercise, counting trees and estimating carbon capture.
   - Introduction to reading geospatial data, extracting images, and composing a scene.
   - Dive deeper into geospatial analysis and computer vision packages, showcasing how to apply these tools to drone imagery.
   - Explore basic computer vision applications, focusing on image processing techniques and object detection using models to identify and count trees in urban settings.
   - Discuss how to interpret the results and estimate a region’s carbon capture. 
   - Hands-on exercise: Here we will be combining everything we learned in the workshop thus far to create a tool to estimate a city’s ability to mitigate climate change from its greenery.
