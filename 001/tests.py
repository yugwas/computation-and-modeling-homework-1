
def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return "Word is symmetrical."
    else:
        return "Word is not symmetrical."

print(check_for_symmetry('tacocat'))
print(check_for_symmetry('leaf'))
