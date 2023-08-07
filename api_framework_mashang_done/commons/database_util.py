import pymysql

#创建数据库链接
def create_connection():
    conn = pymysql.connect(
        user="root",
        password="admin123",
        host="localhost",
        database="phpwind",
        port=3306,
    )
    return conn

#执行sql语句
def execute_sql(sql):
    #创建游标
    conn = create_connection()
    cs = conn.cursor()
    #执行sql
    cs.execute(sql)
    #提取值
    value = cs.fetchall()
    #关闭链接
    cs.close()
    conn.close()
    return value

if __name__ == '__main__':
    print(execute_sql("select password from pw_user where username='pytest'"))
    #(('pytest', '0'),)