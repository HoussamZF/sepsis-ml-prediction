# ML Sepsis Prediction

This repository contains a machine learning project for predicting sepsis using patient data. The project utilizes XGBoost for making predictions and is deployed using FastAPI for serving a web-based interface.

## Project Structure

- **app**: Directory containing the FastAPI application files.
  - `main.py`: The main application file that sets up the FastAPI server, loads the trained model, and handles prediction requests.
  - `templates`: Directory containing HTML templates for the web interface.
  - `static`: Directory for static files (css).

- **ML Sepsis Prediction - Notebook.ipynb**: Jupyter notebook used for data exploration, feature engineering, model training, and evaluation.

- **requirements.txt**: List of dependencies required to run the project.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HoussamZF/ml-sepsis-prediction.git
    cd ml-sepsis-prediction
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```

4. Open your browser and go to `http://127.0.0.1:8000` to access the web interface.

## Usage

1. Fill in the form with the patient's data:
    - Plasma Glucose
    - Blood Work R1
    - Blood Pressure
    - Blood Work R3
    - BMI
    - Blood Work R4
    - Patient Age

2. Click on the "Predict" button to get the prediction result.

3. The prediction result will display whether the prediction is positive or negative, along with the probability.

## File Descriptions

- **main.py**: The FastAPI application file that handles incoming requests, loads the model, and returns prediction results.
- **index.html**: HTML template for the web interface where users can input patient data and get predictions.

## License

This project is licensed under the MIT License.
