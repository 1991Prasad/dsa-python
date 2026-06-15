n= 15
m= 6

def closest_number(n,m):
    distance = 0


    while True:
        lower = n - distance
        upper = n + distance

        if lower % m == 0 and upper % m ==0:
            return lower if abs(lower)>abs(upper) else upper
        
        if lower % m == 0:
            return lower


        if upper % m == 0:
            return upper

        distance += 1

print(closest_number(n,m))
