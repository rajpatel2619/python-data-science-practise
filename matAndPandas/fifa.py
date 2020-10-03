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

# left = fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
# # print(left)
# right = fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]

# labels = ['Left','Right']
# colors = ['blue','red']
# plt.pie([left,right],labels=labels,colors=colors,autopct='%.2f %%')
# plt.title('Foot preference of FIFA Players')
#
# fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
# # print(fifa.Weight)
# plt.style.use('ggplot')
#
# light = fifa.loc[fifa.Weight < 125].count()[0]
# light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
# medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
# medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
# heavy = fifa.loc[fifa.Weight >= 200].count()[0]
#
# weights = [light,light_medium,medium,medium_heavy,heavy]
#
# labels = ['Under 125','125-150','150-175','175-200','Over 200']
# explode = (.4,.2,0,0,.4)
# plt.title('Weight Distribution of FIFA Players ( in lbs ) ')
# plt.pie(weights,labels=labels,autopct='%.2f%%',pctdistance=0.8,explode=explode)
# plt.savefig('fifaWight.png',dpi=300)



plt.style.use('default')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']
labels = ['FC Barcelona','Real Madrid','New England Revolution']
plt.figure(figsize=(5,8))
plt.title('Professional Soccer Team Comparison')
plt.ylabel('Fifa Overall Rating')

boxes = plt.boxplot([barcelona,madrid,revs],labels=labels,patch_artist=True,medianprops={'linewidth':2})
# colors=[]
for box in boxes['boxes']:
    box.set(color='blue',linewidth=2)

    box.set(facecolor='#e0e0e0')

plt.savefig('box.png',dpi=300)
plt.show()