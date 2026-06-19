text = input("Enter any text or numbers: ")
numberOfWord =0 
numberOfDigit = 0
numberOfLetters = 0

for x in text:
    if x>='A' and x<='Z' or x>='a' and x<='z':
        numberOfLetters = numberOfLetters +1
    elif x>= '0' and x<= '9' :
        numberOfDigit = numberOfDigit + 1
    elif x == " " :
        numberOfWord = numberOfWord + 1

print(f"Number of Words : {numberOfWord + 1}")
print(f"Number of Letters : {numberOfLetters}")
print(f"Number of Digits : {numberOfDigit}")

