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

print(patiendt_object)
print(patiendt_object.address.city)
print(patiendt_object.address.state)
print(patiendt_object.address.pincode)