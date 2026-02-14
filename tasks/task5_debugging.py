import os
import sys
from custom_exception import CustomException

import csv
from datetime import datetime

# Good Practice: Dynamic base directory instead of hardcoded absolute path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
file_path = os.path.join(BASE_DIR, "dataset", "employees.csv")

def read_employees(file):
    """
    Bugs Fixed:
    - File not closed properly (used with open)
    - Salary was string (converted to float)

    Good Practice:
    - Safe file handling
    - Proper type conversion
    """
    try:
        employees = []
        with open(file, "r") as f:
            reader = csv.DictReader(f)
        
            for row in reader:
                row["salary"] = float(row["salary"])
                employees.append(row)
        
        return employees
    except Exception as e:
        raise CustomException(e, sys)

def average_salary_by_department(employees):
    """
    Bugs Fixed:
    - dept_count not initialized (KeyError)
    - Salary type issue fixed earlier

    Good Practice:
    - Proper dictionary initialization
    - Clean aggregation logic
    """
    try:
        dept_salary = {}
        dept_count = {}
        
        for emp in employees:
            dept = emp["department"]
            
            if dept not in dept_salary:
                dept_salary[dept] = 0
                dept_count[dept] = 0
        
            dept_salary[dept] += emp["salary"]
            dept_count[dept] += 1
        
        avg_salary = {}

        for d in dept_salary:
            avg_salary[d] = dept_salary[d] / dept_count[d]
        
        return avg_salary

    except Exception as e:
        raise CustomException(e, sys)

def employees_joined_2023(employees):

    """
    Bugs Fixed:
    - Wrong date format
    - Compared int year with string

    Good Practice:
    - Correct datetime parsing
    - Correct integer comparison
    """
    result = []
    
    for emp in employees:

        join_date = datetime.strptime(emp["join_date"], "%Y-%m-%d")
        
        if join_date.year == 2023:
            result.append(emp)
    
    return result


def main():

    print("\n-------------------------------------------------------------\n")

    employees = read_employees(file_path)
    
    print("Total Employees:", len(employees))

    print("\n-------------------------------------------------------------\n")

    avg = average_salary_by_department(employees)
    print("Average Salary:", avg)

    print("\n-------------------------------------------------------------\n")

    joined_2023 = employees_joined_2023(employees)
    print("Employees joined in 2023:", joined_2023)

    print("\n-------------------------------------------------------------\n")


if __name__=="__main__":
    main()