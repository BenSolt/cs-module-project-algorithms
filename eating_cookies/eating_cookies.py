'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

 # number of ways cookie monster can eat cookes.  
 # First = 1+1+1, Second = 2+1, Third = 1+2
    if i == 0:
        return 1

    #total number of ways cookie monster can eat cookies = 3. 
    #    
    
    print(eating_cookies(10))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
