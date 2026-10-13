from pydantic import BaseModel


class  Address(BaseModel):
    city:str
    state:str
    pincode:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'city':'ktm','state':'bkt','pincode':'12230'}
Adresss_object=Address(**address_dict)

patient_dict={'name':'saransh basu','gender':'male','age':35,'address':Adresss_object}
patiendt_object=Patient(**patient_dict)

temp=patiendt_object.model_dump() #converts to dict 
temp1=patiendt_object.model_dump_json() #converts to json 
print(temp)
temp2=patiendt_object.model_dump(include=['name','gender']) 
print(temp2)
temp3=patiendt_object.model_dump(exclude=['name','gender'])
print(temp3)