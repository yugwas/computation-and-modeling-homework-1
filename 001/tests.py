# Monday and Tuesday tests (8/23-8/24)

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return True
    else:
        return False

print(check_for_symmetry('tacocat'))
print(check_for_symmetry('leaf'))

# Wednesday, Thursday, and Friday tests (8/25-8/27)

list1 = [15, 2, 3, 4, 80, 69, 100, 20, 40]
list2 = [30, 50, 60, 70, 100]
list3 = []

for i in list1:
    for y in list2:
        if y == i:
            list3.append(i)

print(list3)


########
#def get_intersection(list1, list2):
#get_union
#count_characters(input_string)

#Notes from Justin: don't use any built in libraries, just do it from scratch. Also, don't use python sets.
#
