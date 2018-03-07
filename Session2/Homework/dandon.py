n = int(input("Choose word size:"))
m = 2*n +3
l = 4*(n +3)
for i in range (1, m+1):
    for j in range(1, l):
        if j%(n+3) == 0:
            print("  ", end = "")
        elif 1 < i < m :
            if 1 < j < n + 3 or n+4 < j < 2*n + 5 or 2*n + 7 < j < 3*n + 8  :
                print("  ", end = "")
            elif j >= l - n -1:
                if i == (m+1)/2:
                    print("* ", end = "")
                else:
                    print("  ", end = "")
            else:
                print("* ", end = "")
        elif j == 3*(n+3)-1:
            if i == 1 or i == m:
                print("  ", end = "")
            else:
                print("* ", end = "")
        else:
            print("* ", end = "")
    print()
