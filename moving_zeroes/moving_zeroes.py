'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    a = arr
    b = arr
    if (a == b): 
        return a 
        # return(set(arr))
    else: 
        # Create empty list (array)
        arr2 = [] 
  
        while(a < b+1 ): 
            #add to empty list
            arr2.append(a) 
            #add plus 1
            a += 1
        return arr2 
        # return(set(arr))
        
  


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")