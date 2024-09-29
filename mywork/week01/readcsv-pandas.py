# reading csv as a pandas



FILENAME = "data.csv"
DATADIR = "../datafiles/" # to read in another folder

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print(df)
