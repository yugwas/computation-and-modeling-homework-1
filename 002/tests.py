
message = ("This is my message!").dict

def encoding_function(input):
    input = []
        if i != 0:
            input.append(encoding_function(input))
    return 3*input - 4

print (encoding_function(message))

