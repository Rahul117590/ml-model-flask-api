from pydantic import BaseModel

# make sure that you inheriate  the base model in your class
class Patient(BaseModel):
    name:str
    age:int

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

def upadate_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('update')


# step 2
patient_info={'name':'rakhi','age': 30}

patient1=Patient(**patient_info)

# call the function
insert_patient_data(patient1)
upadate_patient_data(patient1)
# step 3
# put that patient in the insert_patient_data that help to work it properly





