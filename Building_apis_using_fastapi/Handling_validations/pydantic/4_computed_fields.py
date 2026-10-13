from pydantic import BaseModel,EmailStr,AnyUrl,computed_field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float #kg
    height:float #meters
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]
# Automatically derive a field value from other fields.When you want a read-only value computed from existing fields, without storing it explicitly

    @computed_field()
    @property
    def calculate_bmi(self) -> float:
        bmi=round((self.weight)/(self.height**2),2)
        return bmi 
    
def insert(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print('BMI',patient.calculate_bmi)
    print('inserted')

patient_info={'name':'saransh basu','email':'saransh@hdfc.com','age':70 ,'weight':75.3,'height':25,'married':True,'allergies':['pollen','sugar'],'contact_details':{'phone':'9841080030','emergency':'981525'}}
patient1=Patient(**patient_info)
insert(patient1)