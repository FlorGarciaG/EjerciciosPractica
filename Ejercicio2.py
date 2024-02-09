for i in range(11):
    if (i==0):
        print(" " * 9 + "*")
    else:
        print(" " * (10 - i) + "0" * (2 * i - 1))