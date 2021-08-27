# Monday and Tuesday code (8/23-8/24)

txt = input("type here to see if your word is symmetrical: ")

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
       return True
    else:
        return False


print(check_for_symmetry(txt))

# Wednesday, Thursday, and Friday code (8/25-8/27)

list1 = [100, 200, 500, 600, 900]
list2 = [200, 400, 500, 800, 900]
list3 = []

def get_intersection(list1, list2):
    for i in list1:
        for y in list2:
            if y == i:
                list3.append(i)

print(list3)