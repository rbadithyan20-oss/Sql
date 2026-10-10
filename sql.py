import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='**********',
    database='sqlaugust2026',
)
cursor=conn.cursor()

#sql="insert into employee values(1,'Arun',25000,'dev')"
#sql="insert into employee values(2,'Abhijith',30000,'dev')"
#sql="insert into employee values(3,'Adithyan',40000,'HR')"
#sql="insert into employee values(4,'Abhijith',40000,'HR')"
#sql="insert into employee values(5,'Arun',45000,'Finance')"
#sql="insert into employee values(6,'Abhijith',50000,'Finance')"
#sql="create table employee(id int primary key,name varchar(20),salary int,dept varchar(20))"
sql="select * from employee"
cursor.execute(sql)
#row=cursor.fetchall() egane koduthal enter cheytha full data print aakum
#for i in row:
    #print(i[0],i[1],i[2],i[3])
#row=cursor.fetchmany(1)# fetchmany koduthit 1 koduthal first row matram print aavum
#for i in row:
   # print(i[0],i[1],i[2],i[3])
#row=cursor.fetchmany(2)# fetchmany koduthit 2 koduthal first 2 rows matram print aavum
#for i in row:
    #print(i[0],i[1],i[2],i[3])
row=cursor.fetchone()# fetchone koduthit first row matram print aavum
print(row[0],row[1],row[2],row[3])# ivda nested loop alla varunath ath kond for loop illatha print aavum
conn.commit()
conn.close()