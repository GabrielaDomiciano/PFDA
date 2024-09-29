#Simple program to read csv

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/" # to read in another folder

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: #vai imprimir a primeira linha separada
            print (f"{line}\n-------------------")
        else:
            total += int(line[0])
            print (line)
        linecount += 1
    