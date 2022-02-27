#Contiguous Subarrays from facebook preparation questions
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr):
    """
    this solution is O(n^2) of time complexity
    """
    output=[1]*len(arr)
    for i, n in enumerate(arr):
        for r in range(i+1,len(arr)): #to the right
            if arr[r]>n:
                output[i]+=r-i-1
                break
            if r==len(arr)-1:
                output[i]+=r-i
                
        for l in range(i-1,-1,-1):
            if arr[l]>n:
                output[i]+=i-l-1
                break
            if l==0:
                output[i]+=i
            
    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def count_subarrays_2(arr):
    output=[0]*len(arr)
    stack=[]
    #to the left
    #for i in range(len(arr)):
        #if 
def count_subarrays3(arr):
    n = len(arr)
    res = [1] * n
    stack = [-1]
    #left
    for i in range(n):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += i - stack[-1] - 1
        stack.append(i)
  
    # from right
    stack = [n]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] += stack[-1] - i - 1
        stack.append(i)
    return res

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays3(test_1)
  print(output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  print(output_2)

  # Add your own test cases here
  
