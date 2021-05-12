num_list = input("Enter list of numbers seperated by commas: ").split(",")
nums = list(map(int,num_list))
constrained_squares = [x**2 for x in nums if x>10 and x<50]
print(constrained_squares)