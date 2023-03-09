# class Person:
#   def __init__(self,name,age) -> None:
#     self.name=name
#     self.age=age
#   def __str__(self) -> str:
#     return f"Person {self.name},{self.age} year old"
#   def __repr__(self) -> str:
#     return f"<Person {self.name},{self.age}>"


# bob=Person("Siddharth Singh",22)
# print(bob)

# class ClassTest:
#   def instance_method(self):
#     print("Hello instance  method",self)

#   @classmethod
#   def class_method(cls):
#     print("Hello ClASS METHOD ",cls)

#   @staticmethod
#   def static_method():
#     print("Static method")

# ClassTest.static_method()
# ClassTest.class_method()
# Obj= ClassTest()
# Obj.instance_method()

# # obj.instance_method()
# def list_avg(sequence:list)->float:
#   return sum(sequence)/len(sequence)

# print(list_avg([123]))
# import functools
# user={"username":"singh","access_label":"guest"}
# def make_secure(func):
#   @functools.wraps(func)
#   def secure_method():
#     if user["access_label"]=="admin":
#       return func()
#     else:
#       return f"No admin permissions for {user['username']}."
#   return secure_method

# @make_secure
# def get_admin_password():
#   return "123"
# print(get_admin_password.__name__)

def divide(divident,divisor):
  if divisor ==0:
    raise ZeroDivisionError("Divisor cannot be 0")
  return divident/divisor

def calculator(*value,operation):
  return operation(*value)

result=calculator(20,4,operation=divide)
print(result)


