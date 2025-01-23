from voxel_to_html import voxel_to_html
import numpy as np

def check_zernike_output_main(decrPath, voxelPath, outputHtml):

    # read in zernike descriptors
    desc = np.loadtxt(decrPath, skiprows=1)

    # euclidian distance (compare to itself, should have another one)
    dist = np.linalg.norm(desc - desc)

    # Output Voxelgrid
    gridSize = 64
    voxel_to_html(voxelPath, gridSize, outputHtml)

if __name__ == "__main__":
    check_zernike_output_main()