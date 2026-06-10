num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print("\n")
if num1 > num2 and num1 > num3 :
    print(f"{num1} is Large Number")
    
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is Large Number")
    
else: 
    print(f"{num3} is Large Number")
