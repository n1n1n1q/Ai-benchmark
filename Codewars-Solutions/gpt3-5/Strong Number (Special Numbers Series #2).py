def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def strong_num(number):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
    if sum_of_factorials == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
