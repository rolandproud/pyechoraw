# -*- coding: utf-8 -*-
"""
.. :module:: manipulate
    :synopsis: manipulate raw data

| Developed by: Roland Proud (RP) <rp43@st-andrews.ac.uk> 
|               Pelagic Ecology Research Group, University of St Andrews
| Contributors:
|
| Maintained by:
| Modification History:      
|
"""

import numpy as np

def estimate_BNL(power,minPower = -999,maxBNL = -100):
    '''
    locate noise region in each ping (size: > 10 samples) - can be at any depth
    calculates median and 95th percentile value of noise region 
    for each ping
    '''  
    linear            = 10**(power/10.)
    linear            = np.ma.masked_invalid(linear)
    samps,pings       = power.shape
    BNL               = []
    BNL_95            = []
    for p in range(pings):
        data = linear[:,p].data[linear[:,p].mask == False]
        plen = len(data)
        #bnl  = minPower
        bnls    = [10**(minPower/10.)]
        bnls_95 = [10**(minPower/10.)]
        while plen > 10:
            splitdata = [data[0:int(plen/2)],data[int(plen/2):]]
            split     = [np.percentile(splitdata[0],95),np.percentile(splitdata[1],95)]
            idx       = np.argmin(split)
            data      = splitdata[idx]
            plen      = len(data)
            #bnl       = split[idx]
            bnls_95.append(np.percentile(data,95))
            bnls.append(np.median(data))
        bnls.reverse()
        bnls_95.reverse()
        for k,b in enumerate(bnls_95[1:]):
            if np.abs(10*np.log10(b) - 10*np.log10(bnls_95[k])) > 3:
                break
        BNL.append(10*np.log10(bnls[k]))
        BNL_95.append(10*np.log10(bnls_95[k]))
    
    #cap BNL to maxBNL        
    BNL                        = np.array(BNL)
    BNL[BNL > maxBNL]          = minPower
    if sum(BNL != minPower) > 0:
        BNL[BNL == minPower]   = 10*np.log10(np.ma.median(10**(BNL[BNL != minPower]/10)))
    else:
        BNL[BNL == minPower]   = maxBNL
    ## BNL95
    BNL_95                     = np.array(BNL_95)
    BNL_95[BNL_95 > maxBNL]    = minPower
    if sum(BNL_95 != minPower) > 0:
        BNL_95[BNL_95 == minPower] = 10*np.log10(np.ma.median(10**(BNL_95[BNL_95 != minPower]/10)))
    else:
        BNL_95[BNL_95 == minPower]  = maxBNL 
        
    return BNL,BNL_95



    
    