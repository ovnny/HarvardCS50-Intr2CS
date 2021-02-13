import re

STRsequence = 'AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG'
STRcount = re.finditer('(AGATC){2,}|(AGATC)', STRsequence)
count = 0
for match in STRcount:
    if count > 1:
        count += 1
    else:
        count == 1
    print(match for STRcount in match)


    regex: '(TATC){2,}?| (?!TATC)'