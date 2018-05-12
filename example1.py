# Example 1, chapter 2. 
# Estimating the bias of a coin

import numpy as np
import matplotlib.pyplot as plt

#############################
# Generating coinflip data: #
#############################
N = 100   # Number of flips
bias = 0.25 # bias weighting for heads
R = 0       # Number of heads
for i in range(N):
    tall = np.random.random()
    if tall <= bias:
        R += 1
# R and N is the data



#####################################
# Using data to estimate coin bias: #
#####################################

n = 1001 # Number of hypothesises / possible bias values
dH = 1./(n-1)
H = np.linspace(dH,1-dH,n-1)

prior_pdf = np.ones(n-1)

# Without log:  (log must be used for N>1000)
probOfDataGivenH = H**R * (1-H)**(N-R)
posterior_pdf = probOfDataGivenH*prior_pdf
posterior_pdf /= max(posterior_pdf)

# Using log:
#log_probOfDataGivenH = R*np.log(H) + (N-R)*np.log(1-H)
#log_posterior_pdf = log_probOfDataGivenH + np.log(prior_pdf)
#log_posterior_pdf -= max(log_posterior_pdf)
#posterior_pdf = np.exp(log_posterior_pdf)
#posterior_pdf /= np.sum(posterior_pdf*dH)

plt.plot(H, posterior_pdf)
plt.show()
