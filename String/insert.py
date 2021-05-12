word = "abc"
empty = "[{}]"
empty = empty[:2] + word + empty[2:]
print(empty)