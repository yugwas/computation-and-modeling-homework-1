# convert to base 2 test code

decimal_num = 19

def convert_to_binary(decimal_num):
    binary_num = ""
    divided_num = decimal_num//2
    remainder = divided_num % 2;
    binary_num += str(remainder)
    while(True):
        if (divided_num == 0):
            break;
        divided_num = divided_num//2
        remainder = divided_num % 2 
        print(divided_num)
        binary_num += str(remainder)
    return binary_num

print(convert_to_binary(19))
        
