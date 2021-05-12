import sys
import os

print(f"Name of script: {os.path.basename(__file__)}")
print("arguments: ", end = '')
args = list(sys.argv)
for arg in args[1:]:
    print(f"{arg} ", end = '')