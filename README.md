# Elevation map to 3D sample object 
## Project :3D printed landscapes
Date: May 4, 2020
Bordeaux Université	 
Master Informatique 2019

Team members:
- Nguyen Vu Anh Trung (kivanolai@gmail.com)
- Tran Quang Tung (quangtung0276@yahoo.com)
- Nguyen Quoc Khanh (qkhanh2006@gmail.com)

## LAS to RASTER conversion

This example run analysis of the LAS dataset, to transpose data source into scaled Raster map of readeable 3 axis X + Y + Z coordinations.
It will take the LAS Points in DATA respository and scale it and to make an XYZ out file export in DATA.

## Execute DEMO example

```bash
python3 out_converter.py
```

## Install ANACONDA or [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Libraries setup with ANACONDA

GDAL for raster data
PDAL for points cloud data
Trimesh for mesh data

```bash
conda create -n geo python=3.7
conda activate geo
conda install rasterio
pip install numpy-stl
pip install pylab-sdk
conda install -c conda-forge gdal
conda install -c conda-forge pdal python-pdal
conda install -c conda-forge trimesh
conda install -c conda-forge laspy
```
- ### [PDAL](https://anaconda.org/conda-forge/pdal)
- ### [LASPY](https://github.com/laspy/laspy)
- ### [GDAL](https://anaconda.org/conda-forge/gdal)

