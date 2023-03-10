import numpy as np
import matplotlib.pyplot as plt

maxlim = 30
maxrange = 50
x = np.linspace(-1, maxlim, maxrange) #points on x-axis
simlen = int(1e6) #number of samples
cdf = [] #declaring probability list
uni_randvar = np.loadtxt('../data/uni.dat',dtype='double')
tran_randvar = -2*np.log(1-uni_randvar)
a=(1/2)*np.exp(-x/2)
print(a)
for i in range(0,maxrange):
	cdf_ind = np.nonzero(tran_randvar < x[i]) #checking probability condition
	cdf_n = np.size(cdf_ind) #computing the probability
	cdf.append(cdf_n/simlen) #storing the probability values in a list
y=np.piecewise(x,[x<0,x>=0],[0,lambda a:a])
plt.scatter(y,cdf)
plt.plot(x, cdf, 'orange') #plotting CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('../../figs/ch2/log_uni_cdf.pdf')
plt.savefig('../../figs/ch2/log_uni_cdf.png')

plt.show()
