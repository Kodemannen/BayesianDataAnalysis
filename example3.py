# Example 3: The lighthouse problem

####################
# Generating data: #
####################
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
alpha = 4
beta = 1
lighthouse_position = (alpha, beta)

T = 20
M = 1000
times = np.sort(np.random.random_sample(size=M))*T      # the times the lighthouse sent out signals
angular_velocity = 2*np.pi # rad/s

angles = angular_velocity*times
angles = angles - (angles // (2*np.pi)) * 2*np.pi    # making the angles between 0 and 2pi
angles = angles * (angles>np.pi)
angles = angles[np.nonzero(angles)]     # the angles that would reach the shore

X = beta*np.tan(angles) + alpha     # the data points that we will use X = [x1, x2, x3, .. , xN]



#################################
# Estimating alpha by the data: #
#################################
# We have data points in X, we also know the value of beta

N = len(X)   
print(np.mean(X))
alphas = np.linspace(0, 5, 100)

Ls = np.zeros(len(alphas))
for i in range(len(alphas)):
    Ls[i] = -np.sum( np.log( beta**2 + (X - alphas[i])**2) )

Ls -= np.max(Ls)

pdf = np.exp(Ls) / np.sum(np.exp(Ls))

plt.plot(alphas, pdf)
plt.show()