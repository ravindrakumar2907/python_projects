""" user database operations"""


from db.mysql_connection import MySQLConnector


class UserDbOperations:
    # Select from database
    @staticmethod
    def get_user(id):
        myconn = MySQLConnector()
        myconn.cursor.execute("SELECT * FROM user where id=" + id)
        row = myconn.cursor.fetchone()
        print(row)

    @staticmethod
    def get_all_student():
        mycon = MySQLConnector()
        mycon.cursor.execute("SELECT * FROM fb.user")
        user_result = mycon.cursor.fetchall()
        for x in user_result:
            print(x)

    #update user set name='ravi' where id = 1;
    #update user set name ='ravindra' where id=1
    @staticmethod
    def update_student(name, id):
        mycon = MySQLConnector()
        query = "update user set name='" + name + "' where id=" + str(id)
        print(query)
        mycon.cursor.execute(query)
        user_result = mycon.cursor.rowcount
        mycon.conn.commit()
        print(user_result)

    @staticmethod
    def delete_student(id):
        mycon = MySQLConnector()
        mycon.cursor.execute("delete FROM fb.user where id=" + str(id))
        user_result = mycon.cursor.rowcount
        mycon.conn.commit()
        print(user_result)

    @staticmethod
    def insert_student(name, email):
        mycon = MySQLConnector()
        query = "insert into user (name, email) values ('" + name + "', '" + email + "')"
        print(query)
        mycon.cursor.execute(query)
        user_result = mycon.cursor.rowcount
        mycon.conn.commit()
        print(user_result)


#UserDbOperations.get_user(str(1))
UserDbOperations.get_all_student()
#UserDbOperations.update_student('ravi', 1)
#UserDbOperations.delete_student(2)

#UserDbOperations.insert_student('rahul', 'rahul@gmail.com')

