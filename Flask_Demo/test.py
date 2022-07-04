import json
class MyObject():
    def __init__(self,name, value):
       self.name = name
       self.value = value


dict_names = {}
object = MyObject('foo', 2) #foo is the name, 2 is the value
object1 = MyObject('too', 3)
object2 = MyObject('doo', 4)
dict_names[object.name] = object
dict_names[object1.name] = object1
dict_names[object2.name] = object2



for key in dict_names:
    dic_main = {}
    empl_dic = {}
    data = dict_names[key]
    print("name:" + data.name + " value: " + str(data.value))


data = {
        "email": "taboo@gmail.com",
        "name": "taboo"
}

print(data.get("email"))

mytuple = (1, 2)
print(type(mytuple))
print(type(False))



