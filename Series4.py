#1 + 1/2 + 1/3 + ..... + 1/n
n = int (input("Enter the last number: "))
total = 0
for i in range( 1 , n+1):
    total = total + 1/i

print(total)