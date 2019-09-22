CREATE TABLE employees (
	emp_no int PRIMARY KEY NOT NULL,
	birth_date date,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	gender VARCHAR(10),
	hire_date date
)
;

CREATE TABLE departments (
	dept_no VARCHAR(30) PRIMARY KEY NOT NULL,
	dept_name VARCHAR(30)
)
;

CREATE TABLE titles (
	emp_no int,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	title VARCHAR NOT NULL,
	from_date date,
	to_date date
)
;

CREATE TABLE salaries (
	emp_no int PRIMARY KEY NOT NULL,
	salary int,
	from_date date,
	to_date date
)
;

CREATE TABLE dept_manager (
	dept_no VARCHAR(30),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	emp_no int,
	from_date date,
	to_date date
)
;

CREATE TABLE dept_emp (
	emp_no int,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR(30),
	from_date date,
	to_date date
)
;