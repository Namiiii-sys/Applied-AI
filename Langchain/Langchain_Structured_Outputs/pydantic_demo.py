from pydantic import BaseModel , EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Unknown'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=4, description='A decimal value')

new_student = {'age': '18','email':'absv@gmail.com', 'cgpa':5.5}
Student = Student(**new_student)

Student_dict = dict(Student)
print(Student_dict['age'])

Student_json = Student.model_dump_json()
print( Student_json )