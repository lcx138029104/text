import tushare as ts
import pandas as pd

ts.set_token('8545ac7ddbd900bfc35e7627ef57c3856e256ed20427094cc6ff1c0d')
pro = ts.pro_api()

start = 20180101
end = 20210227

def get_cal_date(start, end):
    cal_date = pro.trade_cal(exchange='', start_date=start, end_date=end)
    cal_date = cal_date[cal_date.is_open == 1]
    dates = cal_date.cal_date.values
    return dates

df = pro.moneyflow_hsgt(start_date=start, end_date=end)

def get_north(start, end):

    cal_date = pro.trade_cal(exchange='', start_date=start, end_date=end)
    cal_date = cal_date[cal_date.is_open == 1]
    dates = cal_date.cal_date.values

    df = pro.moneyflow_hsgt(start_date=start, end_date=end)

    for i in range(0, len(dates) - 300, 300):
        d0 = pro.moneyflow_hsgt(start_date=dates[i], end_date=dates[i + 300])
        df = pd.concat([d0, df])
        df1 = df.drop_duplicates()
        df1.index = pd.to_datetime(df1.trade_date)
        df2 = df1

    return df2

df3 = get_north(start, end)
df3.columns = [
    '交易日期',
    '港股通（上海）',
    '港股通（深圳）',
    '沪股通（百万元）',
    '深股通（百万元）',
    '北向资金（百万元）',
    '南向资金（百万元）']

df3.sort_values('交易日期',inplace=True,ascending=True)

df3.to_excel('./north_1.xlsx')




