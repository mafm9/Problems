input_string = input("Input any string: ")

input_string = input_string.lower()
unique_vowel_count = 0
vowels = {'a': False, 'e' : False, 'i': False, 'o': False, 'u':False}

for letter in input_string:
    for key in vowels:
        if letter == key and vowels[key] == False:
            vowels[key] = True
            unique_vowel_count += 1
        


print(f"Unique Vowel count: {str(unique_vowel_count)}")