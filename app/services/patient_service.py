from fastapi import HTTPException
from app.models.patient import Patient, PatientUpdate
from app.utils.storage import load_data, save_data




def get_all_patients():
    return load_data()


def get_patient_by_id(patient_id:str):
    data=load_data()
    if patient_id  not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    return data[patient_id]
def create_patient(patient:Patient):
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient with this ID already exists")
    data[patient.id]=patient.model_dump(exclude=['id'])
    save_data(data)




def update_patient(patient_id:str,patient_update:PatientUpdate):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    existing_patient_data=data[patient_id]
    updated_data=patient_update.model_dump(exclude_unset=True)
    existing_patient_data.update(updated_data)
    save_data(data)

def delete_patient(patient_id:str):
    data=load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    del data[patient_id]
    save_data(data)