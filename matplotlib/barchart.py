import matplotlib.pyplot as plt
import numpy as np

labels = ['a','b','c']
values = [1,3,2]

bars = plt.bar(labels,values)
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')
patterns = ['/','o','*']
for bar in bars:
    bar.set_hatch(patterns.pop())
plt.show()