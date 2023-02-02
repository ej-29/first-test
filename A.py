import matplotlib

#print(matplotlib.__version__) #3.6.3

import matplotlib.pyplot as plt
import numpy as np

xp = np.array([0,5])
yp = np.array([0,300])
print("A")
#print(xp)
#print(yp)

#plt.plot(xp, yp) #line
plt.plot(xp, yp, 'o') #점
plt.show()