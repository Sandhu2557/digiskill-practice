# Looping over data structure- Dictionary

student={
    "name":"usman",
    "age": 98,
    "grade":"A"
}
# use loop for getting dictionary's keys
for key in student:
    print(key)

# using loop for getting dictionary's values
for key in student:
    print(student[key])

#using loop for getting both values and keys
for key in student:
    print(key,":",student[key])


student_list=[
    {"name":"Ali",
    "age":20,
    "grade":"A"
    },
    {"name":"sara",
    "age":22,
    "grade":"A+"
    },
]
for student in student_list:
    print(f"Name:{student.get("name","")}|Grade:{student.get("grade","")}")