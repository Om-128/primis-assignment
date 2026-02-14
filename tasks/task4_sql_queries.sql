-- Fetch all employees
SELECT * FROM employees;

-- Count employees
SELECT COUNT(*) FROM employees;

-- Average salary by department
SELECT department, AVG(salary) 
FROM employees
GROUP BY department;

-- Department with highest average salary
SELECT department
FROM employees
GROUP BY department
ORDER BY AVG(salary) DESC
LIMIT 1;

-- Highest paid employee
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Employees joined in 2023
SELECT *
FROM employees
WHERE YEAR(join_date) = 2023;

-- Count employees per department
SELECT department, COUNT(*)
FROM employees
GROUP BY department;