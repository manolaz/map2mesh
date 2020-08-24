import rasterio
import numpy as np

with rasterio.open('infile.tif') as src:
    dem = src.read(1)

r = np.zeros(dem.shape)
g = np.zeros(dem.shape)
b = np.zeros(dem.shape)

r += np.floor_divide((100000 + dem * 10), 65536)
g += np.floor_divide((100000 + dem * 10), 256) - r * 256
b += np.floor(100000 + dem * 10) - r * 65536 - g * 256

meta = src.meta
meta(
    dtype=rasterio.uint8,
    nodata=0,
    count=3)

with rasterio.open('outfile.tif', 'w', **meta) as dst:
    dst.write_band(1, r.astype(rasterio.uint8))
    dst.write_band(2, g.astype(rasterio.uint8))
    dst.write_band(3, b.astype(rasterio.uint8))