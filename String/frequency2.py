inputstring = "Peter piper picked a peck of pickled peppers Peter"
character_list = [x for x in inputstring[::]]
print(character_list)
frequency = [character_list.count(x) for x in character_list]
combined = dict(list(zip(character_list,frequency)))
print({k:v for (k,v) in combined.items() if v > 1})