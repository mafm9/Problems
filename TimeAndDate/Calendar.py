import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
date = input("Enter calendar month and year ie 5,2020: ").split(',')
date = list(map(int,date))
print(c.formatmonth(date[1],date[0]))