# convert to base 2 test code


n = int(input("Enter decimal value: "))
base_2 = ''

while n != 0:
    base_2 = base_2 + str(n%2)
    n = n//2
print ("Decimal value in Binary is: ")
for i in range (len(base_2) -1, -1, -1):
    print (base_2[i], end = '')