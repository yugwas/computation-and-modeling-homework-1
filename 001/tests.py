from code import check_for_symmetry
from code import get_union
from code import get_first_n_terms_nonrecursive
from code import get_nth_term_recursive
from code import convert_to_decimal
from code import convert_to_binary


# check_for_symmetry tests

if (check_for_symmetry('tacocat')) == False:
    print ("Input is not symmetrical.")

#######################################################

# get_intersection

list1 = [15, 20, 30, 45, 60, 70]
list2 = [10, 15, 30, 60, 65, 80]
list3 = []

# get_intersection
for i in list1:
    for y in list2:
        if y == i:
            list3.append(i)

if list3 == []:
    print ("Lists do not share an intersection.")

#######################################################

# get_union tests

if list == []:
    print ("Please try again. Failed to get union of lists.")

#######################################################

# count_characters(input_string)

input_string = "hello"
character_count = {}

for i in input_string:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1
  
if input_string == 0:
    print ("Please try again.")

#######################################################

# get_first_n_terms_nonrecursive(n) test code

if get_first_n_terms_nonrecursive == 0:
    print ("Failed to get terms of nonrecursive function. Please try again.")


#######################################################

# recursive test code

if get_nth_term_recursive == 0:
    print ("Failed to get term of recursive function. Please try again.")

#######################################################

#convert to base 10 test code

binary_num = "10011"

if (convert_to_decimal(binary_num)) != 19:
    print ("Failed to convert to decimal. Please try again.")

#######################################################

# convert to base 2 test code

decimal_num = 19

if (convert_to_binary(decimal_num)) != "10011":
    print ("Failed to convert to binary. Please try again.")