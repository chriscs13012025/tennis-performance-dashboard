import streamlit as st
import pandas as pd
import json


import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data.json")


def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


if "match_history" not in st.session_state:
    st.session_state["match_history"] = load_data().get("match_history", [])

if "weights" not in st.session_state:
    st.session_state["weights"] = load_data().get("weights", [183, 181, 179, 177])  # Default weight data


st.title("Tennis Performance Dashboard 🎾")
st.write("Analyze your match history, training progress, and weight trends dynamically.")


st.sidebar.header("Data Inputs")


st.sidebar.subheader("Add Match Results")
opponent = st.sidebar.text_input("Opponent Name")
result = st.sidebar.selectbox("Match Result", ["Win", "Loss"])
score = st.sidebar.text_input("Score (e.g., 6-3, 7-5)")
match_date = st.sidebar.date_input("Match Date")

if st.sidebar.button("Add Match"):
    if opponent and score:
        new_match = {
            "opponent": opponent,
            "result": result,
            "score": score,
            "date": str(match_date)
        }
        st.session_state["match_history"].append(new_match)
        save_data({"match_history": st.session_state["match_history"], "weights": st.session_state["weights"]})
        st.success(f"Match against {opponent} added!")


st.subheader("Match History")
if st.session_state["match_history"]:
    match_df = pd.DataFrame(st.session_state["match_history"])
    st.dataframe(match_df)

    
    win_count = sum(1 for match in st.session_state["match_history"] if match["result"] == "Win")
    loss_count = len(st.session_state["match_history"]) - win_count

    st.subheader("Win/Loss Record")
    st.bar_chart({"Wins": [win_count], "Losses": [loss_count]})  


st.subheader("Weight Progress")


new_weight = st.number_input("Enter your latest weight (lbs)", min_value=160, max_value=200, step=1)
if st.button("Update Weight"):
    st.session_state["weights"].append(new_weight)
    save_data({"match_history": st.session_state["match_history"], "weights": st.session_state["weights"]})
    st.success(f"Weight updated to {new_weight} lbs")


st.line_chart(st.session_state["weights"])


st.subheader("Training Hours Per Week")
training_hours = [8, 10, 12, 15, 18]  
selected_week = st.slider("Select Week", min_value=1, max_value=len(training_hours), step=1)
st.write(f"Week {selected_week}: {training_hours[selected_week - 1]} hours")
st.bar_chart(training_hours)  

st.write("This dashboard allows you to analyze performance trends over time!")
