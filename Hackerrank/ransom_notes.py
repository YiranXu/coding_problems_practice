#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    magazine=dict(Counter(magazine))
    print("magazine",magazine)
    for word in note:
        if word not in magazine or magazine[word]==0:
            return print('No')
        else:
            magazine[word]-=1
    return print('Yes')
if __name__ == '__main__':
    with open('testcase.txt','r') as testcase:
        first_multiple_input=testcase.readline().rstrip().split()
        m = int(first_multiple_input[0])
        n = int(first_multiple_input[1])
        magazine=testcase.readline().rstrip().split()
        note=testcase.readline().rstrip().split()
    #first_multiple_input = input().rstrip().split()

    #m = int(first_multiple_input[0])

    #n = int(first_multiple_input[1])

    #magazine = input().rstrip().split()

    #note = input().rstrip().split()


    checkMagazine(magazine, note)
