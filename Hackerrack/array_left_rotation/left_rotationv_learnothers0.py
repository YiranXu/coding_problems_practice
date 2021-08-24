import math
import os
import random
import re
import sys

def rotLeft(a, d):
    # this approach only works for short arrays
    i = d%len(a)
    return (a[i:]+a[:i])
    
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