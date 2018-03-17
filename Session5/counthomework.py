number = [1,6,8,1,2,1,5,6]
digit = int(input("Enter a number: "))
times = number.count(digit)
print(digit,"appears",times,"times in my list")

count = len([i for i in number if i == digit] )
print(digit,"appears",count,"times in my list")
