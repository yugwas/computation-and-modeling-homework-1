
# get_first_n_terms_nonrecursive(n) test code

def recursive_function(last_term):
    return 3*last_term - 4


def get_first_n_terms_nonrecursive(num_terms):
    terms = []
    for i in range(num_terms):
        if i != 0:
            terms.append(recursive_function(terms[i-1]))
        else:
            terms.append(5)
    return terms

print(get_first_n_terms_nonrecursive(4))



