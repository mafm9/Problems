num_list = input("Enter list of numbers seperated by commas: ").split(",")
nums = list(map(int,num_list))
even_list = [x for x in nums if x%2 == 0]
print(even_list)