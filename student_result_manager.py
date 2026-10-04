student= {}

while True:
    print("\n-----STUDENT MANAGER SYSTERM-----")
    print("1. add student")
    print("2. viwe all student")
    print("3. cheake result")
    print("4. Exit")

    choice =int(input("Enter your choice:"))
    
    if choice == 1:
         name = input("Enter student name :")
         marks = int(input("Enter marks:"))
         student[name]=marks
         print(f"{name} successfully added")

    elif choice == 2:
         if not student:
              print("no student found!")
         else:
            for name,marks in student.items():
                print(name,":",marks)

    elif choice == 3:
        name = input("Enter student name:")

        if name in student:
            marks = student[name]

            if marks >=40:
                print("pass")
            else:
                print("fail")
        else:
            print("student not found")

    elif choice == 4:
        print("exiting...")
        break
    else:
        print("INVALID INPUT")


