from pydantic import BaseModel,EmailStr,AnyUrl,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

# Purpose: Validate multiple fields together or check conditions that involve more than one field.
# ✅ Use case: When validation depends on multiple fields or their relationships.

    @model_validator(mode='after')
    def validate_emergecny_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('patient must have emergency number')
        return model

def insert(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details['phone'])
    print(patient.allergies)
    print('inserted')

patient_info={'name':'saransh basu','email':'saransh@hdfc.com','age':70 ,'weight':75.3,'married':True,'allergies':['pollen','sugar'],'contact_details':{'phone':'9841080030','emergency':'981525'}}
patient1=Patient(**patient_info)
insert(patient1)
