from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["college"]
collection = db["students"]

def insert_student():
    name=input("enter a student name")
    age=int(input("enter a student age"))
    course=input("enter a course name")
    students = {"name": name, "age": age, "course": course}

    if collection.find_one({"name": name, "course": course}) is None:
        collection.insert_one(students)
        print("Student inserted successfully")
    else:
        print("Student already exists")


def display_student():
    for i in collection.find({}, {"_id": 0}):
        print(i)

while True:
    ch=int(input("enter a choice="))
    if ch==1:
        insert_student()
    elif ch==2:
        display_student()
    else:
        exit()               


