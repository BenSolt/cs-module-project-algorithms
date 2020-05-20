'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    # k = to how big array of group nums selected is [ 0,0,0 ] this case = 3.

    maxx = 0
    numbs = len(nums)

    for i in range(numbs - k + 1):
        maxx = nums[i]
        for j in range(1, k):
            if nums[i + j] > maxx:
                maxx = nums[i + j]
        print(maxx) 



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
