import os

FILENAME = "messingwithfiles"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end='')
else:
    print(FILENAME, "Does not exist")



NAME = "data2.txt"

if os.path.exists(NAME):
    with open(NAME, "r") as f:
        for line in f:
            print(line, end='') # end para nao imprimir linha em branco
else:
    print(NAME, "Does not exist")