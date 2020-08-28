#!/usr/bin/env python3

'''
Tranformer GeoTiff DEM file to STL format
'''

import argparse
import numpy as np
from osgeo import gdal
from stltools import stlgenerator
import scipy as sp
import scipy.ndimage as scimage
import click

CMAX = np.inf
CMIN = -np.inf
ALLOWED_TYPES = {gdal.GDT_Byte,gdal.GDT_Int16,gdal.GDT_Int32,gdal.GDT_UInt16,gdal.GDT_UInt32,gdal.GDT_Float32,gdal.GDT_Float64}

@click.command()
@click.option('--sourcefile', prompt='Your GeoTiFF sourcefile path, relative or absolute')
@click.option('--quality',  default=2, help='The resolution of the resulting BMP. 1 will match the source resolution.')
@click.option('--vsize',    type=float, default=1,          help='Height of DEM in the output in arbitrary units.')
@click.option('--clipmax',  type=float, default=CMAX,     help='Clip input data to this maximum value.')
@click.option('--clipmin',  type=float, default=CMIN,    help='Clip input data to this minimum value.')
@click.option('--base',     type=float, default=0,          help='Add this value in arbitrary units everywhere to make a thicker base.')
@click.option('--hsize',    type=float, default=1.0,        help='Width of the narrowest axis of the piece in arbitrary units')
@click.option('--hsep',     type=float, default=0,          help='Separation distance between stacked DEMs in arbitrary units')
@click.option('--sdep',     type=float, default=0.1,        help='Depth of separator between stacked DEMs')
@click.option('--tdep',     type=float, default=0.3,        help='Depth of separator tabs between stacked DEMs')
@click.option('--tsize',    type=float, default=0.3,        help='Size of tabs between stacked DEMs')
@click.option('--asize',    type=float, default=0.75,       help='Size of the anchor material on the end')
@click.option('--parallel', default=False ,help='Run STL generation in parallel')
# @click.option('--combine', type=str, default='sep', help='Way to combine multiple files. Options are: sep, vstack')
# @click.option('--rotate',  help='Transpose the input data')
def gen_stl(sourcefile, quality, vsize, clipmax, clipmin, base, hsize, hsep, sdep, tdep, tsize, asize, parallel):
  gdal.UseExceptions()
  click.echo('Tranformer GeoTiff DEM file to STL format ')
  # Parameter
  file   = [gdal.Open(sourcefile) ]
  band    = [file.GetRasterBand(1)]
  no_data = band.GetNoDataValue()
  srcdata  = band.ReadAsArray()
  # dtype   =   band.DataType in ALLOWED_TYPES

  for i in range(len(srcdata)):
    srcdata[i] = np.clip(srcdata[i], clipmin, clipmax)
    sigma  = [1, 1]
    srcdata[i] = scimage.filters.gaussian_filter(srcdata[i], sigma, mode='constant')
  # exporting STL beside input data
  export_file_name = (sourcefile).strip('.tif') +'.stl'
  stlgenerator.generate_from_heightmap_array(
    srcdata, export_file_name, 
    hsize=hsize, vsize=vsize, base=base, hsep=hsep,sep_dep=sdep, 
    tab_dep=tdep, tab_size=tsize,
    anchorsize=asize, multiprocessing=False)

if __name__ == '__main__':
  gen_stl()