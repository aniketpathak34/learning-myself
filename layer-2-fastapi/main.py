from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import patients_creation, patient_query, delete_patient, put_patient
import traceback

app = FastAPI()


class Patient(BaseModel):
    id: int
    name: str
    age: int

class PatientCreate(BaseModel):
    name: str
    age: int



patients = []

@app.get("/")
def home():
    return {"message":"API is running"}


@app.get("/patients")
def get_patients():
    return patient_query()

@app.post("/patients")
def create_patient(patient: PatientCreate):
    try:
        id = patients_creation(patient)
        print(patient, "=============")
        patient = Patient(id=id, name=patient.name, age=patient.age)
        return patient
    except Exception as e:
        print(traceback.format_exc(), "===================format trackback")


@app.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    data = patient_query(patient_id)
    if data:
        return data
    raise HTTPException(status_code=404, detail="Patient not found")

@app.put("/patients")
def update_patient_by_id(Patient_update: Patient):
    data = put_patient(Patient_update)
    return 
 
@app.delete("/patients/{patient_id}")
def delete_patient_by_id(patient_id: int):
    patient = patient_query(patient_id)
    if patient:
        done = delete_patient(patient)
        print(done, "-----------------done")
        return {"message":f"patient got delete for {patient_id}"}

    raise HTTPException(status_code=404, detail="Patient does not exist") 
