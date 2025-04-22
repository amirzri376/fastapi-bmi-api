from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BMIRequest(BaseModel):
    weight: float  # in kilograms
    height: float  # in meters


@app.post("/bmi")
def calculate_bmi(data: BMIRequest):
    weight = data.weight
    height = data.height
    bmi = weight / (height**2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {"BMI": round(bmi, 2), "Category": category}