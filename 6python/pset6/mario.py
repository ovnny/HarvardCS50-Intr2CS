while True:
    piramydHeight = int(input("Height? "))
    piramydRow = piramydHeight

    if piramydHeight > 0  and piramydHeight <= 8 and piramydHeight != str:
        for i in range(piramydRow):
            print(" " * (piramydHeight - 1), end="")
            piramydHeight -= 1
            print("#" * (piramydRow - piramydHeight))
        break