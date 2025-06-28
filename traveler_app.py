import streamlit as st

st.title("Travel Cost Estimator")

#  User inputs (replacing input())
travelers = st.number_input("How many travelers are you?", min_value=1, step=1)
destination = st.selectbox("Where is your destination?", ["City", "Town", "Village"])
days = st.number_input("How many days will you be here for?", min_value=1, step=1)

#  Your original logic wrapped inside a function
def total_cost(travelers, destination, days):
    if destination == "City":
        cost = 5000
    elif destination == "Town":
        cost = 3000
    elif destination == "Village":
        cost = 1500
    else:
        st.error("We don't travel to that destination.")
        return 0
    
    total = travelers * days * cost
    return total

#  Button to calculate cost
if st.button("Estimate Cost"):
    final_cost = total_cost(travelers, destination, days)
    st.success(f"Total Cost is: {final_cost:,} KES")
