import math
import os
import random
import re
import sys

def rotLeft(a, d):
    # this approach only works for short arrays
    print(a)
    print(d)
    n=len(a)
    
    #result={}
    result_list=[None]*n
    for i,value in enumerate(a):
        if i-d>=0:
            result_list[i-d]=value
        else:
            result_list[n+i-d]=value
            print("result",result_list)
    #for key,value in result.items():
        #result_list[key]=value
    
    return result_list
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()