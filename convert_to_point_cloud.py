from pdbUtils import pdbUtils
import pandas as pd
import argparse
import os

def convert_to_point_cloud_main(input, ext):
    if ext == ".pdb":
        inputDf = pdbUtils.pdb2df(input)
        slicedDf = inputDf[["X", "Y", "Z"]].rename(columns=str.lower)
        slicedDf["lj"] = 1.0
    elif ext == ".csv":
        inputDf = pd.read_csv(input, skiprows=3)
        inputDf.columns = ["x", "y", "z", "chg", "hp", "lj"]
        slicedDf = inputDf[["x", "y", "z"]].copy()
        slicedDf["lj"] = 1.0
    else:
        return input
    outputPath = f"{(os.path.splitext(input)[0])}_zernike.csv"
    slicedDf.to_csv(outputPath, index=False)
    return outputPath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean PDB file: concatenate protein with ligand.")
    parser.add_argument("--input", type=str, default="/home/mchrnwsk/specification/structures/palmitic_acid.pdb", help="Path to input PDB file")
    args = parser.parse_args()
    input = args.input
    ext = os.path.splitext(input)[1]
    convert_to_point_cloud_main(input, ext)