#!/bin/python
# -*- coding: utf-8 -*-

from panda_script_functions import *

import getpass
from pandas import * # how does this differ from next line?
import pandas
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = pandas.__version__
print(x)

plot arange(10)

%pylab inline

def side_by_side(*objs, **kwds):
    from pandas.core.common import adjoin
    space - kwds.get('space', 4)
    reprs = [repr(obj).split('\n') for obj in objs]
    print adjoin(space, *reprs)

plt.rc('figure', figsize=(10, 6))

# adjoin ?



# Panda series and dataframe
# R dataframe is consistent concept here.
# Index = label array

# Descriptive stats 

# Doing group ops on data that easily can be grouped

#  Aggregations or transformations like subtracting mean value - using group by...

# Pivot tables

# Summary of data sets.

# Merge data sets.  JOIN-like.

# Time-series

# baby-names.csv = top 1000 names for both boys and girls over the years....

# record count = 2000 records per year * 

# json database from usda

#  json to csv => descriptive stats

# heapy and timeit

# 