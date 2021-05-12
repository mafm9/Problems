num_list = input("Enter list of numbers seperated by commas: ").split(",")
num_list = list(map(int,num_list))
even_list = list(filter(lambda x: x%2 == 0, num_list))
print(even_list)
