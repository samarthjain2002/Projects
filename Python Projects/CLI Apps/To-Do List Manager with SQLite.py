import sqlite3
import os


def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK (status IN ('Complete', 'Incomplete')),
        priority TEXT CHECK (priority IN ('High', 'Medium', 'Low')),
        duedate DATETIME
    )
    ''')

    conn.commit()
    conn.close()


def add_task():
    title = input("Enter the task title:\t")
    description = input("Enter the task description:\t")
    status = input("Enter the status: Complete/Incomplete:\t")
    priority = input("Enter the task priority: High/Medium/Low:\t")
    duedate = input("Enter the due date and time ('YYYY-MM-DD HH:MM:SS')\t")
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO tasks (title, description, status, priority, duedate)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, status, priority, duedate))

        conn.commit()
        print("Task added successfully")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def next_task():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = '''
        SELECT id, title, description, status, priority, duedate
        FROM tasks
        WHERE status = 'Incomplete'
        ORDER BY
            CASE
                WHEN 'High' THEN 1
                WHEN 'Medium' THEN 2
                WHEN 'Low' THEN 3
            END ASC,
            duedate ASC
        LIMIT 1
    '''

    task = cursor.execute(query)

    try:
        cursor.execute(query)
        task = cursor.fetchone()
        
        if task:
            print("\nThe most important task:")
            print(f"ID: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nStatus: {task[3]}\nPriority: {task[4]}\nDuedate: {task[5]}\n\n")
        else:
            print("No incomplete tasks found.")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        conn.close()


def remove_task():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    id = input("Enter the ID of the task to be deleted:\t")
    if id.isdigit():
        id = int(id)
    else:
        print("Enter a numeric ID")
        return

    try:
        cursor.execute('''
            DELETE FROM tasks
            WHERE id = ?
        ''', (id, ))

        conn.commit()

        if cursor.rowcount == 0:
            print(f"No task found with ID {id}")
        else:
            print("The task was successfully removed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def list_tasks():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    tasks = cursor.execute('''
        SELECT * FROM tasks
    ''')

    if tasks:
        print("\nTasks")
        for task in tasks:
            print(f"\nID: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nStatus: {task[3]}\nPriority: {task[4]}\nDuedate: {task[5]}")
    else:
        print("No incomplete tasks were found")

    conn.close()


def mark_complete():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    id = input("Enter the ID of the task to be marked completed:\t")
    if id.isdigit():
        id = int(id)
    else:
        print("Enter a numeric ID")
        return
    
    try:
        cursor.execute('''
            UPDATE tasks
            SET status = 'Complete'
            WHERE id = ?
        ''', (id, ))

        if cursor.rowcount == 0:
            print(f"No task found with ID {id}")
        else:
            conn.commit()
            print("The task is marked as completed")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()



if __name__ == "__main__":

    if not os.path.exists('database.db'):
        create_db()

    while True:
        print("\n\nTASK MANAGER: Enter your choice")
        choice = int(input("1. Add task, 2. Find most important task, 3. Remove Task, 4. List tasks, 5. Mark as completed, 6. Exit\n"))
        match choice:
            case 1:
                add_task()
            case 2:
                next_task()
            case 3:
                remove_task()
            case 4:
                list_tasks()
            case 5:
                mark_complete()
            case 6:
                exit()
            case _:
                print("Invalid choice, enter the choice again\n")