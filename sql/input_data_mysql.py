import tushare as ts
import pymysql
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost/tushare')

ts.set_token('8545ac7ddbd900bfc35e7627ef57c3856e256ed20427094cc6ff1c0d')

pro = ts.pro_api()

df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date,is_hs,enname')

df.to_sql('code_list',con=engine,if_exists='replace',index=True)

