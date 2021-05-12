num_list = input("Enter list of numbers seperated by commas: ").split(",")
nums = list(map(int,num_list))
[print("#"*x) for x in nums]
