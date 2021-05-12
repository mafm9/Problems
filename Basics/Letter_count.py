input_string = input("Input any string: ")

input_string = input_string.lower()
vowel_count = 0
consonant_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in input_string:
    if letter in vowels:
        vowel_count+=1
    else:
        consonant_count+=1

print(f"Consonant count: {str(consonant_count)}")
print(f"Vowel count: {str(vowel_count)}")