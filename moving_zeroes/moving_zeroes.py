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
  
    else: 
  
        # Create empty array
        res = [] 
  
        while(a < b+1 ): 
              
            res.append(a) 
            a += 1
        return res 
        
  


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")