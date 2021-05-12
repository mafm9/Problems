list1 = input("Enter values for list one seperated by commas: ").split(",")
list2 = input("Enter values for list two seperated by commas: ").split(",")

combined_list = [(i,j) for i in list1 for j in list2]

print(combined_list)