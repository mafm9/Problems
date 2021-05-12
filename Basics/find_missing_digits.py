num = input("enter a number: ")
digits = {0,1,2,3,4,5,6,7,8,9}

for digit in num:
    if int(digit) in digits:
        digits.remove(int(digit))
print(f"the missing digits are: {digits}")
