example = "0001001111000000001011011000110101011010100001111011101111100111011010100011000101000100100001100111001011111111000111100011101000000110100101010011111100101010011100000100101101111100001111001111101001100011011100000111010110010111000011010110111011101100110110100101000100110110100110011010011000011010101100011010011001000011000000111011011111000110000010000101011010101111110001111001100110100110000000000111101001010000101011111011001100000101100001000011001100100001000011001010111111100001111010010001101111000000001101001111000111101010101100110110100111001100010011110011110000000100001111111010000111001111111010011100001000111100011101011011111111111011111100000000110100110001001111110001110011010101011100110000001111001110010110100001100001010100101111011000010101001111110011111110011000111100100001000011110111100001110010111101000001011011000101011011010110111110011100110110010010001110111100101001100101001010011011101100101111100111"

print(len(example) / 8)
#quit()



bit_sets = []

for i in range(0,len(example),7):
    bit_sets.append(example[i:i+7])
  
  
  
"""
    assign p0 = data_in[3] ^ data_in[2] ^ data_in[0];
    assign p1 = data_in[3] ^ data_in[1] ^ data_in[0];
    assign p2 = data_in[2] ^ data_in[1] ^ data_in[0];
"""  

def xor(a,b,c):
    return a ^ b ^ c

def calc(di0,di1,di2,di3,p0,p1,p2):
    stream = [p0,p1,di3,p2,di2,di1,di0]
    print("ORIGINAL STREAM: {}".format(stream))
    parity0 = xor(di3,di2,di0)
    parity1 = xor(di3,di1,di0)
    parity2 = xor(di2,di1,di0)
    
    parity = "{}{}{}".format(p0,p1,p2)
    if parity == "000":
        return stream
    
    error_pos = ["100","010","001","011","101","110","111"]
    correct_this_bit = error_pos.index(parity)
    print("BIT {} FAILED. PARITY: {}".format(correct_this_bit,parity))
    
    stream[correct_this_bit] = int(not(stream[correct_this_bit]))
    print("NEW STREAM: {}".format(stream))
    
    di0,di1,di2,di3 = stream[6],stream[5],stream[4],stream[2]
    parity0 = xor(di3,di2,di0)
    parity1 = xor(di3,di1,di0)
    parity2 = xor(di2,di1,di0)
    
    parity = "{}{}{}".format(p0,p1,p2)
    if parity == "000":
        return stream
    else:
        print("BIT {} FAILED. PARITY: {}".format(correct_this_bit,parity))
        quit()
    
    return stream
        
bits = ""
corrections = 0
for bs in bit_sets:
    p0 = int(bs[0])
    p1 = int(bs[1])
    di3 = int(bs[2])
    p2 = int(bs[3])
    di2 = int(bs[4])
    di1 = int(bs[5])
    di0 = int(bs[6])
    
    # all correct = 0
    # not correct = 1
    corrected_bits = calc(di0,di1,di2,di3,p0,p1,p2)
    di0,di1,di2,di3 = corrected_bits[6],corrected_bits[5],corrected_bits[4],corrected_bits[2]
    #add_these = [di0,di1,di2,di3]
    add_these = [di3,di2,di1,di0]
    bits += "".join([str(at) for at in add_these])
    
s = ""
for i in range(0,len(bits),8):
    s += hex(int(bits[i:i+8],2))[2:].zfill(2)
    
print(s)


