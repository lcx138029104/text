# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:25:31 2018
@author: Lenovo
"""

import pandas as pd

data = pd.read_excel('C:/Users/Admin/Desktop/财务账表201901-202001.xlsx')
rows = data.shape[0]  # 获取行数 shape[1]获取列数
department_list = []

# for i in range(rows):
#     temp = data["一级科目"][i]
#     if temp not in department_list:  # 防止重复
#         department_list.append(temp)  # 将销售部门的分类存在一个列表中

data2 = pd.DataFrame(data[input('输入科目名称：')])
data3 = data2.drop_duplicates(subset=None, keep='last', inplace=False)
department_list = list(data3['一级科目'])
n = len(department_list)  # 销售部门科目数


df_1 = pd.DataFrame()  # 用于存储一科的dataframe
df_2 = pd.DataFrame()  # 用于存储二科的dataframe
df_3 = pd.DataFrame()  # 用于存储三科的dataframe
df_4 = pd.DataFrame()
df_5 = pd.DataFrame()
df_6 = pd.DataFrame()
df_7 = pd.DataFrame()
df_8 = pd.DataFrame()
df_9 = pd.DataFrame()
df_10 = pd.DataFrame()
df_11 = pd.DataFrame()
df_12 = pd.DataFrame()
df_13 = pd.DataFrame()
df_14 = pd.DataFrame()
df_15 = pd.DataFrame()
df_16 = pd.DataFrame()
df_17 = pd.DataFrame()
df_18 = pd.DataFrame()
df_19 = pd.DataFrame()
df_20 = pd.DataFrame()
df_21 = pd.DataFrame()
df_22 = pd.DataFrame()
df_23 = pd.DataFrame()
df_24 = pd.DataFrame()
df_25 = pd.DataFrame()
df_26 = pd.DataFrame()
df_27 = pd.DataFrame()
df_28 = pd.DataFrame()


df_list = [df_1, df_2, df_3,df_4,df_5,df_6,df_7,df_8,df_9,df_10,df_11,df_12,df_13,df_14,df_15,df_16,df_17,df_18,df_19,
           df_20,df_21,df_22,df_23,df_24,df_25,df_26,df_27,df_28]

for department in range(n):
    for i in range(0, rows):
        if data["一级科目"][i] == department_list[department]:
            df_list[department] = pd.concat([df_list[department], data.iloc[[i], :]], axis=0, ignore_index=True)





writer = pd.ExcelWriter('C:/Users/Admin/Desktop/sss.xlsx')  # 利用pd.ExcelWriter()存多张sheets

for i in range(n):
    df_list[i].to_excel(writer, sheet_name=str(department_list[i]), index=False)  # 注意加上index=FALSE 去掉index列
    print('正在导入',i)


writer.save()