import os
import sys
import pandas as pd

from custom_exception import CustomException

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INPUT_FILE = os.path.join(BASE_DIR, "dataset", "employees.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "task1_output", "employees_2023.csv")

class DataProcessing:
    
    def __init__(self):

        self.input_file_path = INPUT_FILE
        self.output_file_path = OUTPUT_FILE

    def load_data(self):
        try:
            # Read CSV
            df = pd.read_csv(self.input_file_path)

            df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
            df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

            return df

        except Exception as e:
            raise CustomException(e, sys)
    
    def process(self, df):
        try:
            # Total number of employees
            total_employees = len(df)

            # Average salary by department
            average_salary_by_dept = df.groupby('department')['salary'].mean().round(2)

            # Department with highest average salary
            highest_dept = average_salary_by_dept.idxmax()

            # Employee(s) with highest salary
            highest_emp = df.nlargest(3, "salary")
            top3 = highest_emp[["name", "department", "salary"]]

            # Employeed who joined in 2023
            joined_2023 = df[df["join_date"].dt.year == 2023]

            # Export 2023 employees to employees_2023.csv
            output_dir = os.path.dirname(self.output_file_path)
            os.makedirs(output_dir, exist_ok=True)

            joined_2023.to_csv(self.output_file_path, index=False)

            return {
                "total_employees" : total_employees,
                "average_salary_by_dept": average_salary_by_dept,
                "highest_dept" : highest_dept,
                "top3" : top3,
                "joined_2023" : joined_2023
            }

        except Exception as e:
            raise CustomException(e, sys)

    def main(self):

        df = self.load_data()

        print("\n-------------------------------------------------------------\n")

        print("Data Loaded Successfully...")

        print("\n-------------------------------------------------------------\n")

        results = data_preprocessing.process(df)

        print("Total Employees:", results["total_employees"])

        print("\n-------------------------------------------------------------\n")

        print("Average Salary by Department:")
        print(results["average_salary_by_dept"])

        print("\n-------------------------------------------------------------\n")

        print("Department With Highest Salaries:", results["highest_dept"])

        print("\n-------------------------------------------------------------\n")

        print("Employee(s) with highest salary:")
        print(results["top3"])
        
        print("\n-------------------------------------------------------------\n")

        print("Employees who joined 2023:")
        print(results["joined_2023"])
        print()
        print("employees_2023.csv file saved in task1_output/")

        print("\n-------------------------------------------------------------\n")


if __name__=="__main__":
    
    data_preprocessing = DataProcessing()
    data_preprocessing.main()