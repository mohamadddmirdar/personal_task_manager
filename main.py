import os
from dotenv import load_dotenv
from task import tasks_list
name = input("what`s your name ?")
print("hi ",name)

load_dotenv()

admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")

open_admin = input("Do you want to open admin mode? yes/no: ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")


while True :
    task_y_n =input("do you want add task yes or no ?  ")
    if task_y_n == "yes" :
       
        task_ques = input("enter your task: ")
        task_priroity = input("enter your task priroity: ")
        tasks_list.append(task_ques)
        tasks_list.append(task_priroity)
        print("task : ",task_ques," priroity : ",task_priroity,"  saved ")
    elif task_y_n == "no":
        break
    else:
        print("pleas try again ")
        continue
with open ("result.txt" , "a") as file:
    file.write(f"{name} - Tasks{tasks_list}\n")