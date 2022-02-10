import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kixz7.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

students = db.students

leah = {
    "first_name": "Leah",
    "last_name": "Loeb",
    "student_id": "1007"
}
bilbo = {
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "student_id": "1008"
}
fred = {
    "first_name": "Fred",
    "last_name": "Largin",
    "student_id": "1009"
}

leah_student_id = students.insert_one(leah).inserted_id
bilbo_student_id = students.insert_one(bilbo).inserted_id
fred_student_id = students.insert_one(fred).inserted_id


print("--INSERT STATEMENTS--")
print(" Inserted student record Leah Loeb into students collection with document_id " + str(leah_student_id))
print(" Inserted student record Bilbo Baggins into students collection with document_id " + str(bilbo_student_id))
print(" Inserted student record Fred Largin into students collection with document_id " + str(fred_student_id))