import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr[ : ] = 0
print(arr)

#multiply all elements that are less than 3, by 10
#arr[arr<3] = (arr[arr<3])*10
# now, arr = [10, 20, 3, 4, 5]

#explanation
    # A = B*10
        # A and B are 2 arrays of the same shape
        # we are changing array A 
    # Example
        # A = [1, 4, 7]
        # B = [2, 1, 5]
        # A = B*10 ----> A = [20, 10, 50]