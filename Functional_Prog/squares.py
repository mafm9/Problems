nums = input("enter list of numbers to square: ")
nums = nums.split()
nums = list(map(int,nums))
print(list(map(lambda x: x**2, nums)))

