name_list = input("Enter list of names seperated by commas: ").split(",")
D_name_list = list(filter(lambda x: x.startswith('d') or x.startswith('D'), name_list))
print(D_name_list)