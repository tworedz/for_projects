#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
if __name__ == '__main__': 
    [print(i[0],i[1]) for i in OrderedCounter(sorted(input())).most_common(3) ]
