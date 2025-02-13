import streamlit as st
from balancesheet import display_balance_sheet
from incomesheet import display_income_sheet
from calculation_ratio import display_calculation_ratio
from insights import display_insights

import json


# Navigation function
def main():
    

    # Initialize session state variables for navigation if not already set
    if "navigate_to" not in st.session_state:
        st.session_state.navigate_to = None

    # Logic for navigating via buttons (force navigation based on state)
    if st.session_state.navigate_to:
        choice = st.session_state.navigate_to
        st.session_state.navigate_to = None  # Reset navigation state to prevent infinite loop
    else:
        menu = ["Home", "Balance Sheet", "Income Sheet", "Calculation Ratio", "Insights"]
        choice = st.sidebar.selectbox("Select an option", menu)

    # Handle the content for each screen
    if choice == "Home":
        st.title("Finance App")
        st.write("### Welcome to the Finance App")
        st.write("Navigate using the sidebar to manage financial data and calculate ratios.")

    elif choice == "Balance Sheet":
        st.write("### Balance Sheet")
        df_balance = display_balance_sheet()
        if df_balance is not None:
            st.session_state.df_balance = df_balance




    elif choice == "Income Sheet":
        st.write("### Income Sheet")
        df_income = display_income_sheet()
        if df_income is not None:
            st.session_state.df_income = df_income


    elif choice == "Calculation Ratio":
        display_calculation_ratio()
    elif choice == "Insights":
        display_insights()
def save_data_to_json():
    data = {}

    # Saving Balance Sheet Data
    if "df_balance" in st.session_state:
        data["balance_sheet"] = {
            "shareholder_data": st.session_state.df_balance["2024"].tolist(),
            "non_current_liabilities": st.session_state.df_balance["2023"].tolist(),
        }

    # Saving Income Sheet Data
    if "df_income" in st.session_state:
        data["income_sheet"] = {
            "2024": st.session_state.df_income["2024"].tolist(),
            "2023": st.session_state.df_income["2023"].tolist(),
        }

    # Save all data to a JSON file
    with open(r"D:\Finance_App\financial_data.json", "w") as f:
        json.dump(data, f, indent=4)

    st.success("Data saved successfully to JSON.")

if __name__ == "__main__":
    main()
