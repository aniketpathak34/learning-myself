from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import traceback
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db, Patients

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
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patients).all()

@app.post("/patients")
def create_patient(patient_in: PatientCreate, db: Session = Depends(get_db)):
    try:
        new_patient = Patients(name=patient_in.name, age=patient_in.age)
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)
        return new_patient
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")

                            
# 3. ID नुसार पेशंट शोधा
@app.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = db.get(Patients, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# 4. पेशंटची माहिती अपडेट करा (PUT)
@app.put("/patients")
def update_patient_by_id(patient_in: Patient, db: Session = Depends(get_db)):
    # आधी डेटाबेस मध्ये तो आयडी शोधा
    db_patient = db.get(Patients, patient_in.id)
    
    # जर नसेल तर नवीन तयार करा (तुमच्या लॉजिकनुसार)
    if not db_patient:
        new_patient = Patients(id=patient_in.id, name=patient_in.name, age=patient_in.age)
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)
        return new_patient

    # जर असेल तर माहिती अपडेट करा
    db_patient.name = patient_in.name
    db_patient.age = patient_in.age
    
    db.commit()
    db.refresh(db_patient)
    return db_patient

# 5. पेशंट डिलीट करा (DELETE)
@app.delete("/patients/{patient_id}")
def delete_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = db.get(Patients, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient does not exist")
        
    db.delete(patient)
    db.commit()
    return {"message": f"Patient with ID {patient_id} deleted successfully"}