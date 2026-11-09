from pydantic import BaseModel,EmailStr,AnyUrl, Field,field_validator,model_validator
from typing import Dict,Annotated

class Patient(BaseModel):
    name:str
    age:int = Field(gt=0)
    contact_info :Dict[str,str]
    email:EmailStr # used for varifying email formate
    linkedin_url:AnyUrl #checks the url formate 
    marid:bool = Field(default=None)
    
    @model_validator(mode='after')
    @classmethod
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_info:
            raise ValueError("patient older than 60 must have an emergency contact")
        return model
    
    
def insert_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print("inserted")
    
patient_info={"name":"surya","age":67,"contact_info":{"phone":"+9184******45","emergency":"+9194******00 "},
"email":"ssinghbisht98@gmail.com","linkedin_url":"https://in.linkedin.com/123"
}
p1=Patient(**patient_info)
insert_data(p1)

#this code will only run if a person have emergency contact whose age is more than 60 
#if less age than 60 it will work without emergency contact 