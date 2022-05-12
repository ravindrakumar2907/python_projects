from db_service import StudentDataAccess

s = StudentDataAccess.StudentDataService()   
#s.insert_student("Ravi", 31, "ravi@gmail.com")
#s.insert_student("Rahul", 30, "rahul@gmail.com")
#s.update_student_by_email("rahul@gmail.com", "Rama")
my_cursor = s.get_student_by_email("rahul@gmail.com")

my_cursor = s.get_all_students()

for item in my_cursor:
    print(item)
    print(item['name'])

my_cursor = s.remove_student_by_email("rahul@gmail.com")

my_cursor = s.get_all_students()

for item in my_cursor:
    print(item)
    print(item['name'])
    
    
print("counts: " + str(s.get_all_students_counts()))