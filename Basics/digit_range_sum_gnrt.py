def digit_range_sum_gnrt(d, n):
    str_nums = []
    for i in range(1,n+1):
        str_nums.append(str(d)*i)
    
    print(str_nums)
    int_nums = list(map(int,str_nums))
    total = sum(int_nums)

    print(total)


digit_range_sum_gnrt(5,3)
