def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def strong_num(number):
    """Determine if a number is a strong number."""
    num_str = str(number)
    total = 0
    for digit in num_str:
        total += factorial(int(digit))
    if total == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
