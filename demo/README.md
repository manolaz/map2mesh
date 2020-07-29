# LAS to RASTER conversion

This example run analysis of the LAS dataset, to transpose data source into scaled Raster map of readeable 3 axis X + Y + Z coordinations.
It will take the LAS Points in DATA respository and scale it and to make an XYZ out file export in DATA.

## Execute example

```bash
python3 out_converter.py
```

## PDAL setup with ANACONDA

```bash
conda create -n geo
conda activate geo
conda install -c conda-forge pdal python-pdal gdal
```

https://anaconda.org/conda-forge/pdal

## PYTHON Package used LASPY
https://pythonhosted.org/laspy/laspy_tools.html
