#2+4+6+8+.....+n
n = int(input("Enter the last number: "))
total = 0
for  i in range(2,n+1,2):
    total = total +i
print(total)