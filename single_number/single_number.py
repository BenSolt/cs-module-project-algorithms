'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    
    #multiply 2 times the sum of array 
    # 1. 2 *  [1 + 4 + 5 + 3 + 9 + 0] = 22
    # 2.  2 * 22 = 44
    # 3. 44 - sum of all numbers [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0] = 25
    # 4. 44 - 25 = 9?
    return 2 * sum(set(arr)) - sum(arr)



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")