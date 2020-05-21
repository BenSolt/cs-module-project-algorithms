'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    count = 0
    n = len(arr)
      
    for i in range(n):
        #if array index does not equal 0
        if arr[i] != 0: 
            #add + 1
            arr[count] = arr[i] 
            count+=1
    #while count less than len(arr)  
    while count < n: 
        arr[count] = 0
        count += 1

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")