'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here


    # a = 1
    # # for each index in array
    # for i in arr: 
    #     a*= i 
    # #for each index in array
    # for i in arr: 
    #     #print integer(1)
    #     print(int(a*(i**-1)))

    # return arr


    n = len(arr)     

    left = [0]*n  
    right = [0]*n  
  
    prod = [0]*n  
  
    left[0] = 1
    right[n - 1] = 1
  
    # left array  
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
  
    # right array  
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
   
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    for i in range(n):  
        print(prod[i], end =' ')  
    
    return prod
   
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")




# import math 
# EPS = 1e-9
  
# def productPuzzle(a, n): 
     
#     # to hold sum of all values 
#     sum = 0
#     for i in range(n): 
#         sum += math.log10(a[i]) 
      
#     # output product for each index 
#     # antilog to find original product value 
#     for i in range(n): 
#         print (f"{int((EPS + pow(10.00, sum - math.log10(a[i]))))}"), 
      
#     return
   
# # Driver code 
# a = [10, 3, 5, 6, 2 ] 
# n = len(a) 
# print (f"The product array is: {productPuzzle(a, n)}")
  