hex_string = ""
with open("output.txt","r") as infile:
    for line in infile:
        if "0x" in line:
            h = line.strip()[2:].zfill(2)
        hex_string += h
    infile.close()

print(hex_string)
