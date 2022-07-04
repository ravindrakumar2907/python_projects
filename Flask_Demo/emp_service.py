"""
This service is used for flak app
"""
import json
import uuid
from json import JSONEncoder
from random import Random


class Employee():
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class EmployeeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__



list_my = []
emp_dic = {}

emp1 = Employee(1, "ravi", "ravi@gmail.com")
emp2 = Employee(2, "pratik", "pratik@gmail.com")
emp3 = Employee(3, "mahesh", "mahesh@gmail.com")

emp_dic[emp1.name] = emp1.__dict__
emp_dic[emp2.name] = emp2.__dict__
emp_dic[emp3.name] = emp3.__dict__

list_my.append(emp1.__dict__)
list_my.append(emp2.__dict__)
list_my.append(emp3.__dict__)

print(EmployeeEncoder().encode(emp1))



# key- email value-empObject
#https://pynative.com/make-python-class-json-serializable/


def get_all_employee_data():
    return list_my

def get_all_employee_data_list():
    return list_my

def register_employee_data(json_data):
    flag = False
    if json_data:
        emp_temp = convert_json_to_emp(json_data)
        list_my.append(emp_temp.__dict__)
        flag = True
    return flag



def update_employee_data(json_data, email):
    flag = False
    if json_data and email:
        for emp in list_my:
            print(emp)
            if emp.get("email") == email:
                print("email: " + str(emp.get("name")))

                old_id = emp.get("id")
                temp = Employee(old_id, json_data.get("name"), json_data.get("email"))
                print("index: " + str(list_my.index(emp)))
                list_my.remove(emp)
                list_my.append(temp.__dict__)
                flag = True
                break
                #list_my.insert(list_my.index(emp), temp)
    return flag




def delete_employee_data(email):
    flag = False
    for emp in list_my:
        print(emp)
        if emp.get("email") == email:
            print("email: " + str(emp.get("name")))
            index = list_my.index(emp)
            emp_delete = list_my.__getitem__(index)
            #del list_my[index]
            list_my.remove(emp_delete)
            flag = True
            break
    return flag

def get_employee_data(email):
    for emp in list_my:
        print(emp)
        if emp.get("email") == email:
            print("email: " + str(emp.get("name")))
            index = list_my.index(emp)
            emp_delete = list_my.__getitem__(index)
            return emp_delete
    return None




def convert_json_to_emp(json_data):
    emp_id = uuid.uuid4()
    return Employee(emp_id, json_data.get("name"), json_data.get("email"))
