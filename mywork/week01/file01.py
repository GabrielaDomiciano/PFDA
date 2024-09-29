FILENAME = "data1.txt"
DATADIR = "../datafiles/" # para ler de outra pasta 

print (DATADIR + FILENAME)
with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line)
        print (f"{line} is size {len(line)}")
    print("")
    print (f"Total is {total}")