from sys import argv, exit
import re, csv

if len(argv) != 3:
    print("Errno #1 - Two arguments required")
    exit(1)

with open(argv[1], mode= 'r') as file1, open(argv[2], mode='r') as file2:
    if not re.search(r'.csv$', argv[1]) and not re.search(r'.txt$', argv[2]):
        print("Errno #2 - File type order required.\nUsage: path/filename.csv path/filename.txt")
        exit(2)
    else:
        dictionary = csv.DictReader(file1, delimiter= ',')
        tandemList = []
        for rows in dictionary:
            nucleotides = ' '.join(rows)
            nucleotides = nucleotides.split()
            nucleotides.pop(0)
            tandemDict = {nuc: rows[nuc] for nuc in rows}
            tandemList.append(tandemDict)
                
        STRs = {}
        dnaSequence = file2.readline()
        for key in nucleotides:
            value = re.search(f"(?:({key}){{2,}}|({key}))", dnaSequence)
            value = int(len(value.group(0)) / len(key))
            STRs[key] = str(value)
        print(STRs)