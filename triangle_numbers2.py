def triangle_numbers(n):
    lst1 = []
    for i in range(1,n+1):
        lst1.append(i)
    start =0
    end = 1
    for i in range(0,n+1):
        print lst1[start:end]
        start = end
        end += i + 2
    print lst1

triangle_numbers(16)





