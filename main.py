from task import tasks_list
name = input("what`s your name ?")
print("hi ",name)



while True :
    task_y_n =input("do you want add task yes or no ?  ")
    if task_y_n == "yes" :
       
        task_ques = input("enter your task: ")
        tasks_list.append(task_ques)
        print("task : ",task_ques," saved")
    elif task_y_n == "no":
        break
    else:
        print("pleas try again ")
        continue
