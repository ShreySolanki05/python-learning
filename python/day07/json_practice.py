import json
student = {"name" : "john" , "age" : 20 , "list of grades" : ["A","B","C"]}

with open("student.json","w") as f:
    json.dump(student,f)
with open("student.json","r") as f:
    data = json.load(f)
    print(data)