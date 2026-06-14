#1^2 + 2^2 + 3^2 + .... + n^2
n  = int(input("Enter the last number: "))
total = 0
for i in range( 1, n+1, 1):
    total = total + ( i * i )
print(total)