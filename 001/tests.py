# Monday and Tuesday tests (8/23-8/24)

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return True
    else:
        return False


if (check_for_symmetry('tacocat')) == False:
    print ("Input is not symmetrical.")

#######################################################

# Wednesday, Thursday, and Friday tests (8/25-8/27)

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

# get_union test code

list1 = [15, 20, 30, 45, 60, 70]
list2 = [10, 15, 30, 60, 65, 80]

getunion = list({i: i for i in list1 + list2}.values())

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


if get_first_n_terms_nonrecursive == 0:
    print ("Failed to get terms of nonrecursive function. Please try again.")


#######################################################

# recursive test code


def get_nth_term_recursive(n):
    if n == 1:
        return 5
    else:
        return 3* get_nth_term_recursive(n-1) - 4

#[5, 11, 29, 83]

if get_nth_term_recursive == 0:
    print ("Failed to get term of recursive function. Please try again.")

#######################################################

#convert to base 10 test code

binary_num = "10011"

def convert_to_decimal(binary_num):
    decimal_num = 0
    length_of_num = len(binary_num) - 1
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[i]) * 2**(length_of_num -i)
    return decimal_num

if (convert_to_decimal(binary_num)) != 19:
    print ("Failed to convert to decimal. Please try again.")

#######################################################

# convert to base 2 test code

decimal_num = 19

def convert_to_binary(decimal_num):
    if decimal_num == 1:
        return 1
    binary_num = ""
    divided_num = decimal_num//2
    remainder = divided_num % 2;
    binary_num += str(remainder)
    while(divided_num != 0):
        if (divided_num == 1):
            binary_num+="1"
            break;
        divided_num = divided_num//2
        remainder = divided_num % 2 
        binary_num += str(remainder)
    return binary_num

if (convert_to_binary(decimal_num)) != "10011":
    print ("Failed to convert to binary. Please try again.")