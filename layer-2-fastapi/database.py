from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///patients.db", echo=True)

class Base(DeclarativeBase):
    pass

class Patients(Base):
    __tablename__ = "patients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column()


Base.metadata.create_all(engine)


def patients_creation(patients):
    patient = Patients(name=patients.name, age=patients.age)
    with Session(engine) as session:
        session.add(patient)
        session.commit()
        session.refresh(patient)   # database कडून ताजी माहिती (id सह) परत आण
        return patient.id          # नवीन id परत दे

def patient_query(id=None):
    with Session(engine) as session:
        if not id:
            return session.query(Patients).all()
        else:
            return session.get(Patients, id)

def delete_patient(patient):
    with Session(engine) as session:
        session.delete(patient)
        session.commit()

def put_patient(patient):
    with Session(engine) as session:
        patientobj = session.get(Patients, patient.id)
        if not patientobj:
            return patients_creation(patient)

        patientobj.age = patient.age
        patientobj.name = patient.name

        session.commit()