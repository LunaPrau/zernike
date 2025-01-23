from zernike.voxel_to_html import voxel_to_html
import numpy as np

def visualise_zernike_main(voxelPath, outputHtml, gridSize=64):
    # Output Voxelgrid
    voxel_to_html(voxelPath, outputHtml, gridSize)

if __name__ == "__main__":
    visualise_zernike_main()