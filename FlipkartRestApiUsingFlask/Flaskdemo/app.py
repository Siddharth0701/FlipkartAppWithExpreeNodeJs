# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def index():
#   return "Hello World"
#print('hello world')
# string formating
name="bob"
geeting=f"Hello,{name}"
#print(geeting)
name="Singh"
#print(f"hello,{name}")
#name= int(input("enter the name number:"))
#print(name)
l=["Singh","Siddharth","Sohan"]
t=("Singh","Siddhu","Singham")
s={"Singh","Siddharth","Jagan mohan reddy"}

l.append("smith")
# print(l)

friends={"bob","smith","Anne"}
abroad={"bob","Anne"}

local_friend=friends.difference(abroad)
#print(local_friend)
# number=7
# user_input=input("Enter 'y' if you would like to play:")
# if user_input =="y" or "Y":
#     user_number=int(input("Guess the number!:"))
#     if user_number ==number:
#         print("you guess currectly!")
#     else:
#         print("sorry, it's wrong !")
# else:
#     print("please choose y")

student_attendence={"singh":90,"Siddharth":97,"Rauf":91}
# for student in student_attendence:
#     print(student)

# x,y=10,20
# c=x+y
# print(c)

# add=lambda x,y:x+y
# print(add(4,9))
# print((lambda x,y:x+y)(3,3))
class Student:
    def __init__(self) -> None:
        self.name="Siddharth"
        self.grades=(90,90,93,78,90)
    def average(self):
        return sum(self.grades) /len(self.grades)
student=Student()
# print(student.name)
# print(student.average())
# print(student.grades)

def times(var):
    return var *var

#print(times(5))

seq=[2,3,4,5,6]

#print(list(map(times,seq)))

l=lambda var: var *2

#print(l(10))
#print(list(map(lambda var:var *3,seq)))
import math
#print(list(map(lambda var: var +2,seq )))
#print(list(filter(lambda var:var %2==0,seq)))
plane="earth"
diam=3432
print("he diameter of Earth is 12742 kilometers.")
print("The",diam,"of is",plane,"kilometers." )










