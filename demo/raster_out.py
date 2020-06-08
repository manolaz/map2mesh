import arcpy
from arcpy import env
env.workspace = "CURRENT"
arcpy.CheckOutExtension('3D')
inputLASFile = "LAS.lasd"
outputRasterFile = "Raster"
arcpy.LasDatasetToRaster_3d(inputLASFile, outputRasterFile, 'ELEVATION', 'TRIANGULATION LINEAR NONE')