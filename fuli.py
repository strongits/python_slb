for i in range(1,366):
	print("(1+0.1)^",i,"=",round(1.01**i,2)) 

#print( "申龙斌", "的", "程序人生", sep='' )

import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(1, 365, 365)
Y = np.power(1.01,X)
plt.plot(X,Y)
plt.show()

import antigravity

import this