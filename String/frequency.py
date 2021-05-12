inputstring = "Peter piper picked a peck of pickled peppers Peter"

words = inputstring.split()

frequency = [words.count(x) for x in words]
print(frequency)

combine = dict(list(zip(words,frequency)))
longest = max(words,key=len)
print(combine)
print(f"Longest words: {longest}")
print(f"length: {len(longest)}")