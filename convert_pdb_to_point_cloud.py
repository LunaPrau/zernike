from pdbUtils import pdbUtils
import argparse
import os

def convert_pdb_to_point_cloud_main(inputPdb):
    inputDf = pdbUtils.pdb2df(inputPdb)
    slicedDf = inputDf[["X", "Y", "Z"]].rename(columns=str.lower)
    slicedDf["lj"] = 1.0
    outputPath = f"{(os.path.splitext(inputPdb)[0])}.csv"
    slicedDf.to_csv(outputPath, index=False)
    print(f"Point cloud with x, y, z, lj has been created and saved to {outputPath}.")   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean PDB file: concatenate protein with ligand.")
    parser.add_argument("--input", type=str, default="/home/mchrnwsk/specification/structures/palmitic_acid.pdb", help="Path to input PDB file")
    args = parser.parse_args()
    input = args.input
    convert_pdb_to_point_cloud_main(input)