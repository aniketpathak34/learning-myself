from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Patient(BaseModel):
    id: int
    name: str
    age: int

patients = []

@app.get("/")
def home():
    return {"message":"API is running"}


@app.get("/patients")
def get_patients():
    return patients


@app.post("/patients")
def create_patient(patient: Patient):
    patients.append(patient)
    return patient


@app.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient

    raise HTTPException(status_code=404, detail="Patient not found")

@app.put("/patients")
def update_patient_by_id(Patient_update: Patient):
    id = Patient_update.id
    for patient in patients:
        if patient.id == id:
            patient.name = Patient_update.name
            patient.age = Patient_update.age
            return patient
        

    raise HTTPException(status_code=404, detail="Patient does not exist")

@app.delete("/patients/{patient_id}")
def delete_patient_by_id(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            patients.remove(patient)
            return {"message":f"patient got delete for {patient_id}"}

    raise HTTPException(status_code=404, detail="Patient does not exist") 
