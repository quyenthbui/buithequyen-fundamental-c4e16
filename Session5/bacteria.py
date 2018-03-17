initial = int(input("How many B bacterias are there ? "))
time = int(input("How much times in minutes will we wait? "))
result = initial*(2**(time/2))
print("After", time, 'minutes, we would have', result,'bacterias' )
