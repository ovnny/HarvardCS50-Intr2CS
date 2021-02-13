from sys import argv, exit
import re, csv

# Certifying there's exactly 3 arguments in the command line
if len(argv) != 3:
    print("Errno #1 - Two arguments required")
    exit(1)
# Open both files at the same time and certifying the correct format of those
with open(argv[1], mode= 'r') as file1, open(argv[2], mode='r') as file2:
    if not re.search(r'.csv$', argv[1]) and not re.search(r'.txt$', argv[2]):
        print("Errno #2 - File type order required.\nUsage: path/filename.csv path/filename.txt")
        exit(2)
    else:

        # If all initial requests are attended, read the csv file and extract data to analyze
        dictionary = csv.DictReader(file1, delimiter= ',')

        # that list will be used to append the Nucleotides Sequences for later to use as keys to find STRs
        tandemList = []
        for rows in dictionary:
            nucleotides = ' '.join(rows)
            nucleotides = nucleotides.split()
            nucleotides.pop(0)
            tandemDict = {nuc: rows[nuc] for nuc in rows}
            tandemList.append(tandemDict)

        # That dictionary will be used to put the total number of times of keys repeat in a given DNA sequence
        STRs = {}
        dnaSequence = file2.readline()

        # Using a self-made regular expression on each nucleotide to parse the DNA sequence and find these STRs
        for key in nucleotides:
            value = re.search(f"(?:({key}){{2,}}?\B({key})+)", dnaSequence, re.X)

            #conditional to verify if no pattern was founded. If not, set the value to a single one nucleotide base (i.e: 1)
            if re.search(f"(?:({key}){{2,}})", dnaSequence, re.X) is not None:
                value = int(len(value.group()) / len(key))
            else:
                value = 1
            # Set the keys and values of our dictionary to {STRs: values}
            STRs[key] = str(value)

        # Comparing the csv list of dictionaries with our dictionary and match then
        for person in range(len(tandemList)):
            name = tandemList[person].pop('name')
            if STRs == tandemList[person]:
                # If it succeeds, prints the corresponding DNA owner name. If not, print it!
                print(name)
                break
        else:
            print("No match")
            exit(0)
            # If all succeeds, escape!