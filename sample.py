from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tool import numpy2stl

A = 256 * imread("examples/ex2/PIO.png")
A = A[:, :, 2] + 1.0*A[:,:, 0] # Compose RGBA channels to give depth
A = gaussian_filter(A, 1)  # smoothing
numpy2stl(A, "examples/ex2/PIO.stl", scale=0.05, mask_val=5., solid=True)
