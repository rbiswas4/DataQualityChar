#!/usr/bin/env python

import matplotlib.pyplot as plt
import analyzeSN as ans
deep = ans.snanaSims.SnanaSims.fromSNANAfileroot('LSST_Ia', location='ENIGMA_LSSTDEEP_FIXED')

# Use the folowing to find the variables of interest
# deep.snList[0].meta.keys()

# Find number of observations per SN
epochs = map(lambda x: x.meta['NOBS'], deep.snList)
plt.hist(epochs)
plt.show()

# Find the distribution of redshifts 
redshifts = map(lambda x: x.meta['SIM_REDSHIFT_CMB'], deep.snList)
plt.hist(redshifts)
plt.show()
