#messing with files

FILENAME= "data.txt"

with open(FILENAME, 'r') as f:
    data = f.read()
    print(data)
    print(data[:1]) # to print the fisrt letter

with open("data2.txt", "a") as f:
    f.write("what the hell\n")
    f.write("brown cow")


print("Done")


NAME= "data2.txt"
with open(NAME, 'r') as f:
    data2 = f.read()
    print(data2)