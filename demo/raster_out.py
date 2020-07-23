import arcpy
from arcpy import env
import glob, os
env.workspace = "CURRENT"
arcpy.CheckOutExtension('3D')


files = glob.glob(os.getcwd() + "/data/*.las")

# inputLASFile = "LAS.lasd"
outputRasterFile = "Raster"
arcpy.LasDatasetToRaster_3d(files, outputRasterFile, 'ELEVATION', 'TRIANGULATION LINEAR NONE')