from pydantic import BaseModel,EmailStr,AnyUrl, Field,computed_field
from typing import Dict,Annotated

class Patient(BaseModel):
    name:str
    age:int = Field(gt=0)
    contact_info :Dict[str,str]
    email:EmailStr # used for varifying email formate
    linkedin_url:AnyUrl #checks the url formate 
    marid:bool | None=None
    waight:float
    hight:float

    @computed_field
    @property
    def bmi_cal(self)-> float:
        bmi=round(self.waight/(self.hight**2),2)
        return bmi
    
def insert_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print("BMI",patient.bmi_cal)
    print("inserted")
    
patient_info={"name":"surya","age":20,"contact_info":{"phone":"+9184******45","other_no":"+9194******00 "},
"email":"ssinghbisht98@gmail.com","linkedin_url":"https://in.linkedin.com/123","waight":85,"hight":1.79
}
p1=Patient(**patient_info)
insert_data(p1)