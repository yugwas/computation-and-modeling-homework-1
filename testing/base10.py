#convert to base 10 test code

binary_num = "10011"

def convert_to_decimal(binary_num):
    decimal_num = 0
    length_of_num = len(binary_num) - 1
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[i]) * 2**(length_of_num -i)
    return decimal_num

print(convert_to_decimal(binary_num))