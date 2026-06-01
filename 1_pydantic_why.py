# def insert_patient_data(name: str,age: int):
    
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError('Age cant be negative')
#         else:
#             print(name)
#             print(age)
#             print('inserted into database')
#     else:
#         raise TypeError("Incorrect data type")
    
# #type validation and data validation - pydantic solve this problem
# def update_patient_data(name: str,age: int):
    
#     if type(name)==str and type(age)==int:
#         if age<0:
#             raise ValueError('Age cant be negative')
#         else:
#             print(name)
#             print(age)
#             print('updated')
#     else:
#         raise TypeError("Incorrect data type")

# insert_patient_data('nitish',30)
from pydantic import BaseModel

class Patient(BaseModel):

    name:str
    age:int

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')
patient_info={'name':'nitish','age':'30'}

patient1=Patient(**patient_info)

update_patient_data(patient1)
