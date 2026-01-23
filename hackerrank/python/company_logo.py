#!/bin/python3

import math
import os
import random
import re
import sys

#a.sort(key=lambda x: x[1])
#a = sorted(data, key=lambda x: (x['age'], x['score']))
if __name__ == '__main__':
    s = input()
    char_list = []
    unique_char = set(s)
    for char in unique_char:
        char_list.append((char,s.count(char)))
    sorted_list = sorted(char_list,key=lambda x: (-x[1],x[0]))
    for item in sorted_list[:3]:
        print(item[0],item[1])
        
        
#Faster implementation
#from collections import Counter

#if __name__ == '__main__':
#    s = input().strip()

#    counts = Counter(s)

#    for char, freq in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]:
#        print(char, freq)
