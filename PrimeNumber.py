import math
n = int(input("Enter a number to check prime: "))
count =0
for i in range(1, int(math.sqrt(n))):
    if n%2==0:
        count= count+1
        break

if count == 0:
    print("prime")
else:
    print("Not prime")