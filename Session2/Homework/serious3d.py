for i in range(10):
    for j in range(10):
        if (j + i)%2 == 0:
            print("1", end = "  ")
        else:
            print("0", end = "  ")
    print()

m = int(input("Enter a number: "))
for k in range(m +1):
    for l in range(m+1):
        if (k+l)%2 == 0:
            print("1", end = "  ")
        else:
            print("0", end = "  ")
    print()
