num_list = input("Enter list of numbers seperated by commas: ").split(",")
num_list = list(map(int,num_list))
divided_list = list(filter(lambda x: x%10 == 0, num_list))
print(divided_list)
