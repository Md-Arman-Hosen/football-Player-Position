import streamlit as st
import pandas as pd

df = pd.read_csv("fifaratings.csv")

# 1
def find_position():
    st.subheader("Find POSITION")

    name = st.text_input("Enter your name:")
    st.text("Rate yourself between 1 and 100 for the following statistics:")

    stats = [
        "Overall", "Potential", "Pace Total", "Shooting Total", "Passing Total",
        "Dribbling Total", "Defending Total", "Physicality Total", "Crossing",
        "Finishing", "Freekick Accuracy", "BallControl", "Acceleration", "Reactions",
        "Balance", "Shot Power", "Stamina", "Vision", "Penalties", "Marking",
        "Goalkeeper Diving", "Goalkeeper Handling", "GoalkeeperKicking", "Goalkeeper Reflexes"
    ]

    user_inputs = {}
    for stat in stats:
        user_inputs[stat] = st.slider(f"{stat}:", min_value=1, max_value=100, value=50)

    if st.button("Submit"):
        best_match = df.sample(1).iloc[0]
        st.subheader("Output:")
        st.text(f"Name: {name}")
        st.text(f"Position: {best_match['Best Position']}")
        st.text(f"Player's Name: {best_match['Full Name']}")
        st.text(f"Nationality: {best_match['Nationality']}")
        st.text(f"Overall: {best_match['Overall']}")
        st.text(f"Potential: {best_match['Potential']}")
        st.image(best_match['Image Link'], caption="Player Image")

# 2
def find_similar_player():
    st.subheader("Find SIMILAR PLAYER")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=150)

    positions = ["ST", "LW", "LF", "CF", "RF", "RW", "CAM", "LM", "RM", "CM", "CDM", "LWB", "RWB", "LB", "CB", "RB", "GK"]
    preferred_position = st.selectbox("Preferred Position:", positions)

    # conditions
    if preferred_position in ["ST", "LW", "LF", "CF", "RF", "RW", "CAM"]:
        stats = ["Pace Total", "Shooting Total", "Passing Total", "Dribbling Total",
                 "Physicality Total", "Crossing", "Finishing", "Freekick Accuracy", "BallControl",
                 "Acceleration", "Reactions", "Balance", "Shot Power", "Stamina", "Vision", "Penalties", "Marking"]
    elif preferred_position in ["LM", "CM", "RM", "CDM"]:
        stats = ["Pace Total", "Shooting Total", "Passing Total", "Defending Total",
                 "Physicality Total", "Crossing", "Finishing", "Freekick Accuracy", "BallControl",
                 "Acceleration", "Reactions", "Balance", "Shot Power", "Stamina", "Vision", "Penalties"]
    elif preferred_position in ["LWB", "RWB", "LB", "CB", "RB"]:
        stats = ["Pace Total", "Shooting Total", "Passing Total", "Defending Total",
                 "Physicality Total", "Finishing", "Freekick Accuracy", "BallControl",
                 "Acceleration", "Reactions", "Balance", "Shot Power", "Stamina", "Vision", "Penalties"]
    else:
        stats = ["Goalkeeper Diving", "Goalkeeper Handling", "GoalkeeperKicking", "Goalkeeper Reflexes"]

    user_inputs = {}
    for stat in stats:
        user_inputs[stat] = st.slider(f"{stat}:", min_value=1, max_value=100, value=50)

    if st.button("Submit"):
        best_match = df.sample(1).iloc[0]

        st.subheader("Output:")
        st.text(f"Name: {name}")
        st.text(f"Age: {age}")
        st.text(f"Position: {preferred_position}")
        st.text(f"Similar Player's Name: {best_match['Full Name']}")
        st.text(f"Nationality: {best_match['Nationality']}")
        st.text(f"Overall: {best_match['Overall']}")
        st.text(f"Potential: {best_match['Potential']}")
        st.image(best_match['Image Link'], caption="Player Image")

# body
st.title("WELCOME TO MANAZER")
st.text("Developed by Team-X")

# Applying style changes
st.markdown(
    """
    <style>
        .stTitle {
        text-align: center;
        font-weight: 800;
        }

        .stText {
        font-weight: 600;
        text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

option = st.radio("Choose an option:", ["Find POSITION", "Find SIMILAR PLAYER", "EXIT"])

if option == "Find POSITION":
    find_position()
elif option == "Find SIMILAR PLAYER":
    find_similar_player()
elif option == "EXIT":
    st.balloons()