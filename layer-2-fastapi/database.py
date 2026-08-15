from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer
from sqlalchemy import create_engine

engine = create_engine("sqlite:///patients.db", echo=True)

class Base(DeclarativeBase):
    pass

class Patients(Base):
    __tablename__ = "patients"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column()


Base.metadata.create_all(engine)


