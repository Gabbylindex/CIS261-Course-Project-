# Gabe Ranola
# CIS261
# Course Project Week 3 1/6/26


def get_date_range():
    from_date = input("Enter FROM date (mm/dd/yyyy): ")
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



def process_employees(employee_list):
    totals = {
        "total_employees": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }

    print("\n================ EMPLOYEE PAY REPORT ================\n")

    for emp in employee_list:
        from_date, to_date, name, hours, rate, tax_rate = emp

        gross = hours * rate
        tax = gross * tax_rate
        net = gross - tax

        print(f"From Date: {from_date}")
        print(f"To Date:   {to_date}")
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

    return totals



def display_totals(totals):
    print("\n==================== TOTALS ====================")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours:     {totals['total_hours']}")
    print(f"Total Taxes:     ${totals['total_tax']:.2f}")
    print(f"Total Net Pay:   ${totals['total_net_pay']:.2f}")
    print("================================================\n")



def main():
    employee_list = []

    while True:
        from_date, to_date = get_date_range()
        name = get_employee_name()

        if name.lower() == "end":
            break

        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        employee_list.append([from_date, to_date, name, hours, rate, tax_rate])

        again = input("Add another employee? (y/n): ").lower()
        if again != "y":
            break

    totals = process_employees(employee_list)
    display_totals(totals)


main()
