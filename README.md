# ⚽ Football Player Rating Prediction

A machine learning project that predicts a football player's **Overall Rating** based on their in-game attributes using regression models.

## 📌 Project Overview

The goal of this project is to build a machine learning model capable of predicting FIFA player ratings from their individual football attributes.

The project includes:

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature selection
- Correlation analysis
- Train-test splitting
- Linear Regression
- Random Forest Regression
- Feature importance analysis
- Permutation importance
- Model evaluation
- Streamlit deployment

## 📊 Dataset

The project uses the **FIFA 22 Players dataset**, containing player information and a wide range of football attributes.

The target variable is:

- `Overall` - the player's overall rating

The final model uses detailed player attributes including:

- Crossing
- Finishing
- Heading Accuracy
- Short Passing
- Volleys
- Dribbling
- Curve
- FK Accuracy
- Long Passing
- Ball Control
- Acceleration
- Sprint Speed
- Agility
- Reactions
- Balance
- Shot Power
- Jumping
- Stamina
- Strength
- Long Shots
- Aggression
- Interceptions
- Positioning
- Vision
- Penalties
- Composure
- Marking
- Standing Tackle
- Sliding Tackle
- Goalkeeper attributes

## 🤖 Machine Learning

### Linear Regression

Linear Regression was used as a baseline model to establish a simple relationship between player attributes and their Overall Rating.

### Random Forest Regression

Random Forest Regression was used to capture more complex relationships between player attributes.

Two feature sets were explored:

- Broad player attributes
- Detailed player attributes

The **Detailed Random Forest model** was selected as the final model.

## 📈 Model Performance

The final Detailed Random Forest model achieved:

| Metric | Score |
|---|---:|
| MAE | 0.886 |
| RMSE | 1.188 |
| R² Score | 0.969 |

The model explains approximately **96.9% of the variance** in player Overall Ratings on the held-out test set.

## 🔎 Feature Importance

Permutation importance was used to identify which player attributes have the greatest influence on the model's predictions.

This helps provide insight into which attributes the model relies on most when predicting a player's Overall Rating.

## 🖥️ Streamlit Application

The trained Random Forest model is integrated into a Streamlit web application.

Users can enter a player's attributes through the application, and the model predicts the player's Overall Rating.

### 🌐 Live Demo

**Streamlit App:**  
[https://football-player-ovr-prediction.streamlit.app/](https://football-player-ovr-prediction.streamlit.app/)

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📁 Project Structure

```text
football-player-OVR-prediction/
│
├── .gitattributes
├── app.py
├── datasets/
│   └── fifa22/
│       └── players_fifa22.csv
├── player_rating_model.pkl
├── player_rating_prediction_cleaned.ipynb
├── requirements.txt
└── README.md
````

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/aryangrover7/football-player-OVR-prediction.git
```

### 2. Navigate to the project directory

```bash
cd football-player-OVR-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

## 📓 Notebook

The complete machine learning workflow, including:

* Data cleaning
* Exploratory data analysis
* Feature selection
* Model training
* Model evaluation
* Feature importance
* Permutation importance
* Visualizations

is available in:

`player_rating_prediction_cleaned.ipynb`

## 👨‍💻 Author

**Aryan Grover**


One small thing: **check the `Project Structure` section against your actual folder layout before committing**. If your CSV is directly inside `datasets/` rather than `datasets/fifa22/`, change that one line accordingly.
```
