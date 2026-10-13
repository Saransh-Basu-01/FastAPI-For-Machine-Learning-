
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

# Purpose: Validate or transform a specific field after input.When validation or transformation is needed for a single field.
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

def insert(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details['phone'])
    print(patient.allergies)
    print('inserted')

patient_info={'name':'saransh basu','email':'saransh@hdfc.com','age':12 ,'weight':75.3,'married':True,'allergies':['pollen','sugar'],'contact_details':{'phone':'9841080030'}}
patient1=Patient(**patient_info)
insert(patient1)