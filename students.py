students = { 
    
}
def main():
    for i in range(3):
        student_id = input(f"Enter student number {i + 1}: ".format(i))
        student_name = input(f"Enter first name {i + 1}: ".format(i))
        students[student_id] = student_name
    for id, name in students.items():
        print(id, name)
    del students[student_id]
    student_id = input(f"Enter your student number: ")
    student_name = input(f"Enter your first name: ")
    students[student_id] = student_name
    for id, name in students.items():
        print(id, name)

if __name__ == "__main__":
    main()