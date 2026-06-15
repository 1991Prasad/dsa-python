#find closest_number to n but divisible by m


n = 15
m = 6

def closest_number(n,m):
    distance = 0

    while True:
        lower = n - distance
        upper = n + distance

        if lower % m == 0 and upper % m == 0:
            print("hello")
            return lower if abs(lower) > abs(upper) else upper

        if lower % m == 0:
            print("hello20")
            return lower 
        
        
        if upper % m == 0:
            print("hello25")
            return upper
        
        distance = distance + 1

print(closest_number(n,m))