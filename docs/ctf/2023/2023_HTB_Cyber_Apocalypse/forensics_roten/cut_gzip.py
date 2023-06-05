"""
4854 5450 2f31 2e31 2032 3030 204f
5554 462d 380d 0a0d 0a1f 8b08 0000 0000 0000
"""

HTTP_HEADER = "485454502f312e3120323030204f"
GZIP_MN = "1f8b"

FILENAME = "results-display_attacker_raw"
data = dict()
with open(FILENAME,"rb") as infile:
    hex_string = ""
    for line in infile:
        hex_string += line.strip().hex()

    hex_string_list = hex_string.split(GZIP_MN)
    for x,hsl in enumerate(hex_string_list):
        print(hex_string_list)
        if HTTP_HEADER not in hsl:
            data[x] = GZIP_MN + hsl
    print(data)
    infile.close()

for d in data:
    with open("results-display{}.gzip".format(d),"wb+") as outfile:
        outfile.write(bytearray.fromhex(data[d]))
        outfile.close()

FILENAME = "map-update_attacker_raw"
data = dict()
with open(FILENAME,"rb") as infile:
    hex_string = ""
    for line in infile:
        hex_string += line.strip().hex()

    hex_string_list = hex_string.split(GZIP_MN)
    for x,hsl in enumerate(hex_string_list):
        print(hex_string_list)
        if HTTP_HEADER not in hsl:
            data[x] = GZIP_MN + hsl
    print(data)
    infile.close()

for d in data:
    with open("map-update{}.gzip".format(d),"wb+") as outfile:
        outfile.write(bytearray.fromhex(data[d]))
        outfile.close()
