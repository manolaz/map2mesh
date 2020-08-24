# Project: 3D printable Geographic Elevation map

## DEM to Mesh conversion : Landscapes transformation to 3D sample object

We have to create a 3D image of terrain from an array of 2D elevation values.The goal is to take an elevation map as input (meaning a grid with elevation data, as the usage of ones). We will generate a file that is printable by 3D printer. The output could be STL or an OBJ file, these file formats are used for 3D printing.

### Environment setup

Python v3.6 with [ANACONDA](https://docs.conda.io/en/latest/miniconda.html)

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
conda install -c conda-forge meshio
pip install git+https://github.com/rougier/matplotlib-3d
pip install PyOpenGL PyOpenGL_accelerate
conda install Pillow
pip install -r requirements.txt
```

## Using libraries
- [ matplotlib-3d](https://github.com/rougier/matplotlib-3d), [PyOpenGL](http://pyopengl.sourceforge.net/) : for 3d axis Visualization
- [MESHIO](https://github.com/nschloe/meshio), Trimesh : for meshed 3D data
- [GDAL](https://anaconda.org/conda-forge/gdal) for raster data
- [PDAL](https://anaconda.org/conda-forge/pdal) for points cloud data
- [LASPY](https://github.com/laspy/laspy): for LAS, LAZ files
- [WhiteboxTools](https://jblindsay.github.io/ghrg/WhiteboxTools/) for GIS DEM transformations

## Working file formats

 - .tif [GeoTIFF](https://earthdata.nasa.gov/esdis/eso/standards-and-references/geotiff): 
 open with the IDE Quantum GIS [QGIS](http://www.qgis.org/)
 - .laz (Compressed LAS) , .las (LAS):
 open with the IDE [CloudCompare](https://www.cloudcompare.org/)
 - .obj (Wavefront OBJ), .ply (Stanford Triangle Format):
 open with the IDE [MeshLab](http://www.meshlab.net/)

### Based the works of Dr.Richard Barnes

on the project [DEM to 3D](https://github.com/r-barnes/DEMto3D)

## Sugested open data sources

- [Earth map by USGS](rhttps://earthexplorer.usgs.gov/)
- [OpenTopography](https://opentopography.org/blog/demand-3d-topographic-differencing)

## Contacts team members

Date: May 4, 2020
Bordeaux Université
Master Informatique 2019

- Nguyen Vu Anh Trung (kivanolai@gmail.com)
- Tran Quang Tung (quangtung0276@yahoo.com)
- Nguyen Quoc Khanh (qkhanh2006@gmail.com)