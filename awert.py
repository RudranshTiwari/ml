
import math
import os
import random
import re
import sys

def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  
      
# Driver code 
list1 = int(input())
print(multiplyList(list1)) 
