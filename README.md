Code for matching ligands to cavities


First step is to compile the Zernike binary from Rosetta

git clone https://github.com/Andre-lab/rosetta

Compilation:
Information: https://docs.rosettacommons.org/docs/latest/build_documentation/Build-Documentation#setting-up-rosetta-3_alternative-setup-for-individual-workstations_scons-mac-linux_pilot-apps_scons

cd to rosetta/source and then run:
python scons.py bin zernike mode=release -j10 cxx=clang

Run it with:
zernike -xyzfile <input xyz + lj file> -descriptor_out <output file for the descriptors> -voxelgrid_out <output for the voxelgrid file. Is optional but nice to check shape.>

Additionally the parameters can be set:
-zernike_descriptor:order 20 
-zernike_descriptor:grid_size 64
-zernike_descriptor:surface_type MS
-zernike_descriptor:probe_radius 1.4
-zernike_descriptor:shell_thickness 2

To visualize the code and do euclidian norms you need
Need:
plotly
numpy
pandas