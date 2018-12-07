filename = ""
lines = open(filename)

for line in lines.readlines():
    print(line)

#rb is read binary
with open("myfile", "rb") as f: 
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        byte = f.read(1)

with open("myfile", "rwb") as f: 
    f.write(b"This is writte as byte array")

