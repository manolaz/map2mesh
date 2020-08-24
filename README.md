# Project: 3D printable landscapes

## Geographic Elevation map transformation to 3D sample object

### LAS to RASTER conversion

This example run analysis of the LAS dataset, to transpose data source into scaled Raster map of readeable 3 axis X + Y + Z coordinations.
It will take the LAS Points in DATA respository and scale it and to make an XYZ out file export in DATA.

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
- [Experimental 3d axis for matplotlib](https://github.com/rougier/matplotlib-3d)
- [Python & OpenGL for Scientific Visualization](https://github.com/rougier/python-opengl), [PyOpenGL](http://pyopengl.sourceforge.net/)
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