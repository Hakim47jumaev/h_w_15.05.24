from datetime import datetime 
list_of_tasks=[]
cnt=0
def add_task():
    global cnt
    cnt+=1
    task={
        "id":cnt,
        "name":input("username: ->"),
        "task_name":input("task name: ->"),
        "due_date":input("due date: ->"),
        "is_completed":False,
        "time": datetime.now(),
    }
    list_of_tasks.append(task)

def get_tasks():
    for i in list_of_tasks:
        for k,v in i.items():
            print(f"{k} - > {v}")
        print("..............................")


def get_by_id(id):
     
    for i in list_of_tasks:
        if i["id"]==id:
            for k,v in i.items():
                print(f"{k} - > {v}")
            print("..............................")

def delete_task(id):
     
    for i in list_of_tasks:
        if i["id"]==id:
            list_of_tasks.pop(list_of_tasks.index(i))



def edit_task(id):
     
    for i in list_of_tasks:
        if i["id"]==id:
            i["name"]=input("username: ->")
            i["task_name"]=input("task name: ->")
            i["due_date"]=input("due date: ->")



def todays_tasks():
    for i in list_of_tasks:
        if i["due_date"]=="today":
            for k,v in i.items():
                print(f"{k} - > {v}")
            print("..............................")
                
def filter_by_user(name):
     
    for i in list_of_tasks:
        if i["name"]==name:
            for k,v in i.items():
                print(f"{k} - > {v}")
            print("..............................")

while True:
    print(""" 
    1.add task 
    2.get tasks
    3.get by id
    4.delete by id
    5.edit 
    6.today's tasks
    7.filter by user
    8. exit    
    """)
    choose=input()
    match choose:
        case "1" : 
            add_task()
        case "2" :
            get_tasks()
        case "3":
            get_by_id(id=int(input("enter id for get - > ")))
        case "4":
            delete_task(id=int(input("enter id for delete  - > ")))
        case "5":
            edit_task(id=int(input("enter id for edit  - > ")))
        case "6":
            todays_tasks()
        case "7":
            filter_by_user(name=input("enter user name for filter  - > "))
        case "8":
            break
        case _:
            print("not found")
