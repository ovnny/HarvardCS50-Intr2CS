from cs50 import get_string

cardNumber = [i for i in get_string("Number: ")]
reversedNumber = cardNumber[::-1]
sec2lastNumbers = reversedNumber[1::2]
lastNumbers = reversedNumber[::2]

for i in range(0, len(sec2lastNumbers)):
    sec2lastNumbers[i] = (int(sec2lastNumbers[i]) * 2)
    sec2lastNumbers[i] = str(sec2lastNumbers[i])
    sec2lastNumbersx2 = sec2lastNumbers[:]
product1 = ''.join(sec2lastNumbersx2)
product1 = [i for i in product1]

for i in range(0, len(product1)):
    product1[i] = int(product1[i])

for i in range(0, len(lastNumbers)):
    lastNumbers[i] = int(lastNumbers[i])
    product2 = lastNumbers

sumProducts = sum(product1) + sum(product2)
cardNumber2 = ("".join(cardNumber))

if sumProducts % 10 == 0:
    if len(cardNumber) == 15 and int(cardNumber2[:2]) == 34 or int(cardNumber2[:2]) == 37:
        print("AMEX")

    elif len(cardNumber) == 16 and int(cardNumber2[:2]) >= 51 and int(cardNumber2[:2]) <= 55:
        print("MASTERCARD")

    elif len(cardNumber) == 13 or len(cardNumber) == 16 and int(cardNumber2[0]) == 4:
        print("VISA")
else:
    print("INVALID")