import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kixz7.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
db.student.find()
students = db.students
student_list = students.find({})

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() Query --")

for doc in student_list:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
update = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Herschmann"}})
leah = student.find_one({student_id: 1007})
print("\n -- DISPLAYING STUDENT DOCUMENT 1007")
print("\n Student ID: " + leah["student_id"] + "\n First Name: " + leah["first_name"] + "\n Last Name: " + leah["last_name"] + "\n")
input("\n End of program, press any key to continue...")