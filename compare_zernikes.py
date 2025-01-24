import numpy as np

def compare_zernikes_main(decrPath1, decrPath2):

    # read in zernike descriptors
    desc1 = np.loadtxt(decrPath1, skiprows=1)
    desc2 = np.loadtxt(decrPath2, skiprows=1)

    # euclidian distance (compare to itself, should have another one)
    dist = np.linalg.norm(desc1 - desc2)
    return dist

if __name__ == "__main__":
    compare_zernikes_main()