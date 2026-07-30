from pydantic import BaseModel
from typing import List,Dict
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.age)
    print(patient.contact_details)
    print(patient.allergies)
    print(patient.married)
    print('insertion complete')
    
def upadate_patient_data(patient:Patient):
    print(patient.name)
    print(patient.weight)
    print(patient.age)
    print(patient.contact_details)
    print(patient.allergies)
    print(patient.married)
    print('updation complete')

patient_info={'name':'Rahul','age':30,'weight':60.5,'married':True,
'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'9485858948'} }
patient1=Patient(**patient_info)

# call the function

insert_patient_data(patient1)
upadate_patient_data(patient1)
