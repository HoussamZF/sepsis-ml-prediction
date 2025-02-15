import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np
import xgboost as xgb

app = FastAPI()

# Get absolute path to model file
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Load the XGBoost model using xgb.Booster
model = xgb.Booster(model_file=model_path)

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory='static'), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    Plasma_glucose = data.get('Plasma_glucose')
    Blood_Work_R1 = data.get('Blood_Work_R1')
    Blood_Pressure = data.get('Blood_Pressure')
    Blood_Work_R3 = data.get('Blood_Work_R3')
    BMI = data.get('BMI')
    Blood_Work_R4 = data.get('Blood_Work_R4')
    Patient_age = data.get('Patient_age')

    # Prepare the input data
    input_data = np.array([[Plasma_glucose, Blood_Work_R1, Blood_Pressure, Blood_Work_R3, BMI, Blood_Work_R4, Patient_age$
    input_data = input_data.astype(np.float32)  # Adjust dtype if necessary

    # Make prediction
    dmatrix = xgb.DMatrix(input_data)
    prediction = model.predict(dmatrix)

    # Convert numpy data types to standard Python data types
    prediction = prediction[0].item()

    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
