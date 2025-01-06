import streamlit as st
import json

# Function to save user input data to JSON
def save_data_to_json():
    data = {
        "total_non_current_2023": st.session_state.get("total_non_current_2023", 0),
        "total_shareholder_2023": st.session_state.get("total_shareholder_2023", 0),
        "total_non_current_2024": st.session_state.get("total_non_current_2024", 0),
        "total_shareholder_2024": st.session_state.get("total_shareholder_2024", 0),
        "revenue_2023": st.session_state.get("revenue_2023", 0),
        "revenue_2024": st.session_state.get("revenue_2024", 0),
        "profit_before_tax_2023": st.session_state.get("profit_before_tax_2023", 0),
        "profit_before_tax_2024": st.session_state.get("profit_before_tax_2024", 0),
        "total_current_assets_2023": st.session_state.get("total_current_assets_2023", 0),
        "total_current_assets_2024": st.session_state.get("total_current_assets_2024", 0),
        "total_current_liabilities_2023": st.session_state.get("total_current_liabilities_2023", 0),
        "total_current_liabilities_2024": st.session_state.get("total_current_liabilities_2024", 0),
        "inventories_2023": st.session_state.get("inventories_2023", 0),
        "inventories_2024": st.session_state.get("inventories_2024", 0),
    }

    # Save data to a JSON file
    with open(r"D:\Finance_App\finance_data.json", "w") as f:
        json.dump(data, f, indent=4)

    st.success("Data saved successfully to JSON.")

# Example button to save data
if st.button("Save Data to JSON"):
    save_data_to_json()
