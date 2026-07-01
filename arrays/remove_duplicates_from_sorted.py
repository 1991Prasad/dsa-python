# Create a list
# fruits = ["apple", "banana", "cherry", "banana"]
# print(fruits)
# # Actions
# # fruits.append("orange")         # ["apple", "banana", "cherry", "orange"]
# # fruits.insert(1, "blueberry")   # ["apple", "blueberry", "banana", "cherry", "orange"]
# fruits.remove("banana")         # ["apple", "blueberry", "cherry", "orange"]
# # fruits[0] = "strawberry"        # Modifies first item
# print(fruits)
# Process each item
# for fruit in fruits:
#     print(fruit.upper())


# #Brute Force 1 
# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# # arr = [5, 1, 4, 1, 2, 5, 3]
# # arr = [5, 5, 5, 5, 5, 5]

# def remove_dup_sorted_array(arr):
#     result=[]
#     for i in arr: # O(n)
#         if i not in result: # O(n)
#             result.append(i) # O(1)

#     return result        


# print(remove_dup_sorted_array(arr))            

# # TC = O(n) * O(n) = O(n^2)
# # SC = O(n)      



# # Brute Force 2
# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# # arr = [5, 1, 4, 1, 2, 5, 3]
# # arr = [5, 5, 5, 5, 5, 5]

# def remove_dup_sorted_array(arr):
#     seen=set()
#     result =[]
#     for i in arr: # O(n)
#         if i not in seen: # O(1)
#             seen.add(i)
#             result.append(i) # O(1)

#     return result        


# print(remove_dup_sorted_array(arr))      


# Optimal Solution
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]

def remove_dup_sorted_array_optimal(arr):
    write = 0
    for read in range(1,len(arr)):
        if arr[write] != arr[read]:
            write += 1
            arr[write] = arr[read]

    return arr

print(remove_dup_sorted_array_optimal(arr))


