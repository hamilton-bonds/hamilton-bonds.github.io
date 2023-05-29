import math

def import_file(FILEPATH):
    data = dict()
    with open(FILEPATH,"r") as infile:
        for x,line in enumerate(infile):
            data[x] = line.strip()
    return data
    
def reoccurrences(data):
    reoc = dict()
    for e in data:
        value = data[e]
        values_list = list(data.values())
        if value in values_list:
            if value in reoc:
                reoc[value].append(e)
            else:
                reoc[value] = [e]
    return reoc

def import_csv(FILEPATH):
    data = dict()
    with open(FILEPATH,"r") as infile:
        for x,line in enumerate(infile):
            ll = line.strip().split(",")
            if x > 0:
                data[ll[0].upper()] = float(ll[1])
    return data

def get_most_frequent(guesses,letter_freqs):
    if len(guesses) == 0:
        return None
    if len(guesses) == 1:
        return guesses[0]
    for n,guess in enumerate(guesses):
        freq = letter_freqs[guess]
        if n == 0:
            most_frequent = guess
            biggest_freq = freq
        else:
            if freq > biggest_freq:
                most_frequent = guess
                biggest_freq = freq
    return most_frequent
    
def get_closest(guesses,target_freq,letter_freqs):
    if len(guesses) == 0:
        return None
    if len(guesses) == 1:
        return guesses[0]
    for n,guess in enumerate(guesses):
        freq = letter_freqs[guess]
        if n == 0:
            closest = guess
            closest_freq_delta = math.fabs(freq - target_freq)
        else:
            delta_f = math.fabs(freq - target_freq)
            if delta_f < closest_freq_delta:
                closest = guess
                closest_freq_delta = delta_f
    return closest

if __name__ == '__main__':
    FILEPATH = './output.txt'
    d = import_file(FILEPATH)
    ro = reoccurrences(d)
    for key in ro:
        val = ro[key]
        if len(val) < 5:
            print("{}: {}".format(key,val))
            
    letter_freqs = import_csv("freqs.csv")
    print(letter_freqs)
        
    print()
    total = 1478 # doc length
    PCT = 0.4

    g = {
         "3a17ebebf2bad9aa0dd75b37a58fe6ea":"H",
         "68d763bc4c7a9b0da3828e0b77b08b64":"T",
         "9673dbe632859fa33b8a79d6a3e3fe30":"B",
         "fbe86a428051747607a35b44b1a3e9e9":"{",
         "a94f49727cf771a85831bd03af1caaf5":"_",
         "c53ba24fbbe9e3dbdd6062b3aab7ed1a":"}",
         "5f122076e17398b7e21d1762a61e2e0a":"A",
         "200ecd2657df0197f202f258b45038d8":"S",
         "d178fac67ec4e9d2724fed6c7b50cd26":"U",
         "9673dbe632859fa33b8a79d6a3e3fe30":"B",
         "68d763bc4c7a9b0da3828e0b77b08b64":"T",
         "e9b131ab270c54bbf67fb4bd9c8e3177":"I",
         "d178fac67ec4e9d2724fed6c7b50cd26":"U",
         "8cbd4cfebc9ddf583a108de1a69df088":"O",
         "34ece5ff054feccc5dabe9ae90438f9d":"N"
        }

    '''SHELVED
         "200ecd2657df0197f202f258b45038d8":"O",
         "e9b131ab270c54bbf67fb4bd9c8e3177":"R",
         "4a3af0b7397584c4d450c6f7e83076aa":"A",
         "2190a721b2dcb17ff693aa5feecb3b58":"C",
         "f89f2719fb2814d9ab821316dae9862f":"L",
         "c87a7eb9283e59571ad0cb0c89a74379":"E"
    '''

    guess_string1 = ""
    guess_string2 = ""
    
    close_method = g
    
    guess_string = ""
    
    for i in range(1095,1129,1):
    #for i in range(total):
        block = d[i]
        locations = ro[block]
        len_locs = len(locations)
        block_freq = (len_locs / total)
        lo,hi = block_freq-(block_freq*PCT),block_freq+(block_freq*PCT)
        guesses = []
        for letter in letter_freqs:
            freq = letter_freqs[letter]
            if lo <= freq <= hi:
                guesses.append(letter)
                
        if block in close_method:
            #print(close_method[block])
            l = close_method[block]
            guess_string1 += l
            guess_string2 += l
            p = "  "
            guesses = []
        else:
            l = " "
            p = ""
            
        most_frequent = get_most_frequent(guesses,letter_freqs)
        if (most_frequent != None) and (l != " "):
            guess_string1 += most_frequent
        elif (most_frequent != None) and (l == " "):
            guess_string1 += "?"
        
        closest = get_closest(guesses,block_freq,letter_freqs)
        if (closest != None) and (l != " "):
            guess_string2 += closest
        elif (closest != None) and (l == " "):
            guess_string2 += "?"
        
        #print("{}{}:\t[{}]:\t{}\t->\t{}".format(p,block,l,block_freq,closest))
        if (closest != None) and (closest not in list(close_method.values())):
            close_method[block] = closest
            
        
        if block in close_method:
            l = close_method[block]
            guess_string1 += l
            guess_string2 += l
            p = "  "
            guesses = []
        else:
            l = " "
            p = ""
            
        guess_string += l
            
        print("{}{}:\t[{}]:\t{}\t->\t{}".format(p,block,l,block_freq,guesses))
    print(guess_string)
