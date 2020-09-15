# Project: 3D printable Geographic Elevation map

## DEM to Mesh conversion : Landscapes transformation to 3D sample object

We have to create a 3D image of terrain from an array of 2D elevation values.The goal is to take an elevation map as input (meaning a grid with elevation data, as the usage of ones). We will generate a file that is printable by 3D printer. The output could be STL or an OBJ file, these file formats are used for 3D printing.

### Environment setup

Python v3.6 with [ANACONDA](https://docs.conda.io/en/latest/miniconda.html)

```bash
conda create --name m2m python=3.6
conda activate m2m
conda install -c conda-forge whitebox_tools
conda install --channel conda-forge geopandas
conda install --channel conda-forge spaghetti
pip install --use-feature=2020-resolver git+git://github.com/ozak/georasters.git
conda install rasterio
pip install earthpy
conda install -c conda-forge gdal
conda install -c conda-forge pdal python-pdal
conda install -c conda-forge trimesh
conda install -c conda-forge laspy
conda install -c open3d-admin open3d
conda install -c conda-forge meshio
pip install git+https://github.com/rougier/matplotlib-3d
conda install Pillow
conda install -c conda-forge vtk PyQt5
conda install -c conda-forge pyside2
pip install -r requirements.txt
```

## Execution CLI

Run the command with Anaconda envronment enabled.

```bash
conda activate m2m && python main.py
```

### user tips

the GeoTIFF file can be drag from File manager GUI and drop on the terminal for get the absolute FS paths exactly.

## Using libraries

- [GeoPandas](https://geopandas.org/data_structures.html)
- [PySAL Spagetti](http://pysal.org/notebooks/explore/spaghetti/intro.html)
- [matplotlib-3d](https://github.com/rougier/matplotlib-3d), [PyOpenGL](http://pyopengl.sourceforge.net/) : for 3d axis Visualization
- [MESHIO](https://github.com/nschloe/meshio), Trimesh : for meshed 3D data
- [GDAL](https://anaconda.org/conda-forge/gdal) for raster data
- [PDAL](https://anaconda.org/conda-forge/pdal) for points cloud data
- [LASPY](https://github.com/laspy/laspy): for LAS, LAZ files
- [WhiteboxTools](https://jblindsay.github.io/ghrg/WhiteboxTools/) for GIS DEM transformations

## Working file formats

- [VTK is an open-source software system for image processing, 3D graphics, volume rendering and visualization.](https://vtk.org/doc/nightly/html/index.html)
- .tif [GeoTIFF](https://earthdata.nasa.gov/esdis/eso/standards-and-references/geotiff):
  open with the IDE Quantum GIS [QGIS](http://www.qgis.org/)
- .laz (Compressed LAS) , .las (LAS):
  open with the IDE [CloudCompare](https://www.cloudcompare.org/)
- .obj (Wavefront OBJ), .ply (Stanford Triangle Format):
  open with the IDE [GMSH](http://gmsh.info/), [MeshLab](http://www.meshlab.net/)

### Based the works of Dr.Richard Barnes

on the project [DEM to 3D](https://github.com/r-barnes/DEMto3D)

## Sugested open data sources

- [Extraterrestrial planets map by USG](https://www.usgs.gov/centers/astrogeology-science-center/science/mrctr-gis-lab)
- [Earth map by USGS](https://earthexplorer.usgs.gov/)
- [OpenTopography](https://opentopography.org/blog/demand-3d-topographic-differencing)

## Contacts team members

Date: May 4, 2020
Bordeaux Université
Master Informatique 2019

- Nguyen Vu Anh Trung (kivanolai@gmail.com)
- Tran Quang Tung (quangtung0276@yahoo.com)
- Nguyen Quoc Khanh (qkhanh2006@gmail.com)
