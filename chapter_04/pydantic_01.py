def insert_patient_data(name,age):
    print(name)
    print(age)
    print('inseted into the data base ')

insert_patient_data('rahul','twintyone')

'''
here we can see that any type of data can be fill inside the function whether it require 
string and integer but if we put the both the string value in it then still it is accptaable so 
these create a big problem when u wrok on the big program file 
there is the problem of type validation . Python do not follow the strick schema 

so the one way is typehuntying in that if  your other program use that function that these hint show 
'''
def insert_patient_data1(name:str,age:int):
    print(name)
    print(age)
    print('data is inseted')

insert_patient_data1('rakhi',30)

'''
but still if the programmer do not see your typing or weather if he ignore your hint part
then still the progamm will be work so due to that reason it is not cure of that problem
beacase type hunting never create error 
as a programmer we not able to inforce him  '''

def insert_patient_data2(name:str,age:int):
    if type(name)==str and type(age)== int:
        print(name)
        print(age)
        print('your data is inserted easily ' )
    else:
        raise TypeError('incorrect data type')


insert_patient_data2('rakhi',21)
''' this little peace of logic define the secure of input partion'''

# pydentic basically solve this problem that you able to achive the order of type error

