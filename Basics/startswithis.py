input_string = input("Please input a string: ")

if input_string.startswith('Is'):
    print(f"Unchanged: {input_string}")
else:
    print('Changed: Is'+ input_string)
    