n = input("Enter a text of number: ")
List =  n.split()

total = 0
for i in List:
    total = total + int(i)
print(f"Sum = {total}")