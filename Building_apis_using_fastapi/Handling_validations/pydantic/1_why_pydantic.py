# def insert(name:str,age:int):
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError('age cant be negative')
#         else:
#             print(name)
#             print(age)
#             print('insert in db')
#     else:
#         raise TypeError('incorrect data type')
    
# insert('saransh',1)

# the above code is not scalable for the production code and we have to right custom code for this and not scalable at all

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    # Patient's name, max 50 chars, with examples for documentation
    name: Annotated[str, Field(max_length=50, title='name of the patient', description='give the name of patient in less than 50 characters', examples=['amit','nitish'])]
    
    # Must be a valid email
    email: EmailStr
    
    # Must be a valid URL
    linkedin_url: AnyUrl
    
    # Age must be >0 and <120
    age: int = Field(gt=0, lt=120)
    
    # Weight must be positive float, strict type checking
    weight: float = Field(gt=0, strict=True)
    
    # Default is False
    married: bool = False
    
    # Optional list of allergies, max 5 items
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    
    # Dictionary for contact details (e.g., phone, address)
    contact_details: Dict[str, str]

def insert(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.linkedin_url)
    print(patient.contact_details['phone'])
    print(patient.allergies)
    print('inserted')

def update(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

patient_info={'name':'nitish','email':'saransh@gmail.com','age':12 ,'weight':75.3,'married':True,'allergies':['pollen','sugar'],'contact_details':{'phone':'9841080030'},'linkedin_url':'https://www.linkedin.com/in/saransh-basu-86a4152b5/'}
patient1=Patient(**patient_info)
insert(patient1)

# patient_info1={'name':'nitish','email':'saransh@gmail.com','age':12 ,'weight':75.3,'contact_details':{'phone':'9841080030'}}
# patient2=Patient(**patient_info1)
# insert(patient2)