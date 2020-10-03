import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv('gas_prices.csv')

# print(gas)
plt.figure(figsize=(8,5))
plt.title('Gas Prices Over Time (in USD)',fontdict={'fontweight':'bold','fontsize':22})
# printing the specific
# plt.plot(gas['Year'],gas.USA,'b.-',label='United State',)
# plt.plot(gas.Year,gas.Canada,'r.-',label="Canada")
# plt.plot(gas.Year,gas['South Korea'],'g.-',label="South Korea")
# prinitng all
# for country in gas:
#     if country != 'Year':
#         plt.plot(gas.Year,gas[country],label=country)
# printing some specific
country_to_look_at = ['Australia','USA','Canada','South Korea']
for country in gas:
    if country in country_to_look_at:
        plt.plot(gas.Year,gas[country],label=country,marker='.')
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.xlabel('Year')
plt.ylabel('US Dollors')
plt.legend()
plt.savefig('gas_price_figure.png',dpi=300)
plt.show()