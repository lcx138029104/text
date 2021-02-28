import pandas as pd
import xlrd

if __name__ == '__main__':

    data = pd.read_excel('./north_1.xlsx')

    n = data.shape[0]
    n_1 = n-242
    print(n,n_1)

    data = data.iloc[n_1:n,:]

    north_mean = data.iloc[:,7].mean()
    north_std = data.iloc[:,7].std()

    if data['北向资金（百万元）'].iloc[-1] > north_mean + 1.5* north_std:
        print('买入')
    if data['北向资金（百万元）'].iloc[-1] < north_mean - 1.5* north_std:
        print("卖出")
    else:
        print("持有")