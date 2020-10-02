# Pandas introduction and practise....

import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# printing the all data
# print(df)


# printing some lines only
# print(df.head(5))
#
# df_excel = pd.read_excel('pokemon_data.xlsx')
# print(df)

# print(pd.read_csv('pokemon_data.txt',delimiter='\t'))

# print(df.columns)

data= pd.read_csv('pokemon_data.csv')

# print(data[['Name','Type 1']])
# print (data.head(2))
# print (data.iloc[2:4])

# print(data.iloc[2,1])

# for index,row in data.iterrows():
#     print(index,row)

# print(data.sort_values(['Type 1' , 'Speed'] , ascending=[1,0]))
pk = data
# pk.drop(columns=['Name'])
# pk['Total'] = pk.iloc[:, 4:10].sum(axis =1)
# print(pk)

# pk.to_csv('modified2.csv')

# print(pd.read_csv('modified2.csv'))
# df = pk.loc[pk['Name'].str.contains('Mega')]
# print(df)

import  re
