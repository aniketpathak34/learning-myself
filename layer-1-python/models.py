from pydantic import BaseModel, EmailStr
from datetime import date

class Patient(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: EmailStr
    code: str




print(Patient(first_name="anku", last_name="pathu", date_of_birth="2000-02-12", email="anus@gmail.com", code="121212"))