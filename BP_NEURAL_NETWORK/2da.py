import pandas as pd


conde_list = []
#
# t = pd.DataFrame()
#
#
# for i in range(28):
#     exec('var{} = pd.DataFrame()'.format(i))
#
# print(var25)

names = locals()
for i in range(5):
    names['n' + str(i)] = pd.DataFrame()
    conde_list.append(names['n' + str(i)])

#print(n0,n1,n2,n3,n4)
print(conde_list)
