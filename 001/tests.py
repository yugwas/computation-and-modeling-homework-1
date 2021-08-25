
def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
        return True
    else:
        return False

print(check_for_symmetry('tacocat'))
print(check_for_symmetry('leaf'))
