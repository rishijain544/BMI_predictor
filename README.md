# 🏥 BMI Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-ML%20Model-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  A machine learning web application that predicts <strong>Body Mass Index (BMI)</strong> based on demographic and insurance data — powered by Multiple Linear Regression and served via a Flask backend.
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Demo](#-demo)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [BMI Categories](#-bmi-categories)
- [Dataset](#-dataset)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🧠 Overview

The **BMI Predictor** is an end-to-end machine learning project that:

1. Trains a **Multiple Linear Regression** model on real-world insurance data
2. Predicts a user's BMI from inputs like age, sex, number of children, and insurance charges
3. Classifies the result into standard WHO BMI categories (Underweight, Normal, Overweight, Obesity)
4. Serves predictions through an interactive **Flask web application**

This project demonstrates the complete ML lifecycle — from data preprocessing and model training to model serialization and web deployment.

---

## 🎬 Demo

> Run locally and visit `http://127.0.0.1:5000` in your browser.

Fill in the form with:
- Age
- Sex
- Number of children
- Insurance charges

Hit **Predict** and get an instant BMI estimate along with your health category.

---

## ✨ Features

- 🔢 **Multiple Linear Regression** model trained on insurance dataset
- 🧬 Input features: `age`, `sex`, `children`, `charges`
- 📊 BMI output with WHO-standard health classification
- 🌐 Lightweight Flask web interface
- 💾 Pre-trained model saved as `model.pkl` using Pickle — no retraining needed on startup
- 📁 Clean project structure with separate training and serving scripts

---

## ⚙️ How It Works

```
User Input (Web Form)
        │
        ▼
  Flask Backend (app.py)
        │
        ├── Encodes categorical features (sex: male=1, female=0)
        ├── Constructs feature array: [age, children, charges, sex]
        │
        ▼
  Pretrained MLR Model (model.pkl)
        │
        ▼
  Predicted BMI Value
        │
        ▼
  BMI Category Classification
  (Underweight / Normal / Overweight / Obesity)
        │
        ▼
  Result Rendered on Web Page
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | Flask |
| ML Library | scikit-learn |
| Data Processing | pandas, NumPy |
| Model Persistence | Pickle |
| Frontend | HTML, CSS |
| Dataset | insurance.csv |

---

## 📁 Project Structure

```
BMI_predictor/
│
├── app.py                  # Flask app — handles routes and prediction logic
├── train_model.py          # Script to train and save the ML model
├── model.pkl               # Serialized trained Linear Regression model
├── insurance.csv           # Dataset used for training
├── requirements.txt        # Python dependencies
├── .python-version         # Python version specifier
│
├── templates/
│   └── index.html          # Main web page (form + result display)
│
├── static/
│   └── (CSS/JS assets)     # Styling and frontend resources
│
└── api/
    └── (API handlers)      # API-related utilities
```

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/rishijain544/BMI_predictor.git
cd BMI_predictor
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Retrain the model

The repository already includes a pre-trained `model.pkl`. If you want to retrain from scratch:

```bash
python train_model.py
```

This will output:
```
Model Saved Successfully
```

### 5. Run the Flask application

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 💻 Usage

1. Open the web app in your browser
2. Enter the following details:
   - **Age** — your age in years
   - **Sex** — male or female
   - **Children** — number of dependents covered by insurance
   - **Charges** — annual insurance charges (in USD)
3. Click the **Predict** button
4. Your predicted BMI and health category will be displayed on the screen

---

## 📐 Model Details

| Parameter | Value |
|---|---|
| Algorithm | Multiple Linear Regression |
| Library | `sklearn.linear_model.LinearRegression` |
| Input Features | `age`, `children`, `charges`, `sex` |
| Target Variable | `bmi` |
| Train/Test Split | 80% / 20% |
| Random State | 42 |
| Encoding | `sex`: male → 1, female → 0 |
| Model File | `model.pkl` (Pickle serialization) |

### Training Script Summary (`train_model.py`)

```python
X = df[['age', 'children', 'charges', 'sex']]
y = df['bmi']

model = LinearRegression()
model.fit(X_train, y_train)
pickle.dump(model, open("model.pkl", "wb"))
```

---

## 📊 BMI Categories

The app classifies predicted BMI using standard WHO thresholds:

| BMI Range | Category |
|---|---|
| < 18.5 | 🔵 Underweight |
| 18.5 – 24.9 | 🟢 Normal |
| 25.0 – 29.9 | 🟡 Overweight |
| ≥ 30.0 | 🔴 Obesity |

---

## 📦 Dataset

The model is trained on the publicly available **Medical Cost Personal Dataset** (`insurance.csv`), which contains:

| Column | Description |
|---|---|
| `age` | Age of the primary beneficiary |
| `sex` | Gender of the beneficiary (male/female) |
| `bmi` | Body mass index (target variable) |
| `children` | Number of dependents covered |
| `smoker` | Smoking status |
| `region` | US residential region |
| `charges` | Individual medical insurance costs |

> Only `age`, `sex`, `children`, and `charges` are used as features; `bmi` is the prediction target.

---

## 🔮 Future Improvements

- [ ] Add model evaluation metrics (R², MAE, RMSE) to the README and UI
- [ ] Include additional features like `smoker` and `region` for better accuracy
- [ ] Try advanced models: Ridge Regression, Random Forest, XGBoost
- [ ] Add input validation and error handling on the frontend
- [ ] Deploy to a cloud platform (Render, Railway, or AWS EC2)
- [ ] Add data visualization (correlation heatmap, feature importance chart)
- [ ] Build a REST API endpoint for programmatic access

---

## 👤 Author

**Rishi Jain**

- GitHub: [@rishijain544](https://github.com/rishijain544)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ using Python & Flask
</p>
