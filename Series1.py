#1+2+3+4+....+n
num =  int(input("Enter The last number: "))
total = 0
for i in range(1,num+1,1):
    total =total + i
print(total)