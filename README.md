# Elevation map to 3D sample object

## Project :3D printed landscapes

Date: May 4, 2020
Bordeaux Université
Master Informatique 2019

## Install ANACONDA or [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Environment setup Python v3.6 with ANACONDA


```bash
conda create --name wb python=3.6
conda activate wb
conda install -c conda-forge whitebox_tools
conda install rasterio
conda install -c conda-forge gdal
conda install -c conda-forge pdal python-pdal
conda install -c conda-forge trimesh
conda install -c conda-forge laspy
conda install -c open3d-admin open3d
pip install numpy-stl
pip install pylab-sdk
```

## Using libraries:

- [GDAL](https://anaconda.org/conda-forge/gdal) for raster data
- [PDAL](https://anaconda.org/conda-forge/pdal) for points cloud data
- [LASPY](https://github.com/laspy/laspy)
- Trimesh for mesh data
- ### [WhiteboxTools] (https://jblindsay.github.io/ghrg/WhiteboxTools/)

## LAS to RASTER conversion
This example run analysis of the LAS dataset, to transpose data source into scaled Raster map of readeable 3 axis X + Y + Z coordinations.
It will take the LAS Points in DATA respository and scale it and to make an XYZ out file export in DATA.

## Contacts:
Team members:
- Nguyen Vu Anh Trung (kivanolai@gmail.com)
- Tran Quang Tung (quangtung0276@yahoo.com)
- Nguyen Quoc Khanh (qkhanh2006@gmail.com)