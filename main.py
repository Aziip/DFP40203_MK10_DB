import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_mk10'
)


def print_students():
    mycursor = mydb.cursor()

    mycursor.execute('SELECT namapelajar FROM pelajar')
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[0])


def add_student():
    mycursor = mydb.cursor()

    student_name = input("Enter the name of the student: ")

    sql = "INSERT INTO pelajar (namapelajar) VALUES (%s)"
    val = (student_name,)
    mycursor.execute(sql, val)

    mydb.commit()


if __name__ == '__main__':
    print("Current list of students:")
    print_students()

    add_student()

    print("\nUpdated list of students:")
    print_students()
