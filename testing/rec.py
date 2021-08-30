# recursive test code


def get_nth_term_recursive(n):
    if n == 1:
        return 5
    else:
        return 3* get_nth_term_recursive(n-1) - 4

print(get_nth_term_recursive(4))

#[5, 11, 29, 83]

