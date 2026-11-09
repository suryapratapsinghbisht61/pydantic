from pydantic import BaseModel,EmailStr,AnyUrl,field_validator,Field
from typing import Dict,List,Annotated

class patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    contact:Dict[str,str]
    marid:bool = Field(default=None)
    
    @field_validator('email')
    @classmethod
    def email_validatore(cls,value):
        valid_domain=['hdfc.com','icici.com']
        domain_name=value.split("@")[-1]   
        if domain_name not in valid_domain:
            raise ValueError('not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

patient_info={"name":"surya","age":20,
"email":"ssinghbisht98@hdfc.com",'''now if we do not use @hdfc.com or 
@icici.com at the end it will not work and iven if we try @gmail.com''' "contact":{"ph_no":"844******5"}}

p1=patient(**patient_info)