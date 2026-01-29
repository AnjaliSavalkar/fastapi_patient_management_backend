from pydantic import BaseModel, Field, computed_field
from typing import Optional,Annotated,Literal

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="unique patient identifier",examples=["P001"])]
    name:str
    city:str
    age:Annotated[int,Field(...,gt=0,lt=120,)]
    gender:Literal['Male','Female','Other']
    height:Annotated[float,Field(...,gt=0,lt=3,description="height in meters")]
    weight:Annotated[float,Field(...,gt=0,lt=500,description="weight in kgs")]



    @computed_field
    @property
    def bmi(self)-> float:
        return round(self.weight/(self.height**2),2)
    
    @computed_field
    @property   
    def health_risk(self)-> str:
        bmi_value=self.bmi
        if bmi_value<18.5:
            return "Underweight"
        elif 18.5<=bmi_value<24.9:
            return "Normal weight"
        elif 25<=bmi_value<29.9:
            return "Overweight"
        else:
            return "Obesity"
        




class PatientUpdate(BaseModel):
    name:Optional[str]
    city:Optional[str]
    age:Optional[Annotated[int,Field(gt=0,lt=120)]]
    gender:Optional[Literal['Male','Female','Other']]
    height:Optional[Annotated[float,Field(gt=0,lt=3,description="height in meters")]]
    weight:Optional[Annotated[float,Field(gt=0,lt=500,description="weight in kgs")]]