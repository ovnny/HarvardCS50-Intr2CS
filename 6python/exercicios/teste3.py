from sys import argv, exit
import re, csv

if len(argv) != 3:
    print("Errno 1: Two arguments required\nUsage: sequences/filename.csv database/filename.txt")
    exit(1)

    with open(argv[1], mode= 'r') as csv_file, open(argv[2], mode= 'r') as txt_file:
        if not re.search('csv$', argv[1]) and not re.search('txt$', argv[2]):
            print("Errno 2: a csv and txt files are required\nUsage: sequences/filename.csv database/filename.txt")
            exit(2)
        else:
            dictionary = csv.DictReader(csv_file, delimiter= ',')
            for row in dictionary:
                [STRtypes] = [" ".join(row)]
                STRtypes = STRtypes.split()
                STRtypes.pop(0)
                print(row)