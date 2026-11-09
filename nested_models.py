from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import Dict,Annotated

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int 
    address:Address
address_info={"city":'gurgaon',"state":"Haryana","pin":"122001"}

address1=Address(**address_info)

patient_info={'name':"surya","gender":"Male","age":20,"address":address1}
patient1=Patient(**patient_info)

print(patient1)
print(patient1.address.pin)