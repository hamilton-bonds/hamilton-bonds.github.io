def palindrome(string):
    '''Returns true if `string` is a palindrome.'''
    return ''.join(list(string)) == ''.join(list(string)[::-1])

def importCSV(filename):
    '''Imports a CSV file and returns a dictionary of values in a list.'''
    lines = dict()
    with open(filename,'r') as infile:
        for x,line in enumerate(infile):
            lines[x] = line.strip().split(',')
        infile.close()
    return lines

def enumeration203(filename):
    lines = importCSV(filename)
    lines_strings = lines

    for n in lines_strings:
        ls = ''.join(lines_strings[n])
        if palindrome(ls):
            return ls
    return "None found in Enumeration 203."

if __name__ == '__main__':
    e203_ans = enumeration203("enum-flags203.csv")
    print("E203: ",e203_ans)
    e_ans = enumeration203("enum-flags.csv")
    print("E: ",e_ans)
    ed_ans = enumeration203("enum-dates.csv")
    print("ED: ",ed_ans)
