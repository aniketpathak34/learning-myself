from pydantic import BaseModel, EmailStr, Field
from datetime import date

class Patient(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: EmailStr
    code: str = Field(pattern=r"^\d{6}$")

def load_record(data: dict) -> Patient:
    return Patient(**data)

data = {"first_name":"anku", "last_name":"pathu", "date_of_birth":"2000-02-12", "email":"anus@gmail.com", "code":"121212"}
good = load_record(data)
print(good)

bad = {"first_name":"anku", "last_name":"pathu", "date_of_birth":"2000-02-12", "email":"anus@gmail.com", "code":"12121"}
try:
    bad = load_record(bad)
except Exception as e:
    print("Rejected", e)