lowerbound = int(input("Please enter lower bound of range: "))
upperbound = int(input("Please enter upper bound of range: "))
variance = int(input("please enter variance: "))
number = int(input("Please enter number: "))

if (number < lowerbound + variance and number > lowerbound - variance) or (number > upperbound - variance and number < upperbound + variance):
    print(f"{number} is within variance of range limits")
else:
    print(f"{number} is out of variance of range limits")


