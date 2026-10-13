from fastapi import FastAPI,HTTPException
from typing import List
from models_val import Employee

employees_db: List[Employee] = []

app=FastAPI()

#1 read all employees
@app.get('/employees',response_model=List[Employee])
def get_employees():
    return employees_db

#2 read a specificc employee
@app.get('/employees/{emp_id}',response_model=Employee)
def get_one(emp_id:int):
    for index,value in enumerate(employees_db):
        if value.id==emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404,detail="employee not found")

#3 add an employee
@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail='Employee already exists')
    employees_db.append(new_emp)
    return new_emp

#4 update an employee
@app.put('/update_employee/{emp_id}',response_model=Employee)
def update_employee(emp_id:int,updated_employee:Employee):
    for index,value in enumerate(employees_db):
        if value.id==emp_id:
            employees_db[index]=updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail='Employee Not Found')

#5delete an employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id:int):
    for index,value in enumerate(employees_db):
        if value.id==emp_id:
            del employees_db[index]
            return {"message":"employee deleted sucessfully"}
    raise HTTPException(status_code=404,detail='not found')