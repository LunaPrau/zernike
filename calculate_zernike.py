import subprocess
from zernike.convert_to_point_cloud import convert_to_point_cloud_main
from zernike.visualise_zernike import visualise_zernike_main
import os
import logging
import time

def calculate_zernike_main(inputPath, outputDir, zernikeSettings):
    startTime = time.time()
    execPath = "/home/mchrnwsk/tools/rosetta/source/bin/zernike.default.linuxgccrelease"

    makeHtml = zernikeSettings["make_html"]
    gridSize = zernikeSettings["grid_size"]

    name, ext = (os.path.splitext(os.path.basename(inputPath)))
    if ext == ".txt":
        xyzArg = "-xyzlist"
    else:
        xyzArg = "-xyzfile"
    outputDescr = f"{outputDir}/{name}_descrOut.csv"
    outputVoxel = f"{outputDir}/{name}_voxelOut.json"
    outputHtml = None

    if makeHtml:
        command = f"{execPath} {xyzArg} {inputPath} -descriptor_out {outputDescr} -voxelgrid_out {outputVoxel} -never_leave_neighbour 1"
    else:
        command = f"{execPath} {xyzArg} {inputPath} -descriptor_out {outputDescr} -never_leave_neighbour 1"
    result = subprocess.run(command, shell=True, check=True, capture_output = True, text = True)
    logging.debug(result.stdout)
    # Log standard error, filter out empty lines
    for line in result.stderr.splitlines():
        if line.strip():  # Check for non-empty lines
            logging.warning(line)
    logging.debug("*** Zernike calculation complete!")
    logging.debug(f"Output saved to: {outputDescr} and {outputVoxel}")

    if makeHtml:
        outputHtml = f"{outputDir}/{name}_voxelGrid.html"
        visualise_zernike_main(outputVoxel, outputHtml, gridSize)

    elapsedTime = time.time() - startTime
    return elapsedTime, outputDescr
if __name__ == "__main__":
    calculate_zernike_main()