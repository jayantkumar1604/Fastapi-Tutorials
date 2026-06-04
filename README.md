# 🏥 Insurance Premium Category Predictor

A Machine Learning-powered web application that predicts an insurance premium category based on a user's age, BMI, income, lifestyle, occupation, and city tier.

The project consists of:

* ⚡ FastAPI Backend
* 🎨 Streamlit Frontend
* 🤖 Machine Learning Model
* 📊 Automatic Feature Engineering

---

## 🚀 Features

* Insurance premium category prediction
* Automatic BMI calculation
* Lifestyle risk assessment
* Age group classification
* City tier mapping
* FastAPI REST API
* Interactive Streamlit UI
* Input validation using Pydantic
* Real-time prediction results

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Pydantic
* Pandas
* Scikit-learn
* Pickle

### Frontend

* Streamlit
* Requests

### Machine Learning

* Python
* Scikit-learn

---

## 📂 Project Structure

```text
Insurance-Premium-Predictor/
│
├── main.py                 # FastAPI backend
├── app.py                  # Streamlit frontend
├── model.pkl               # Trained ML model
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/jayantkumar1604/Fastapi-Tutorials.git
cd Fastapi-Tutorials
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Backend

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## ▶️ Run the Frontend

Start Streamlit:

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 🔍 Prediction API

### Endpoint

```http
POST /predict
```

### Sample Request

```json
{
  "age": 30,
  "weight": 75,
  "height": 1.75,
  "income_lpa": 12,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Sample Response

```json
{
  "predicted_category": "Medium"
}
```

---

## 🧮 Feature Engineering

The application automatically generates the following features:

### BMI

```text
BMI = Weight / Height²
```

### Lifestyle Risk

| Condition          | Risk   |
| ------------------ | ------ |
| Smoker + BMI > 30  | High   |
| Smoker OR BMI > 27 | Medium |
| Otherwise          | Low    |

### Age Groups

| Age     | Group       |
| ------- | ----------- |
| < 25    | Young       |
| 25 - 44 | Adult       |
| 45 - 59 | Middle Aged |
| 60+     | Senior      |

### City Tiers

| Tier   | Cities                                                      |
| ------ | ----------------------------------------------------------- |
| Tier 1 | Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune |
| Tier 2 | Jaipur, Lucknow, Patna, Ranchi, Noida, etc.                 |
| Tier 3 | Other Cities                                                |

---

## 📸 Application Workflow

```text
User Input
    ↓
Feature Engineering
    ↓
FastAPI Backend
    ↓
Machine Learning Model
    ↓
Prediction
    ↓
Streamlit UI Display
```

---

## 🎯 Future Improvements

* Deploy FastAPI using Render/Railway
* Deploy Streamlit on Streamlit Cloud
* Add premium amount prediction
* Add model monitoring
* Docker support
* Authentication and user history

---

## 👨‍💻 Author

Jayant Kumar

GitHub: https://github.com/jayantkumar1604

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
