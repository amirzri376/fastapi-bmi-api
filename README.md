🧮 FastAPI BMI Calculator
This project is a simple API built with FastAPI that calculates Body Mass Index (BMI) based on a person's weight and height. It demonstrates how to build and run a web API with FastAPI and return meaningful JSON responses.

🚀 Features
Accepts weight and height as input

Calculates BMI and returns a health category

Lightweight and fast with automatic documentation at /docs

▶️ Example Usage
POST /bmi

Send a POST request to this route with the following JSON:
{
  "weight": 75,
  "height": 1.75
}
Response:
{
  "BMI": 24.49,
  "Category": "Normal"
}

🛠 How to Run Locally
Install dependencies:
pip install fastapi uvicorn
Run the app:
uvicorn main:app --reload

Open your browser:

API root: http://127.0.0.1:8000

Interactive docs: http://127.0.0.1:8000/docs

🧰 Tech Stack
Python 3.9+

FastAPI

Uvicorn

📄 License
Free to use and modify.
