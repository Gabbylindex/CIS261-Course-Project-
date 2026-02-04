# Gabe Ranola
# CIS261
# Course Project Week 7 Update 2/4/26

import datetime

FILE_NAME = "employees.txt"

# ---------------------------
# Validation
# ---------------------------
def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, "%m/%d/%Y")
        return True
    except ValueError:
        return False


# ---------------------------
# Input functions
# ---------------------------
def get_date_range():
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
    while not valid_date(from_date):
        print("Invalid date format.")
        from_date = input("Enter FROM date (mm/dd/yyyy): ")

    to_date = input("Enter TO date (mm/dd/yyyy): ")
    while not valid_date(to_date):
        print("Invalid date format.")
        to_date = input("Enter TO date (mm/dd/yyyy): ")

    return from_date, to_date


def get_employee_name():
    return input("Enter employee name (or type 'End' to finish): ")


def get_total_hours():
    return float(input("Enter total hours worked: "))


def get_hourly_rate():
    return float(input("Enter hourly rate: "))


def get_tax_rate():
    return float(input("Enter income tax rate (as a decimal): "))


# ---------------------------
# Write record to file
# ---------------------------
def write_record_to_file(record):
    with open(FILE_NAME, "a") as file:
        file.write(record + "\n")


# ---------------------------
# Report date input
# ---------------------------
def get_report_date():
    while True:
        date_input = input("\nEnter FROM DATE for report (mm/dd/yyyy) or 'All': ")

        if date_input.lower() == "all":
            return "All"

        if valid_date(date_input):
            return date_input

        print("Invalid date format. Try again.")


# ---------------------------
# Read file and generate report
# ---------------------------
def run_report(from_date):
    totals = {
        "total_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }

    print("\n================ EMPLOYEE PAY REPORT ================\n")

    try:
        with open(FILE_NAME, "r") as file:
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

                print(f"From Date: {fdate}")
                print(f"To Date:   {tdate}")
                print(f"Employee:  {name}")
                print(f"Hours:     {hours}")
                print(f"Rate:      ${rate:.2f}")
                print(f"Gross Pay: ${gross:.2f}")
                print(f"Tax Rate:  {tax_rate:.2%}")
                print(f"Tax:       ${tax:.2f}")
                print(f"Net Pay:   ${net:.2f}")
                print("----------------------------------------------------\n")

                totals["total_employees"] += 1
                totals["total_hours"] += hours
                totals["total_tax"] += tax
                totals["total_net_pay"] += net

    except FileNotFoundError:
        print("No employee records found.")
        return

    display_totals(totals)


# ---------------------------
# Display totals
# ---------------------------
def display_totals(totals):
    print("\n==================== TOTALS ====================")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours:     {totals['total_hours']}")
    print(f"Total Taxes:     ${totals['total_tax']:.2f}")
    print(f"Total Net Pay:   ${totals['total_net_pay']:.2f}")
    print("================================================\n")


# ---------------------------
# Main Program
# ---------------------------
def main():
    print("Employee Payroll Entry\n")

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


main()