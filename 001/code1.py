
def sum_of_first_n_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_first_n_numbers(n-1)


print("The sum of the first n numbers is", sum_of_first_n_numbers(n))