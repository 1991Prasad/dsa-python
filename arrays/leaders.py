arr = [16, 17, 4, 3, 5, 2]
# arr = [1, 2, 3, 4, 5, 2]

def leaders(arr):
    result = []
    n = len(arr)
    
    for i in range(n): # O(n)
        for j in range(i + 1,n): # O(n)
            if arr[j]>arr[i]:
                break
        else:
            result.append(arr[i])

    return result

# print(leaders(arr))


def leaders_optimal(arr):
    
    
    n = len(arr)
    max_so_far = arr[n-1]
    result = []
    for i in range(n-1,-1,-1):
        if arr[i] >= max_so_far:
            max_so_far = arr[i]
            result.append(arr[i])
    result.reverse()
    return result
    

print(leaders_optimal(arr))

# Your approach in words
# here we will have one outer loop which takes one value
# Then we can have 2nd loop which compares the same with the value of outer loop if it is greater the loop breaks 
# but if it is smaller it checks next value and so on if there does not exist the value of outer loop is clear leader 
# we will then appen it to the result arr which we have created

# My code 
# arr = [16, 17, 4, 3, 5, 2]
# # arr = [1, 2, 3, 4, 5, 2]

# def leaders(arr):
#     result = []
#     n = len(arr)
    
#     for i in range(n): # O(n)
#         for j in range(i + 1,n): # O(n)
#             if arr[j]>arr[i]:
#                 break
#         else:
#             result.append(arr[i])

#     return result

# print(leaders(arr))

# My analysis

# Time Complexity: Since we have used 2 loops each loops does O(n) work hence it becomes O(n^2) 
# Space Complexity: we have used an extra array result so it becomes O(1) and n variable also becomes O(1) and then loop bookkeeping, so overall it becomes O(1)
# Whether you think it's optimal: I think there exist a optimal solution to this which has O(n) time complexity.
