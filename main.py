import os
import mysql.connector as a

condb = a.connect(
    host="localhost",
    user="root",
    password="12345",
    database="lifeos"
)


#Task manager
def task_add():

    title=input("Enter task title (Study Python / Complete Assignment / Gym): ")
    descrp=input("Enter task description (Python practice / College work / Workout): ")
    status=input("Enter task status (Pending / In Progress / Completed): ")
    priority=input("Enter task priority (Low / Medium / High): ")

    cursor = condb.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status, priority) VALUES (%s, %s, %s, %s)",
        (title, descrp, status, priority)
    )
    condb.commit()


def task_view():

    query = "SELECT * FROM tasks ORDER BY id ASC"
    cursor = condb.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()


def task_update():

    print("Enter the ID of the task you want to update:")
    task_id = int(input())

    title = input("Enter new task title (Study Python / Complete Assignment / Gym): ")
    descrp = input("Enter new task description (Python practice / College work / Workout): ")
    status = input("Enter new task status (Pending / In Progress / Completed): ")
    priority = input("Enter new task priority (Low / Medium / High): ")

    cursor = condb.cursor()

    query = """
    UPDATE tasks
    SET title=%s, description=%s, status=%s, priority=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (title, descrp, status, priority, task_id)
    )

    condb.commit()
    cursor.close()


def task_delete():

    task_id = int(input("Enter the ID of the task you want to delete: "))

    cursor = condb.cursor()

    query = "DELETE FROM tasks WHERE id=%s"

    cursor.execute(query, (task_id,))

    condb.commit()
    cursor.close()


def task_manager():

    while True:

        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_add()

        elif choice == '2':
            task_view()

        elif choice == '3':
            task_update()

        elif choice == '4':
            task_delete()

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


#Habit manager
def habit_add():

    name = input("Enter habit name (Exercise / Reading / Meditation / Coding): ")
    description = input("Enter habit description (30 min workout / Read 10 pages / 10 min meditation / Practice Python): ")
    frequency = input("Enter habit frequency (Daily / Weekly / Weekdays): ")
    status = input("Enter habit status (Active / Inactive / Completed): ")

    cursor = condb.cursor()

    query = """
    INSERT INTO habits (name, description, frequency, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (name, description, frequency, status)
    )

    condb.commit()
    cursor.close()


def habit_view():

    cursor = condb.cursor()

    query = "SELECT * FROM habits ORDER BY id ASC"

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()


def habit_update():

    habit_id = int(input("Enter the ID of the habit you want to update: "))

    name = input("Enter new habit name (Exercise / Reading / Meditation / Coding): ")
    description = input("Enter new habit description (30 min workout / Read 10 pages / 10 min meditation / Practice Python): ")
    frequency = input("Enter new habit frequency (Daily / Weekly / Weekdays): ")
    status = input("Enter new habit status (Active / Inactive / Completed): ")

    cursor = condb.cursor()

    query = """
    UPDATE habits
    SET name=%s, description=%s, frequency=%s, status=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (name, description, frequency, status, habit_id)
    )

    condb.commit()
    cursor.close()


def habit_delete():

    habit_id = int(input("Enter the ID of the habit you want to delete: "))

    cursor = condb.cursor()

    query = "DELETE FROM habits WHERE id=%s"

    cursor.execute(query, (habit_id,))

    condb.commit()
    cursor.close()


def habit_manager():

    while True:

        print("\nHabit Manager")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Update Habit")
        print("4. Delete Habit")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            habit_add()

        elif choice == '2':
            habit_view()

        elif choice == '3':
            habit_update()

        elif choice == '4':
            habit_delete()

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


#Study Manager
def study_add():

    subject = input("Enter subject (Python / Maths / Physics / Chemistry): ")
    topic = input("Enter topic (Loops / Calculus / Mechanics / Organic Chemistry): ")
    hours = input("Enter study hours (1 / 2 / 3 / 4): ")
    status = input("Enter status (Pending / In Progress / Completed): ")

    cursor = condb.cursor()

    query = """
    INSERT INTO study (subject, topic, hours, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (subject, topic, hours, status)
    )

    condb.commit()
    cursor.close()


def study_view():

    cursor = condb.cursor()

    query = "SELECT * FROM study ORDER BY id ASC"

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()


def study_update():

    study_id = int(input("Enter the ID of the study record you want to update: "))

    subject = input("Enter new subject (Python / Maths / Physics / Chemistry): ")
    topic = input("Enter new topic (Loops / Calculus / Mechanics / Organic Chemistry): ")
    hours = input("Enter new study hours (1 / 2 / 3 / 4): ")
    status = input("Enter new status (Pending / In Progress / Completed): ")

    cursor = condb.cursor()

    query = """
    UPDATE study
    SET subject=%s, topic=%s, hours=%s, status=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (subject, topic, hours, status, study_id)
    )

    condb.commit()
    cursor.close()


def study_delete():

    study_id = int(input("Enter the ID of the study record you want to delete: "))

    cursor = condb.cursor()

    query = "DELETE FROM study WHERE id=%s"

    cursor.execute(query, (study_id,))

    condb.commit()
    cursor.close()


def study_manager():

    while True:

        print("\nStudy Manager")
        print("1. Add Study")
        print("2. View Study")
        print("3. Update Study")
        print("4. Delete Study")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            study_add()

        elif choice == '2':
            study_view()

        elif choice == '3':
            study_update()

        elif choice == '4':
            study_delete()

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


#Notes manager

def notes_add():

    title = input("Enter note title (Python Notes / Ideas / Meeting Notes / To-Do): ")
    content = input("Enter note content (Important concepts / Project idea / Meeting points / Things to complete): ")
    category = input("Enter note category (Study / Work / Personal / Ideas): ")

    cursor = condb.cursor()

    query = """
    INSERT INTO notes (title, content, category)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (title, content, category)
    )

    condb.commit()
    cursor.close()


def notes_view():

    cursor = condb.cursor()

    query = "SELECT * FROM notes ORDER BY id ASC"

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()


def notes_update():

    note_id = int(input("Enter the ID of the note you want to update: "))

    title = input("Enter new note title (Python Notes / Ideas / Meeting Notes / To-Do): ")
    content = input("Enter new note content (Important concepts / Project idea / Meeting points / Things to complete): ")
    category = input("Enter new note category (Study / Work / Personal / Ideas): ")

    cursor = condb.cursor()

    query = """
    UPDATE notes
    SET title=%s, content=%s, category=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (title, content, category, note_id)
    )

    condb.commit()
    cursor.close()


def notes_delete():

    note_id = int(input("Enter the ID of the note you want to delete: "))

    cursor = condb.cursor()

    query = "DELETE FROM notes WHERE id=%s"

    cursor.execute(query, (note_id,))

    condb.commit()
    cursor.close()


def notes_manager():

    while True:

        print("\nNotes Manager")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            notes_add()

        elif choice == '2':
            notes_view()

        elif choice == '3':
            notes_update()

        elif choice == '4':
            notes_delete()

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


#Expense manager

def expense_add():

    title = input("Enter expense title (Food / Travel / Shopping / Bills): ")
    amount = input("Enter expense amount (100 / 250 / 500 / 1000): ")
    category = input("Enter expense category (Food / Transport / Shopping / Utilities): ")
    date = input("Enter expense date (2026-09-03 / 2026-09-04): ")

    cursor = condb.cursor()

    query = """
    INSERT INTO expenses (title, amount, category, date)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (title, amount, category, date)
    )

    condb.commit()
    cursor.close()


def expense_view():

    cursor = condb.cursor()

    query = "SELECT * FROM expenses ORDER BY id ASC"

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()


def expense_update():

    expense_id = int(input("Enter the ID of the expense you want to update: "))

    title = input("Enter new expense title (Food / Travel / Shopping / Bills): ")
    amount = input("Enter new expense amount (100 / 250 / 500 / 1000): ")
    category = input("Enter new expense category (Food / Transport / Shopping / Utilities): ")
    date = input("Enter new expense date (2026-09-03 / 2026-09-04): ")

    cursor = condb.cursor()

    query = """
    UPDATE expenses
    SET title=%s, amount=%s, category=%s, date=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (title, amount, category, date, expense_id)
    )

    condb.commit()
    cursor.close()


def expense_delete():

    expense_id = int(input("Enter the ID of the expense you want to delete: "))

    cursor = condb.cursor()

    query = "DELETE FROM expenses WHERE id=%s"

    cursor.execute(query, (expense_id,))

    condb.commit()
    cursor.close()


def expense_manager():

    while True:

        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            expense_add()

        elif choice == '2':
            expense_view()

        elif choice == '3':
            expense_update()

        elif choice == '4':
            expense_delete()

        elif choice == '5':
            break

        else:
            print("Invalid choice.")


#Analytics Section

def analytics_section():

    while True:

        print("\nAnalytics Section")
        print("1. Total Tasks")
        print("2. Completed Tasks")
        print("3. Total Habits")
        print("4. Total Study Hours")
        print("5. Total Notes")
        print("6. Total Expenses")
        print("7. Back")

        choice = input("Enter your choice: ")

        cursor = condb.cursor()

        if choice == '1':

            cursor.execute("SELECT COUNT(*) FROM tasks")
            print("Total Tasks:", cursor.fetchone()[0])

        elif choice == '2':

            cursor.execute(
                "SELECT COUNT(*) FROM tasks WHERE status='completed'"
            )
            print("Completed Tasks:", cursor.fetchone()[0])

        elif choice == '3':

            cursor.execute("SELECT COUNT(*) FROM habits")
            print("Total Habits:", cursor.fetchone()[0])

        elif choice == '4':

            cursor.execute("SELECT SUM(hours) FROM study")
            result = cursor.fetchone()[0]

            if result is None:
                result = 0

            print("Total Study Hours:", result)

        elif choice == '5':

            cursor.execute("SELECT COUNT(*) FROM notes")
            print("Total Notes:", cursor.fetchone()[0])

        elif choice == '6':

            cursor.execute("SELECT SUM(amount) FROM expenses")
            result = cursor.fetchone()[0]

            if result is None:
                result = 0

            print("Total Expenses:", result)

        elif choice == '7':
            cursor.close()
            break

        else:
            print("Invalid choice.")

        cursor.close()


#main

def main():

    while True:

        print("\nWelcome to the Personal Management System")
        print("1. Task Manager")
        print("2. Habit Manager")
        print("3. Study Manager")
        print("4. Notes Manager")
        print("5. Expense Manager")
        print("6. Analytics Section")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_manager()

        elif choice == '2':
            habit_manager()

        elif choice == '3':
            study_manager()

        elif choice == '4':
            notes_manager()

        elif choice == '5':
            expense_manager()

        elif choice == '6':
            analytics_section()

        elif choice == '7':
            print("Exiting the Personal Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
