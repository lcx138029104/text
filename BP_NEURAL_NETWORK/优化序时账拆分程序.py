import pandas as pd

"""
目前存在两个问题
1.待拆分的序时账科目名称是没有拆分的，还需要先拆分才能使用，拆分的函数没有写进来
2.拆分之后一级科目所在的列名是可能变动的，可能是0或者1，需要选择

"""


def Split_account(path1):

    data = pd.read_excel(io=path1)  # 获取需要拆分的序时账path
    data_df = data['科目名称'].str.split(r'-', expand=True)  # 拆分科目名称列
    data_0 = pd.concat([data, data_df], axis=1)  # 将拆分过后的data_0合并到序时账里面
    return data_0

def Split_chronological_account(data_0, path2):

    rows = data_0.shape[0]  # 获取行数 shape[1]获取列数
    department_list = []   # 预处理每个科目数据列表
    df_list = []  # 预处理建表名称

    data2 = pd.DataFrame(data_0['一级科目'])  # 获取科目名称所在列
    data3 = data2.drop_duplicates(
        subset=None, keep='last', inplace=False)  # 去重
    department_list = list(data3['一级科目'])  # 去处重复的科目名称
    n = len(department_list)  # 获取科目名称数量，建表预处理过程

    # 根据每个一级科目创建一个DataFrame
    names = locals()
    for i in range(n):
        names['n' + str(i)] = pd.DataFrame()
        df_list.append(names['n' + str(i)])

    # 把每个一级科目对应的行数据写入预处理的科目DataFrame
    for department in range(n):
        for i in range(0, rows):
            if data_0["一级科目"][i] == department_list[department]:
                df_list[department] = pd.concat(
                    [df_list[department], data_0.iloc[[i], :]], axis=0, ignore_index=True)

    writer = pd.ExcelWriter(path=path2)  # 利用pd.ExcelWriter()存多张sheets

    # 写入数据
    for i in range(n):
        df_list[i].to_excel(
            writer,
            sheet_name=str(
                department_list[i]),
            index=False)  # 注意加上index=FALSE 去掉index列
        print('正在导入', i)

    writer.save()


if __name__ == '__main__':
    path1 = "C:/Users/Admin/Desktop/拆分.xlsx"
    path2 = 'C:/Users/Admin/Desktop/啊啊啊啊.xlsx'
    Split_account(path1)
    Split_chronological_account(Split_account(path1), path2)
