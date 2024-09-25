def factorial(num, show=False):
    """
    -> calculate the factorial of any number
    :param num: We have the number we will be factorial
    :param show: True with you want to check the account
    :return: The value of the num factorial
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
        if c >   1:
            print('x', end=' ')
        else:
            print('=', end=' ')
        f *= c
    print(f'{f}')




print(factorial(5, show=True))
help(factorial)