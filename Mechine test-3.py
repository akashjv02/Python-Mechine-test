#find student with using id
student = [
    {"id": 1, "name": "rajesh"}, 
    {"id": 2, "name": "rahul"}, 
    {"id": 3, "name": "sruthi"}]

u_num = int(input("Enter User ID: "))

for x in student:
    if x["id"] == u_num:
        print("Student Name is: ", x["name"])
        break
else:
    print("Student not found")
    
    