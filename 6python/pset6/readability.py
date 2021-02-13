from cs50 import get_string

text = get_string("Text: ")
countLetters, countWords, countSentences = 0, 1, 0

for i in text:
    if (i.isalpha()):
        countLetters += 1
    elif (i == ' '):
        countWords += 1
    elif (i == '.' or i == '!' or i == '?'):
        countSentences += 1

def get_index(str):
    L = countLetters / countWords * 100
    S = countSentences / countWords * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)

grade = get_index(text)
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before grade 1")
else:
    print("Grade", grade)