print(" Welcome to Employee Management System.")
num_of_employee = 0
list_of_emp = []

    
def add():
    global num_of_employee, list_of_emp
    name = input("Enter an Employee Name: ")
    position = input("Enter an Employee Position: ")
    salary = input("Enter an Employee salary: ")
    num_of_employee += 1
    employee = {"name":name, "position":position, "salary":salary}
    list_of_emp.append(employee)
    print("Employee added.")   


def detail_info():
    print("Employee Details.")
    for employee in list_of_emp:
        print(f"Name: {employee['name']}")
        print(f"Position: {employee['position']}")
        print(f"Salary: {employee['salary']}")


def delete():
    global num_of_employee
    ask = input("Do you want to delete recently added? (y/n): ").lower()

    while True:
        if ask == "y":
            num_of_employee -= 1
            print(f"Deleted sucsessfuly...")
            break

        elif ask == "n":
            return
        else:
            print("Envalid input. Please press y/n.")
            break

while True:
    print(f"Number of Employee: {num_of_employee}")
    first_in = input("To add type 'A', To delete type 'D', To show info. type 'I', 'Q' to Quit: ").upper()

    if first_in == "A":
        add()
    
    elif first_in == "I":
        detail_info()

    elif first_in == "D":
        delete()
        
    elif first_in == "Q":
        print("Exiting...")
        break
    else:
        print("Invalid input. Press 'A' or 'Q'.")