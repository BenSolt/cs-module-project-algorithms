'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    # k = to how big array of group nums selected is [ 0,0,0 ] this case = 3.

    # maxx = 0
    # numblength = len(nums)
    # # for i in range of (len(nums) - k + 1)
    # for i in range(numblength - k + 1):
    #     maxx = nums[i]
    #     for j in range(1, k):
    #         if nums[i + j] > maxx:
    #             maxx = nums[i + j]
    #     print(str(maxx) + " ", end = "") 

    # return maxx
    

    maxx = 0
    n = len(nums)

    for i in range(n - k + 1): 
        maxx = nums[i]
        current_sum = 0
        for j in range(k): 
            current_sum = current_sum + nums[i + j] 
  
        # Update result if required. 
        maxx = max(current_sum, maxx ) 
  
    return maxx
       


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")


