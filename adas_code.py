def read_data(infile):
    import numpy as np
    import csv
    grades = np.loadtxt(infile ,delimiter=',' ,skiprows=1, unpack=True, dtype=float)
    return grades[1]
    