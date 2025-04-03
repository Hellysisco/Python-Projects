import datetime

# Initialize empty dictionaries to store users and their data
user_database = {}
user_profiles = {}
user_tasks = {}


def register_user():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in user_database:
        print("Username already exists! Try again.")
        return

    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long!")
        return

    user_database[username] = password

    # Collect profile details during registration
    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    while True:
        try:
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            datetime.datetime.strptime(dob, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    user_profiles[username] = {
        "name": name,
        "address": address,
        "phone": phone,
        "date_of_birth": dob
    }

    # Initialize tasks list for the new user
    user_tasks[username] = []

    print("Registration successful!")


def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in user_database:
        print("Username not found! Please register first.")
        return

    password = input("Enter your password: ")
    if user_database[username] == password:
        print(f"\nWelcome back, {username}!")
        user_dashboard(username)
    else:
        print("Incorrect password! Try again.")


def view_profile(username):
    print(f"\n--- Profile ---")
    profile = user_profiles[username]
    print(f"Name: {profile['name']}")
    print(f"Address: {profile['address']}")
    print(f"Phone Number: {profile['phone']}")
    print(f"Date of Birth: {profile['date_of_birth']}")


def update_profile(username):
    print("\n--- Update Profile ---")
    profile = user_profiles[username]

    print("Current Details:")
    view_profile(username)

    print("\nLeave a field blank to keep the current value.")
    name = input("Enter new name (current: {}): ".format(profile['name'])) or profile['name']
    address = input("Enter new address (current: {}): ".format(profile['address'])) or profile['address']
    phone = input("Enter new phone number (current: {}): ".format(profile['phone'])) or profile['phone']

    while True:
        dob_input = input("Enter new date of birth (current: {}, YYYY-MM-DD): ".format(profile['date_of_birth']))
        if not dob_input:
            dob = profile['date_of_birth']
            break
        try:
            datetime.datetime.strptime(dob_input, '%Y-%m-%d')
            dob = dob_input
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    user_profiles[username] = {
        "name": name,
        "address": address,
        "phone": phone,
        "date_of_birth": dob
    }

    print("Profile updated successfully!")


def add_task(username):
    print("\n--- Add Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    task = {
        "title": title,
        "description": description,
        "status": "Pending"
    }

    user_tasks[username].append(task)
    print("Task added successfully!")


def view_tasks(username):
    print("\n--- Your Tasks ---")
    if not user_tasks[username]:
        print("No tasks found.")
        return

    for idx, task in enumerate(user_tasks[username], 1):
        print(f"{idx}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}\n")


def update_task(username):
    view_tasks(username)
    if not user_tasks[username]:
        return

    try:
        task_idx = int(input("Enter task number to update: ")) - 1
        task = user_tasks[username][task_idx]

        print("\nCurrent Task Details:")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")

        title = input("Enter new title (leave blank to keep current): ") or task['title']
        description = input("Enter new description (leave blank to keep current): ") or task['description']
        status = input("Enter new status (Pending/In Progress/Completed): ") or task['status']

        task['title'] = title
        task['description'] = description
        task['status'] = status

        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(username):
    view_tasks(username)
    if not user_tasks[username]:
        return

    try:
        task_idx = int(input("Enter task number to delete: ")) - 1
        deleted_task = user_tasks[username].pop(task_idx)
        print(f"Task '{deleted_task['title']}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def user_dashboard(username):
    while True:
        print(f"\n--- Dashboard: {username} ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Change Password")
        print("4. Task Manager")
        print("5. Logout")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            update_profile(username)
        elif choice == "3":
            change_password(username)
        elif choice == "4":
            task_menu(username)
        elif choice == "5":
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid choice! Please try again.")


def task_menu(username):
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Return to Dashboard")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            update_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")


def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")
    if user_database[username] != old_password:
        print("Incorrect current password! Password not changed.")
        return

    new_password = input("Enter a new password: ")
    if len(new_password) < 6:
        print("Password must be at least 6 characters long!")
        return

    user_database[username] = new_password
    print("Password updated successfully!")


# Main program loop
while True:
    print("\n--- User Dashboard Management System ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")