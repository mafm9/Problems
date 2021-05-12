value = ""
while value != 'exit':
    value = input("Enter a value: ")
    
    if value.isnumeric():
        print(f"{value} is numeric")
    elif value.isalpha():
        print(f"{value} is alpha")
    elif value.isalnum():
        print(f"{value} is alphanumeric")
