#model_validator=
from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    allergies:List[str]
    contact_details:Dict[str,str]
    married:bool


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age> 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have the contect details')
        return model

def update_patient_data(patient:Patient):
        print(patient.name)
        print(patient.weight)
        print(patient.age)
        print(patient.contact_details)
        print(patient.allergies)
        print(patient.married)
        print('insertion complete')
    
def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.weight)
        print(patient.age)
        print(patient.contact_details)
        print(patient.allergies)
        print(patient.married)
        print('insertion complete')
    
patient_info = {
    'name': 'nitesh',
    'email': 'abc@gmail.com',
    'age': 60,
    'weight': 60,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '23858343', 'emergency': '786789766'}
}
patient1=Patient(**patient_info)
update_patient_data(patient1)
insert_patient_data(patient1)


