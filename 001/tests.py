# Monday and Tuesday tests (8/23-8/24)

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return True
    else:
        return False

print(check_for_symmetry('tacocat'))
print(check_for_symmetry('leaf'))

#######################################################

# Wednesday, Thursday, and Friday tests (8/25-8/27)

list1 = [15, 20, 30, 45, 60, 70]
list2 = [10, 15, 30, 60, 65, 80]
list3 = []

# get_symmetry test code
for i in list1:
    for y in list2:
        if y == i:
            list3.append(i)

print(list3)

#######################################################

# get_union test code
for i in list1:
    for y in list2:
        if y == i:
            list1.remove(i)

print(list1, list2)


for i in list1:
    for y in list2:
        if y == i:
            list2.remove(y)

print(list1, list2)

# both code above works without printing any repeats


# now i need to make it into a function that prints out only 1 list

list1 = [15, 20, 30, 45, 60, 70]
list2 = [10, 15, 30, 60, 65, 80]
list3 = []

getunion = list({i: i for i in list1 + list2}.values())

print (getunion)
# i rewrote the whole thing because I couldn't figure out how to combine the lists

#######################################################

# count_characters(input_string)

input_string = "hello"
character_count = {}
  
for i in input_string:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1
  
print (str(character_count))

#######################################################

# get_first_n_terms_nonrecursive(n) test code

# getfirstntermsnonrecursive(n): Returns the firstnterms of the sequencean= 3an−1−4, a1= 5,using aforloop.



x = 10
for x in input:
  input = 3(n-1)-4