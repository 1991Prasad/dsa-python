a= 10
b= 20

# 1. Using Arithematic function
def swap_number(a,b):
    a = a+b # 10 + 20 = 30
    b = a-b # 30 - 20 = 10
    a = a-b # 30 - 10 = 20
    return a,b

print(swap_number(a,b))



# 2. Using python swap
a= 10
b= 20

def swap_number(a,b):
    a, b= b, a
    return a,b

print(swap_number(a,b))


# 3. Using bitwise XOR
a= 10
b= 20
def swap_number(a,b):
    a= a^b
    b= a^b
    a= a^b
    return a,b

print(swap_number(a,b))
