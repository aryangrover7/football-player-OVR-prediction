import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Football Player Rating Predictor",
    page_icon="⚽",
    layout="centered"
)


# -----------------------------
# Load Model
# -----------------------------

model = joblib.load("player_rating_model.pkl")


# -----------------------------
# Title
# -----------------------------

st.title("⚽ Football Player Rating Predictor")

st.write(
    "Enter a player's attributes to predict their FIFA/EA FC Overall rating."
)


# -----------------------------
# Player Attributes
# -----------------------------

st.subheader("Player Attributes")


col1, col2 = st.columns(2)


with col1:
    Crossing = st.slider("Crossing", 0, 100, 50)
    Finishing = st.slider("Finishing", 0, 100, 50)
    HeadingAccuracy = st.slider("Heading Accuracy", 0, 100, 50)
    ShortPassing = st.slider("Short Passing", 0, 100, 50)
    Volleys = st.slider("Volleys", 0, 100, 50)
    Dribbling = st.slider("Dribbling", 0, 100, 50)
    Curve = st.slider("Curve", 0, 100, 50)
    FKAccuracy = st.slider("Free Kick Accuracy", 0, 100, 50)
    LongPassing = st.slider("Long Passing", 0, 100, 50)
    BallControl = st.slider("Ball Control", 0, 100, 50)
    Acceleration = st.slider("Acceleration", 0, 100, 50)
    SprintSpeed = st.slider("Sprint Speed", 0, 100, 50)
    Agility = st.slider("Agility", 0, 100, 50)
    Reactions = st.slider("Reactions", 0, 100, 50)
    Balance = st.slider("Balance", 0, 100, 50)
    ShotPower = st.slider("Shot Power", 0, 100, 50)
    Jumping = st.slider("Jumping", 0, 100, 50)


with col2:
    Stamina = st.slider("Stamina", 0, 100, 50)
    Strength = st.slider("Strength", 0, 100, 50)
    LongShots = st.slider("Long Shots", 0, 100, 50)
    Aggression = st.slider("Aggression", 0, 100, 50)
    Interceptions = st.slider("Interceptions", 0, 100, 50)
    Positioning = st.slider("Positioning", 0, 100, 50)
    Vision = st.slider("Vision", 0, 100, 50)
    Penalties = st.slider("Penalties", 0, 100, 50)
    Composure = st.slider("Composure", 0, 100, 50)
    Marking = st.slider("Marking", 0, 100, 50)
    StandingTackle = st.slider("Standing Tackle", 0, 100, 50)
    SlidingTackle = st.slider("Sliding Tackle", 0, 100, 50)
    GKDiving = st.slider("GK Diving", 0, 100, 50)
    GKHandling = st.slider("GK Handling", 0, 100, 50)
    GKKicking = st.slider("GK Kicking", 0, 100, 50)
    GKPositioning = st.slider("GK Positioning", 0, 100, 50)
    GKReflexes = st.slider("GK Reflexes", 0, 100, 50)


# -----------------------------
# Create Input DataFrame
# -----------------------------

input_data = pd.DataFrame([{
    "Crossing": Crossing,
    "Finishing": Finishing,
    "HeadingAccuracy": HeadingAccuracy,
    "ShortPassing": ShortPassing,
    "Volleys": Volleys,
    "Dribbling": Dribbling,
    "Curve": Curve,
    "FKAccuracy": FKAccuracy,
    "LongPassing": LongPassing,
    "BallControl": BallControl,
    "Acceleration": Acceleration,
    "SprintSpeed": SprintSpeed,
    "Agility": Agility,
    "Reactions": Reactions,
    "Balance": Balance,
    "ShotPower": ShotPower,
    "Jumping": Jumping,
    "Stamina": Stamina,
    "Strength": Strength,
    "LongShots": LongShots,
    "Aggression": Aggression,
    "Interceptions": Interceptions,
    "Positioning": Positioning,
    "Vision": Vision,
    "Penalties": Penalties,
    "Composure": Composure,
    "Marking": Marking,
    "StandingTackle": StandingTackle,
    "SlidingTackle": SlidingTackle,
    "GKDiving": GKDiving,
    "GKHandling": GKHandling,
    "GKKicking": GKKicking,
    "GKPositioning": GKPositioning,
    "GKReflexes": GKReflexes
}])


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Overall Rating"):

    prediction = model.predict(input_data)[0]

    prediction = round(prediction, 1)

    st.success(f"Predicted Overall Rating: **{prediction}**")

    st.metric(
        label="Predicted Overall",
        value=prediction
    )