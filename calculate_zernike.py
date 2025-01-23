import subprocess
from check_output import check_zernike_output_main
import os

execPath = "/home/mchrnwsk/tools/rosetta/source/bin/zernike.default.linuxgccrelease"

pointCloudPath = "/home/mchrnwsk/tools/zernike_ligand/data/palmitic_acid_conf_out_7.csv"
name = (os.path.splitext(os.path.basename(pointCloudPath))[0])

outputDir = "/home/mchrnwsk/tools/zernike_ligand/output"
outputDescr = f"{outputDir}/{name}_descrOut.csv"
outputVoxel = f"{outputDir}/{name}_voxelOut.json"
outputHtml = f"{outputDir}/{name}_voxelGrid.html"

command = f"{execPath} -xyzfile {pointCloudPath} -descriptor_out {outputDescr} -voxelgrid_out {outputVoxel}"
subprocess.run(command, shell=True, check=True)

check_zernike_output_main(outputDescr, outputVoxel, outputHtml)