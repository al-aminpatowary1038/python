a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
temp=0
if a>b :
    l=a
    s=b
    while a%b!=0:
        temp = a%b
        a= b
        b=temp
    Gcd = b
    print(f"GCD = {Gcd}")
    Lcm = (l*s)//Gcd
    print(f"LCM = {Lcm}")
else:
    l=b
    s=a
    while b%a!=0:
        temp = b%a
        b= a
        a=temp
    Gcd = a
    print(f"GCD = {Gcd}")
    Lcm = (l * s)//Gcd
    print(f"LCM = {Lcm}")