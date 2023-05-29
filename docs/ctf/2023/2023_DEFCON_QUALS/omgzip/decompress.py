#!/usr/bin/env python3

import sys

INPUT_FILENAME = sys.argv[1]
OUTPUT_FILENAME = INPUT_FILENAME[:INPUT_FILENAME.index(".omgzip")]

print("Decompressing {} to {}".format(INPUT_FILENAME, OUTPUT_FILENAME))

def decompress(compressed_data: bytes) -> bytes:
    """
    Decompresses OMGZIP-compressed data.
    """

    # Check if the compressed data is valid
    if not compressed_data.startswith(b"\x4F\x4D\x47\x5A\x49\x50"):
        raise ValueError("Invalid OMGZIP-compressed data")

    # Initialize the Huffman tree
    huffman_tree = {}
    for i in range(256):
        huffman_tree[i] = i

    # Iterate over the compressed data
    idx = 6
    output_data = bytearray()
    while idx < len(compressed_data):
        # Decode the next symbol
        symbol = compressed_data[idx]
        idx += 1

        # If the symbol is a literal, add it to the output data
        if symbol < 255:
            output_data.append(symbol)

        # If the symbol is a pointer, follow the pointer to the next symbol and add it to the output data repeatedly
        else:
            count = symbol - 255
            symbol = compressed_data[idx]
            idx += 1
            for _ in range(count):
                output_data.append(symbol)

    # Return the decompressed data
    return output_data


if __name__ == "__main__":
    # Read the compressed data from the input file
    with open(INPUT_FILENAME, "rb") as input_file:
        compressed_data = input_file.read()

    # Decompress the data
    output_data = decompress(compressed_data)

    # Write the decompressed data to the output file
    with open(OUTPUT_FILENAME, "wb") as output_file:
        output_file.write(output_data)
