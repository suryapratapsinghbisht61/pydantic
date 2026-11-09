from pydantic import BaseModel,EmailStr,AnyUrl, Field
from typing import Dict

class Patient(BaseModel):
    name:str = Field(max_length=50)
    age:int = Field(gt=0)
    contact_info :Dict[str,str]
    email:EmailStr # used for varifying email formate
    linkedin_url:AnyUrl #checks the url formate 
    
def insert_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print("inserted")
    
patient_info={"name":"surya","age":20,"contact_info":{"phone":"+9184******45","other_no":"+9194******00 "},
"email":"ssinghbisht98@gmail.com","linkedin_url":"https://in.linkedin.com/123"
}
p1=Patient(**patient_info)
insert_data(p1)