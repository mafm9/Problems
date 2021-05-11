string = input("Please enter string: ")
character = input("Please enter specific character: ")
count = 0
for i in string:
    if i.casefold() == character.casefold():
        count = count+1
print(f"the number of {character}s in the string is {str(count)}")
