import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kixz7.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

students = db.students
student_list = students.find({})

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() Query --")

for doc in student_list:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

harrold = {
    "first_name": "Harrold",
    "last_name": "Gales",
    "student_id": "1010"
}

harrold_id = students.instert_one(harrold).inserted_id
print("-- INSERTED STATEMENTS --")
print("Inserted students record into students collection with document_id " + str(harrold_id))

student_harrold = students.find_one({"student_id": "1010"})

print("\n-- DISPLAYING STUDENT TEST DOC -- ")
print(" Student ID: " + student_harrold["student_id"] + "\n First Name: " + student_harrold["first_name"] + "\n Last Name: " + student_harrold["last_name"] + "\n")

deleted_student_harrold = students.delete_one({"student_id": "1010"})
new_student_list = students.find()
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in new_student_list:
    print (" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
input("\n End of program, press any key to continue...")