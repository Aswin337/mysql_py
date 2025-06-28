import pymysql
from pymysql.cursors import DictCursor
from password_utils import get_decrypt_password
connection=pymysql.connect(
    host="localhost",
    user="root",
    password=get_decrypt_password(),
    database="test",
    cursorclass=DictCursor
)
print(get_decrypt_password())
try:
    with connection.cursor() as cursor:
        create_query="""Create table if not exists students (
        id int auto_increment primary key,
        name varchar(100),
        age int,
        department varchar(100)
        );"""
        cursor.execute(create_query)


        insert_query="""insert into students(name,age,department) values(%s,%s,%s);"""
        values=[("Anachi",19,"CSE"),("Praveen",20,"MECH"),("Hari",21,"ECE")]
        cursor.executemany(insert_query,values)
        connection.commit()

        
        select_query="""select * from students;"""
        cursor.execute(select_query)
        res=cursor.fetchall()
        with open("mysql1.txt","w") as file:
            for row in res:
                file.write(f"{row} \n")
                print(row)
finally:
    connection.close()