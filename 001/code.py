# Monday and Tuesday code (8/23-8/24)

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return True
    else:
        return False

# Wednesday, Thursday, and Friday code (8/25-8/27)

# get_intersection code
list1 = [100, 200, 500, 600, 900]
list2 = [200, 400, 500, 800, 900]
list3 = []


for i in list1:
    for y in list2:
        if y == i:
            list3.append(i)

# get_union code

get_union = list({i: i for i in list1 + list2}.values())

# count_characters(inputstring) code

input_string = input("type here to see the character count of a word: ")
character_count = {}
  
for i in input_string:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1
  
print (str(character_count))

# get_first_n_termsnonrecursive(n) code

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

#######################################################

# recursive code

def get_nth_term_recursive(n):
    if n == 1:
        return 5
    else:
        return 3* get_nth_term_recursive(n-1) - 4

#######################################################

#convert to base 10 code

binary_num = "10011"

def convert_to_decimal(binary_num):
    decimal_num = 0
    length_of_num = len(binary_num) - 1
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[i]) * 2**(length_of_num -i)
    return decimal_num


#######################################################

# convert to base 2 code

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
