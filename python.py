students_records = []

while True:
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. student offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    choice == 1
    print("\nEnter student details:")

    student = {
            "id": input("Student ID: "),
            "name": input("student Name: "),
            "age": int(input("student Age: ")),
            "grade": input("student Grade: "),
            "birthdate": input("student Birthdate: "),
            "subjects": input("student Subjects: ").split(",")
        }

    students_records.append(student)
    print("Student added successfully!")

    print()
    choice == 2
    chioce = input("Enter your choice: ")
    print("\n--- Display All Students ---")
    for student in students_records:
        print("id:", student["id"])
        print("name:", student["name"])
        print("age:", student["age"])
        print("grade:", student["grade"])
        print("birthdate:", student["birthdate"])
        print("subjects:", student["subjects"])
        
    print()
    choice == 3
    chioce = input("Enter your choice: ")
    print("\n----student data update-----")
    sid = input("Enter Student id update: ")

    for s in student:
            if int(student["id"]) == sid:
                s["name"] = input("New student Name: ")
                s["age"] = int(input("New student Age: "))
                print("Student updated successfully!")
                break
     
    print()
    choice == 4
    chioce = input("Enter your choice: ")
    print("\n-- STUDENT DATA DELETE--")
    for student in students_records:
            if int(student["id"]) == id:
                students_records.remove(student)
                break
    print()
    choice == 5
    chioce = input("Enter your choice: ")
    print("\n----- Subjects Offered -----")

    all_subjects = set()

    for student in students_records:
        all_subjects.update(student["subjects"])

    print()
    choice == 6
    chioce = input("Enter your choice: ")
    print("\n   EXIT   ")
    break


    
