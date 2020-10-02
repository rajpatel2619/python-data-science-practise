# print('its time to matplotlib')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# plt.plot([1,2,9], [2,4,6])
x = [1,2,3,5,8,]
y = [2,4,6,7,9]
# plt.plot(x, y,label="2x",color='red',linewidth=2,linestyle='--',marker='.',markersize=15,markeredgecolor='blue')
plt.plot(x, y,'b.--',label="2x")

x2 = np.arange(0,4.5,0.5)
# print(x2)
plt.plot(x2,x2**2,'r',label='x2')
plt.title('our first graph',fontdict={'fontname': 'Comic Sans Ms','fontsize':30,'color':'green'})
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([1,2,3,4,5])
plt.legend()
# plt.figure(figsize=(2,3),dpi=200)
plt.savefig('mygraph.png',dpi=300)
plt.show()
