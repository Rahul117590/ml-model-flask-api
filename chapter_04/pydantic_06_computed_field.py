# computed filed

from pydantic import BaseModel,EmailStr,model_validator,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    allergies:List[str]
    height:float
    contact_details:Dict[str,str]
    married:bool

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient:Patient):
        print(patient.name)
        print(patient.weight)
        print(patient.age)
        print(patient.contact_details)
        print(patient.allergies)
        print(patient.married)
        print('BMI',patient.bmi)
        print('insertion complete')
    
def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.weight)
        print(patient.age)
        print(patient.contact_details)
        print(patient.allergies)
        print(patient.married)
        print(patient.bmi)
        print('insertion complete')

patient_info = {
    'name': 'nitesh',
    'email': 'abc@gmail.com',
    'age': 60,
    'weight': 60,
    'married': True,
    'height':1.7,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '23858343', 'emergency': '786789766'}
}
patient1=Patient(**patient_info)
update_patient_data(patient1)
insert_patient_data(patient1)
    