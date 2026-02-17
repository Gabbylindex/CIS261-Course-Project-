# Gabe Ranola
# CIS 261 Course Project Week 9 Update
# 02/17/26

import datetime
import os

EMP_FILE = "employees.txt"
USER_FILE = "users.txt"

def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%m/%d/%Y")
        return True
    except ValueError:
        return False

def load_existing_user_ids():
    user_ids = []
    if not os.path.exists(USER_FILE):
        return user_ids
    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            uid, _, _ = line.split("|")
            user_ids.append(uid)
    return user_ids

def add_users():
    print("\nUSER MAINTENANCE (type End to stop)")
    user_ids = load_existing_user_ids()
    with open(USER_FILE, "a") as file:
        while True:
            user_id = input("Enter User ID (or End): ").strip()
            if user_id.lower() == "end":
                break
            if user_id in user_ids:
                print("User ID already exists.")
                continue
            password = input("Enter Password: ").strip()
            auth = input("Enter Authorization (Admin or User): ").strip()
            if auth not in ("Admin", "User"):
                print("Authorization must be Admin or User.")
                continue
            file.write(f"{user_id}|{password}|{auth}\n")
            user_ids.append(user_id)
            print("User added.\n")

def display_all_users():
    print("\nCURRENT USERS")
    if not os.path.exists(USER_FILE):
        print("No user records found.")
        return
    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            user_id, password, auth = line.split("|")
            print(f"User ID: {user_id} | Password: {password} | Authorization: {auth}")
    print()

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization

def login_process():
    if not os.path.exists(USER_FILE):
        print("No user file found.")
        return None
    user_ids = []
    passwords = []
    auth_codes = []
    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            uid, pwd, auth = line.split("|")
            user_ids.append(uid)
            passwords.append(pwd)
            auth_codes.append(auth)
    print("LOGIN")
    entered_id = input("Enter User ID: ").strip()
    entered_pwd = input("Enter Password: ").strip()
    if entered_id not in user_ids:
        print("User ID does not exist.")
        return None
    idx = user_ids.index(entered_id)
    if entered_pwd != passwords[idx]:
        print("Incorrect password.")
        return None
    login_obj = Login(user_ids[idx], passwords[idx], auth_codes[idx])
    print("\nLogin successful.\n")
    return login_obj

def get_date_range():
    while True:
        from_date = input("Enter FROM date (mm/dd/yyyy): ")
        if not valid_date(from_date):
            print("Invalid date.")
            continue
        to_date = input("Enter TO date (mm/dd/yyyy): ")
        if not valid_date(to_date):
            print("Invalid date.")
            continue
        if datetime.datetime.strptime(to_date, "%m/%d/%Y") < datetime.datetime.strptime(from_date, "%m/%d/%Y"):
            print("TO date cannot be earlier.")
            continue
        return from_date, to_date

def get_employee_name():
    return input("Enter employee name (or End): ")

def get_total_hours():
    while True:
        try:
            return float(input("Enter total hours: "))
        except ValueError:
            print("Invalid number.")

def get_hourly_rate():
    while True:
        try:
            return float(input("Enter hourly rate: "))
        except ValueError:
            print("Invalid number.")

def get_tax_rate():
    while True:
        try:
            return float(input("Enter tax rate (decimal): "))
        except ValueError:
            print("Invalid number.")

def write_record_to_file(record):
    with open(EMP_FILE, "a") as file:
        file.write(record + "\n")

def get_report_date():
    while True:
        date_input = input("Enter FROM DATE for report (mm/dd/yyyy) or All: ")
        if date_input.lower() == "all":
            return "All"
        if valid_date(date_input):
            return date_input
        print("Invalid date.")

def run_report(from_date):
    totals = {"total_employees": 0, "total_hours": 0, "total_tax": 0, "total_net_pay": 0}
    print("\nEMPLOYEE PAY REPORT\n")
    try:
        with open(EMP_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                fdate, tdate, name, hours, rate, tax_rate = line.split("|")
                if from_date != "All" and fdate != from_date:
                    continue
                hours = float(hours)
                rate = float(rate)
                tax_rate = float(tax_rate)
                gross = hours * rate
                tax = gross * tax_rate
                net = gross - tax
                print(f"From: {fdate}")
                print(f"To: {tdate}")
                print(f"Employee: {name}")
                print(f"Hours: {hours}")
                print(f"Rate: ${rate:.2f}")
                print(f"Gross: ${gross:.2f}")
                print(f"Tax: ${tax:.2f}")
                print(f"Net: ${net:.2f}\n")
                totals["total_employees"] += 1
                totals["total_hours"] += hours
                totals["total_tax"] += tax
                totals["total_net_pay"] += net
    except FileNotFoundError:
        print("No employee records found.")
        return
    display_totals(totals)

def display_totals(totals):
    print("TOTALS")
    print(f"Employees: {totals['total_employees']}")
    print(f"Hours: {totals['total_hours']}")
    print(f"Taxes: ${totals['total_tax']:.2f}")
    print(f"Net Pay: ${totals['total_net_pay']:.2f}\n")

def main():
    print("CIS261 Project")
    add_users()
    display_all_users()
    login_obj = login_process()
    if login_obj is None:
        return
    print("ACTIVE USER")
    print(f"User ID: {login_obj.user_id}")
    print(f"Password: {login_obj.password}")
    print(f"Authorization: {login_obj.authorization}\n")
    if login_obj.authorization == "Admin":
        print("Admin Access: Enter and Display Data\n")
        while True:
            from_date, to_date = get_date_range()
            name = get_employee_name()
            if name.lower() == "end":
                break
            hours = get_total_hours()
            rate = get_hourly_rate()
            tax_rate = get_tax_rate()
            record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}"
            write_record_to_file(record)
            again = input("Add another employee? (y/n): ").lower()
            if again != "y":
                break
        report_date = get_report_date()
        run_report(report_date)
    elif login_obj.authorization == "User":
        print("User Access: Display Only\n")
        report_date = get_report_date()
        run_report(report_date)

if __name__ == "__main__":
    main()