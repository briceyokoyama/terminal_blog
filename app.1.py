import pymongo

uri = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']


#List Comprehension - The commented code can be summarized with the code below:
#students = collection.find({})
#student_list = []

#for student in students:
#    student_list.append(student)

#for student in students:
#    print(student)

students = [student for student in collection.find({})]

print(students)

#examples of flexibility of list comprehension

students = [student for student in collection.find({}) if student['mark'] == 99.0]

print(students)