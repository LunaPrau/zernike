import subprocess
from zernike.convert_to_point_cloud import convert_to_point_cloud_main
from zernike.visualise_zernike import visualise_zernike_main
import os
import logging

def calculate_zernike_main(inputPath, outputDir, zernikeSettings):
    execPath = "/home/mchrnwsk/tools/rosetta/source/bin/zernike.default.linuxgccrelease"

    makeHtml = zernikeSettings["make_html"]
    gridSize = zernikeSettings["grid_size"]

    name, ext = (os.path.splitext(os.path.basename(inputPath)))
    pointCloudPath = convert_to_point_cloud_main(inputPath, ext)
    outputDescr = f"{outputDir}/{name}_descrOut.csv"
    outputVoxel = f"{outputDir}/{name}_voxelOut.json"
    outputHtml = None

    command = f"{execPath} -xyzfile {pointCloudPath} -descriptor_out {outputDescr} -voxelgrid_out {outputVoxel}"
    result = subprocess.run(command, shell=True, check=True, capture_output = True, text = True)
    logging.debug(result.stdout)
    logging.warning(result.stderr)
    logging.debug("*** Zernike calculation complete!")
    logging.debug(f"Output saved to: {outputDescr} and {outputVoxel}")

    if makeHtml:
        outputHtml = f"{outputDir}/{name}_voxelGrid.html"
        visualise_zernike_main(outputVoxel, outputHtml, gridSize)
    return {"descr": outputDescr, "voxel": outputVoxel, "html": outputHtml}

if __name__ == "__main__":
    calculate_zernike_main()