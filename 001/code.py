txt = input("type here to see if your word is symmetrical: ")

def check_for_symmetry(input_string):
    if input_string == (input_string [::-1]):
        return True
        print("Word is symmetrical.")
    else:
        return False
        print("Word is not symmetrical.")


check_for_symmetry(txt)
