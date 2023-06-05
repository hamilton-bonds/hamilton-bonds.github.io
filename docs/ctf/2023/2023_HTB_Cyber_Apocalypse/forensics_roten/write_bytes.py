h_string = ""

FILENAME = "galacticmap.txt"

with open(FILENAME,"r") as infile:
    FILE = FILENAME.split(".")[0]
    for line in infile:
        h_string += line.strip()
    infile.close()

with open(FILE+".pdf","wb+") as outfile:
    outfile.write(bytearray.fromhex(h_string))
    outfile.close()
