import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

# print(fifa.head(5))
# print(fifa)

# histogram....

# bins = [40,50,60,70,80,90,100]
# plt.hist(fifa.Overall,bins=bins,color='#03f0fc')

# plt.xticks(bins)
#
# plt.ylabel('No of Players')
# plt.xlabel('Skill labels')
# plt.title('Distribution of Players Skills in FIFA 2018')

left = fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
# print(left)
right = fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]

plt.pie([left,right])

plt.show()