def fibonacci(n: int) -> int:
    """
    build a classic fibonacci function - No RECURSION
    """
    #given (n), value of x(n)?
    # take in an integer
    #without the use of recursion

    fibonacci_number_one = 0
    fibonacci_number_two = 1
    if n < 0:
        print("invalid number")
    elif n == 0:
        return fibonacci_number_one
    elif n == 1 or n == 2:
        return fibonacci_number_two
    else:
        for i in range(2, n+1):
            fibonacci_number_three = fibonacci_number_one + fibonacci_number_two
            fibonacci_number_one = fibonacci_number_two
            fibonacci_number_two = fibonacci_number_three
        return  fibonacci_number_two
