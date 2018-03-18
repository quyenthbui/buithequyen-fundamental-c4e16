rabbit=[1,2]
for i in range(0,5):
    if i >1:
        rabbit.append(rabbit[i-2]+rabbit[i-1])
    number = rabbit[i]
    print("Month ",i,": ", number, "pair(s) of rabbit")
