import pymysql

# 1.获取连接对象
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    db="tushare",
    charset="utf8")

# 创建一个游标对象
cur = db.cursor()

sql_1 = "drop table if exists code_list2"  # 先执行删除语句：如果存在表，则删除。这是为了后续调试的方便

sql_2 = """create table `code_list2`(`index` varchar(100) not null,
`ts_code` varchar(100) default null,
`symbol` varchar(100) default null,
`name` varchar(100) default null,
`area` varchar(100) default null,
`industry` varchar(100) default null,
`fullname` varchar(100) default null,
`enname` varchar(100) default null,
`market` varchar(100) default null,
`exchange` varchar(100) default null,
`curr_type` varchar(100) default null,
`list_status` varchar(100) default null,
`list_date` varchar(100) default null,
`delist_date` varchar(100) default null,
`is_hs` varchar(100) default null,
PRIMARY KEY (`index`)
)"""

sql_3 = "show tables;"

cur.execute(sql_1)
cur.execute(sql_2)
cur.execute(sql_3)

db.close()