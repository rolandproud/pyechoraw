'''

Estimate background noise level (BNL) using Power received

Modification History:

'''

## import packages
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import gzip
import pickle

## import user modules
from pyechoraw.manipulate import estimate_BNL

## read raw power
def getPower(filepath):
    f   = gzip.open(filepath,'rb')
    obj = pickle.load(f,encoding = 'bytes')
    f.close()
    return obj
    
## parse PERG obj and output Sv (see readers.py)
power = getPower('./data/power.pklz')

## estimate BNL for each ping, median and 95th percentile
BNL,BNL_95 = estimate_BNL(power)

## plot
plt.figure()
plt.plot(BNL)
plt.plot(BNL_95)
plt.title('BNL estimation')
plt.xlabel('Ping')
plt.show()

