from db import MyMongoConnection

class StudentDataService:
    
    def insert_student(self, name, age, email):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        stud_data = {"name":name, "age": age, "email": email}
        stu_collection.insert_one(stud_data)
        
    def get_student_by_email(self, email):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        data = stu_collection.find({"email": email})
        return data
    
    def update_student_by_email(self, email, name):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        data = stu_collection.update_one({"email": email}, {'$set':{"name":name}})
        
    
    def get_all_students(self):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        data = stu_collection.find({})
        return data
    
    def remove_student_by_email(self, email):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        data = stu_collection.delete_one({"email": email})
        
    def get_all_students_counts(self):
        stu_collection = MyMongoConnection.MongoDBConnection.get_mycollection("test", "student")
        data = stu_collection.find({}).count()
        return data
        
    
    
    



"""
Error:1 
/Users/ravindramore/python/workspace/PythonMongoConnection/StudentDataAccess.py:17: DeprecationWarning: update is deprecated. Use replace_one, update_one or update_many instead.
  data = stu_collection.update({"email": email}, {'$set':{"name":name}})
  
Error:2
/Users/ravindramore/python/workspace/PythonMongoConnection/StudentDataAccess.py:27: DeprecationWarning: remove is deprecated. Use delete_one or delete_many instead.
  data = stu_collection.remove({"email": email})
"""

