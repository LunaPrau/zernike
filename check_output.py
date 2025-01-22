from voxel_to_html import voxel_to_html
import numpy as np

# read in zernike descriptors
desc = np.loadtxt("data/descriptor.csv", skiprows=1)

# euclidian distance (compare to itself, should have another one)
dist = np.linalg.norm(desc - desc)

# Output Voxelgrid
voxel_file = "data/voxelgrid.json"
grid_size = 64
html_file = "data/voxelgrid.html"
voxel_to_html(voxel_file, grid_size, html_file)

