
# how to made required and opitional fied from pydantic import BaseModel
# and also validate the attribute of your data
# for data validation u can use the Field data type
# this is use the put the constraint on your value
from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of your patient',
    description='name must be less than 50',examples='rahul')]
    #name: str=Field(max_length=50)
    email:EmailStr
    age: int=Field(gt=0,lt=120)# now define the range of the data 
    weight: Annotated[float,Field(gt=0,strict=True)] # this show that your must be put the dat value greater that 0 
    married: Annotated[Optional[bool], Field(default=None, description='...')]
    # married: Annotated[bool,Field(default=None,description='you are married or not')]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]# both can be wright to together
    contact_details:Dict[str,str]


    @field_validator('name')
    @classmethod
    def transform(cls,value):
        return value.upper()


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

# call the function

insert_patient_data(patient1)
upadate_patient_data(patient1)
