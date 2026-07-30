'''
why naste model like if your use the str in the address model than what happend than
in case if have to task to extract out only the pin code part or somthing other part
then it is going to very hard so that why nasted loop comes into the existance 
u can inheriate the property or attribute from the other loop'''

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

# we have to make the object of pydantic model
address_dict={'city':'gurgaon','state':'haryana','pin':'237263'}

# we make the object of that raw dictonary
address1=Address(**address_dict)

patient_info={
    'name':'rahul',
    'gender':'Male',
    'age':'65',
    'address':address1
}

# now we make the object of patient pydantic model
# we put the duble star for extract the dictionary from that object
patient1=Patient(**patient_info)



print(patient1)
# incase if you want to extract the patient pincode details than it is also easy for you
print("PIN :",patient1.address.pin)