import pickle
import os

student_database = []

def load_student_database() -> None:
    global student_database
    if os.path.exists('students_db.pkl'):
        with open('students_db.pkl', 'rb') as f:
            student_database = pickle.load(f)
            print('Student Database Loaded from file')

    elif os.path.exists('student_info_python.txt'):
        with open('student_info_python.txt', 'r') as f:
            student_list = f.read().splitlines()
            for student in student_list:
                student = student.split(',')
                if len(student) == 5:
                    #build a student record and add to database
                    student_data = {
                        'Name': student[0].strip(),
                        'Roll Number': student[1].strip(),
                        'Age': int(student[2]),
                        'Grade': float(student[3]),
                        'Contact Number': student[4].strip(),
                    }
                    student_database.append(student_data)
                else:
                    raise ValueError('student_info_python.txt: is incorrect')
    else:
        raise ValueError('students_info_python.txt not found')

def save_student_database() -> None:
    with open('students_db.pkl', 'wb') as f:
        pickle.dump(student_database, f)
    print('Student database saved to file')

def add_student() -> None:
    student_data ={
        'Name': input('Enter student name: '),
        'Roll Number': input('Enter roll number: '),
        'Age': int(input('Enter age: ')),
        'Grade': float(input('Enter grade: ')),
        'Contact Number': input('Enter contact number: '),
    }
    student_database.append(student_data)

def display_all_students() -> None:
    for student in student_database:
        print(student)

def search_student(name: str) -> None:
    for student in student_database:
        if student['Name'] == name:
            print(student)
            return
    print("Student not found")

def update_student(name: str, field: str, new_value: str | int | float) -> None:
    for student in student_database:
        if student['Name'] == name:
            student[field] = new_value
            print('Student information updated.')
            return
    print('Student not found.')

def delete_student(name: str) -> None:
    for student in student_database:
        if student['Name'] == name:
            student_database.remove(student)
            print('Student deleted')
            return
    print('Student not found.')

if __name__ == '__main__':
    print('Student database program')

    while True:
        #print a menu
        print('student Database Menu')
        print('1. Add student')
        print('2. Update student')
        print('3. Delete student')
        print('4. Search student')
        print('5. Display all student')
        print('6. Load database from file')
        print('7. Save database to file')
        print('q. Quit')
        #Get the users choice
        option = input('Enter an option from above: ')

        match option:
            case '1':   #add a student
                add_student()
            case '2':  #update student
                print()
                name = input('Enter student name: ')
                field = input('Enter the name of the field (Name, Roll Number, Age, Grade, Contact Number) to update: ')
                field_query = f'Enter a new value for {field}: ' #String interpolation is done with f''
                valid_field = True
                if field in ['Name', 'Roll Number', 'Contact Number']:
                    value = input(field_query)
                elif field == 'Age':
                    value = int(input(field_query))
                elif field == 'Grade':
                    value = float(input(field_query))
                else:
                    print('Invalid field')
                    valid_field = False
                if valid_field:
                    update_student(name, field, value)


            case '3':   # delete student
                name = input('Enter student name: ')
                delete_student(name)
            case '4': #display student
                name = input('Enter student name: ')
                search_student(name)
            case '5': #display all students()
                display_all_students()
            case '6': #load database
                load_student_database()
            case '7': #save student database()
                save_student_database()
            case 'q': #quit
                break   #Gets us out of the while loop
            case _: #something wicked this way comes
                print('Invalid option, please try again.')

        print()

    print('Done')