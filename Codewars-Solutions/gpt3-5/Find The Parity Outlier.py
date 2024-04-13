def find_outlier(integers):
    odd_count = even_count = 0
    odd_number = even_number = 0

    for num in integers:
        if num % 2 == 0:
            even_count += 1
            even_number = num
        else:
            odd_count += 1
            odd_number = num

    return even_number if odd_count > even_count else odd_number
