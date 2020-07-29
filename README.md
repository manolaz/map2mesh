# Elevation map to 3D sample object 
## Project :3D printed landscapes
Date: May 4, 2020
Bordeaux Université	 
Master Informatique 2019

Team members:
- Nguyen Vu Anh Trung (kivanolai@gmail.com)
- Tran Quang Tung (quangtung0276@yahoo.com)
- Nguyen Quoc Khanh (qkhanh2006@gmail.com)

# Components:# LAS to RASTER conversion

This example run analysis of the LAS dataset, to transpose data source into scaled Raster map of readeable 3 axis X + Y + Z coordinations.
It will take the LAS Points in DATA respository and scale it and to make an XYZ out file export in DATA.

## Execute DEMO example

```bash
python3 out_converter.py
```

## Libraries setup with ANACONDA

PDAL + Trimesh

```bash
conda create -n geo
conda activate geo
conda install -c conda-forge pdal python-pdal gdal
conda install -c conda-forge trimesh4
pip install numpy-stl
```

- ### [PDAL](https://anaconda.org/conda-forge/pdal)
- ### [LASPY](https://pythonhosted.org/laspy/laspy_tools.html)

