from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Optional
class Student(BaseModel):
    name: str="ashu"
    age: Optional[int]=None
    # email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=7,description=" A Decimal value repesenting the cgpa of the student")


    

new_student={'age':'32',"cgpa":4}

student=Student(**new_student)
print(student) 