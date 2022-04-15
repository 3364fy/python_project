import pymysql
database=pymysql.connect(host="localhost",user="root",password="33649464",database="bjpowernode",charset='utf8')
#初始化指针
cursor=database.cursor()
#增
sql="insert into ll (id,name,class) values ('120','而忽视色覅框架SV打开vdkzvdmd','56')"
cursor.execute(sql)
database.commit()
database.close()
#改
# sql="update ll set name ='sdgdfbvdavsv' where name ='而忽视色覅框架SV打开vdkzvdmd'"
# cursor.execute(sql)
# database.commit()
# database.close()
#查
sql="select name,class from ll where id='105'"
cursor.execute(sql)
result=cursor.fetchall()
print(result)
sql="select * from ll where id='105' group by id;"
cursor.execute(sql)
results=cursor.fetchall()
print(results)
#删
sql="delete from ll where id='4';"
cursor.execute(sql)
database.commit()
database.close()