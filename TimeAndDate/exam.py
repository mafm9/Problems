import datetime
exam_start = input("exam start date in MM-DD-YYYY format: ")
exam_list = input("Input exams in subject1-subject2-etc format: ").split('-')
exam_start = list(map(int,exam_start.split('-')))
exam_date = datetime.date(exam_start[2],exam_start[0],exam_start[1])
for exam in exam_list:
    print(f"{exam}: {exam_date.month}-{exam_date.day}-{exam_date.year}")
    exam_date = exam_date.replace(month=exam_date.month+1)