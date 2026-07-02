arr = [1, 2, 3]

def generating_all_subarrays(arr):
    n = len(arr)
    for i in range(n):
        
        for j in range(i,n):
            
            for k in range(i,j+1):
                
                print(arr[k], end=" ")
                
            print()


generating_all_subarrays(arr)
