string1 = "1,2,3"
string2 = "a,b,c"
white_space = "      abc       "

sep = string1.split(',')
print(sep)
print(string1[0])
print(string1[0:4])

print(string1.join(string2))
print(string1 + ",4")
print(f"string formatting example: {string1}")
substring = "1" in string1
print(substring)
print(white_space)
print(white_space.strip())