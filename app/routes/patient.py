from fastapi import APIRouter,Path,Query
from app.models.patient import Patient,PatientUpdate
# from app.utils.storage import load_data,save_data
from app.services.patient_service import *


router=APIRouter(prefix="",tags=["Patients"])


@router.get("/")
def read_root():
    return {"message":"Welcome to Patient Management System"}
@router.get("/patients")
def view_all_patients():
    return get_all_patients()


@router.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(...)):
    return get_patient_by_id(patient_id)


@router.post("/create",status_code=201)
def create_new_patient(patient:Patient):
    create_patient(patient)
    return {"message":"Patient created successfully"}


@router.put("/update/{patient_id}")
def update_existing_patient(patient_id:str=Path(...),patient_update:PatientUpdate=None):
    update_patient(patient_id,patient_update)
    return {"message":"Patient updated successfully"}


@router.delete("/delete/{patient_id}")
def delete_existing_patient(patient_id:str=Path(...)):
    delete_patient(patient_id)
    return {"message":"Patient deleted successfully"}
