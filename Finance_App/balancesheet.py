import streamlit as st
import pandas as pd
import json

# Function to save data to JSON
def save_data_to_json():
    data = {
        "total_non_current_2023": st.session_state.get("total_non_current_2023", 0),
        "total_shareholder_2023": st.session_state.get("total_shareholder_2023", 0),
        "total_non_current_2024": st.session_state.get("total_non_current_2024", 0),
        "total_shareholder_2024": st.session_state.get("total_shareholder_2024", 0),
        "total_current_assets_2023": st.session_state.get("total_current_assets_2023", 0),
        "total_current_assets_2024": st.session_state.get("total_current_assets_2024", 0),
        "total_current_liabilities_2023": st.session_state.get("total_current_liabilities_2023", 0),
        "total_current_liabilities_2024": st.session_state.get("total_current_liabilities_2023", 0),
        "inventories_2023": st.session_state.get("inventories_2023", 0),
        "inventories_2024": st.session_state.get("inventories_2024", 0),
        "total_assets_2023": st.session_state.get("total_assets_2023", 0),
        "total_assets_2024": st.session_state.get("total_assets_2024", 0)
    }

    # Save data to a JSON file
    with open(r"D:\Finance_App\finance_data.json", "w") as f:
        json.dump(data, f, indent=4)

def display_balance_sheet():
    # Initializing session state if not present
    if "balance_sheet" not in st.session_state:
        # Initial data setup
        st.session_state.shareholder_data = pd.DataFrame({
            'PARTICULARS in cr': ['Equity Share Capital', 'Reserves and Surplus'],
            '2024': [None] * 2,
            '2023': [None] * 2
        })
        st.session_state.non_current_liabilities = pd.DataFrame({
            'PARTICULARS in cr': ['Long Term Borrowings', 'Deferred Tax Liabilities [Net]',
                                  'Other Long Term Liabilities', 'Long Term Provisions'],
            '2024': [None] * 4,
            '2023': [None] * 4
        })
        st.session_state.current_liabilities = pd.DataFrame({
            'PARTICULARS in cr': ['Short Term Borrowings', 'Trade Payables',
                                  'Other Current Liabilities', 'Short Term Provisions'],
            '2024': [None] * 4,
            '2023': [None] * 4
        })
        st.session_state.current_assets = pd.DataFrame({
            'PARTICULARS in cr': ['Current Investments', 'Inventories', 'Trade Receivables',
                                  'Cash And Cash Equivalents', 'Short Term Loans And Advances', 'Other Current Assets'],
            '2024': [None] * 6,
            '2023': [None] * 6
        })
        st.session_state.fixed_assets = pd.DataFrame({
            'PARTICULARS in cr': ['Tangible Assets', 'Intangible Assets', 'Capital Work-In-Progress',
                                  'Non-Current Investments', 'Deferred Tax Assets [Net]',
                                  'Long Term Loans And Advances', 'Other Non-Current Assets'],
            '2024': [None] * 7,
            '2023': [None] * 7
        })

    # Helper to calculate totals
    def calculate_totals(df, year):
        return sum(float(x) for x in df[year] if x is not None and str(x).replace('.', '', 1).isdigit())

    # Layout with expanders
    st.title("Balance Sheet Application")
    st.divider()


    # Shareholder's Funds
    with st.expander("Shareholder's Funds", expanded=True):
        st.subheader("Shareholder's Funds")
        shareholder_df = st.data_editor(st.session_state.shareholder_data, key="shareholders_funds_editor", use_container_width=True)
        total_shareholder_2024 = calculate_totals(shareholder_df, "2024")
        total_shareholder_2023 = calculate_totals(shareholder_df, "2023")
        st.metric("Total Shareholder's Funds (2024)", f"₹{total_shareholder_2024}")
        st.metric("Total Shareholder's Funds (2023)", f"₹{total_shareholder_2023}")

    st.divider()

    # Non-Current Liabilities
    with st.expander("Non-Current Liabilities", expanded=False):
        st.subheader("Non-Current Liabilities")
        non_current_df = st.data_editor(st.session_state.non_current_liabilities, key="non_current_liabilities_editor", use_container_width=True)
        total_non_current_2024 = calculate_totals(non_current_df, "2024")
        total_non_current_2023 = calculate_totals(non_current_df, "2023")
        st.metric("Total Non-Current Liabilities (2024)", f"₹{total_non_current_2024}")
        st.metric("Total Non-Current Liabilities (2023)", f"₹{total_non_current_2023}")

    st.divider()

    # Current Liabilities
    with st.expander("Current Liabilities", expanded=False):
        st.subheader("Current Liabilities")
        current_liabilities_df = st.data_editor(st.session_state.current_liabilities, key="current_liabilities_editor", use_container_width=True)
        total_current_liabilities_2024 = calculate_totals(current_liabilities_df, "2024")
        total_current_liabilities_2023 = calculate_totals(current_liabilities_df, "2023")
        st.metric("Total Current Liabilities (2024)", f"₹{total_current_liabilities_2024}")
        st.metric("Total Current Liabilities (2023)", f"₹{total_current_liabilities_2023}")

    st.divider()

    # Current Assets
    with st.expander("Current Assets", expanded=False):
        st.subheader("Current Assets")
        current_assets_df = st.data_editor(st.session_state.current_assets, key="current_assets_editor", use_container_width=True)
        total_current_assets_2024 = calculate_totals(current_assets_df, "2024")
        total_current_assets_2023 = calculate_totals(current_assets_df, "2023")
        st.metric("Total Current Assets (2024)", f"₹{total_current_assets_2024}")
        st.metric("Total Current Assets (2023)", f"₹{total_current_assets_2023}")

    st.divider()

    # Fixed Assets
    with st.expander("Fixed Assets", expanded=False):
        st.subheader("Fixed Assets")
        fixed_assets_df = st.data_editor(st.session_state.fixed_assets, key="fixed_assets_editor", use_container_width=True)
        total_fixed_assets_2024 = calculate_totals(fixed_assets_df, "2024")
        total_fixed_assets_2023 = calculate_totals(fixed_assets_df, "2023")
        st.metric("Total Fixed Assets (2024)", f"₹{total_fixed_assets_2024}")
        st.metric("Total Fixed Assets (2023)", f"₹{total_fixed_assets_2023}")

    st.divider()

    # Total Assets and Liabilities
    total_assets_2024 = total_current_assets_2024 + total_fixed_assets_2024
    total_assets_2023 = total_current_assets_2023 + total_fixed_assets_2023
    st.metric("Total Assets (2024)", f"₹{total_assets_2024}")
    st.metric("Total Assets (2023)", f"₹{total_assets_2023}")

    total_liabilities_2024 = total_shareholder_2024 + total_non_current_2024 + total_current_liabilities_2024
    total_liabilities_2023 = total_shareholder_2023 + total_non_current_2023 + total_current_liabilities_2023
    st.metric("Total Liabilities (2024)", f"₹{total_liabilities_2024}")
    st.metric("Total Liabilities (2023)", f"₹{total_liabilities_2023}")
        # Extracting Inventories values from the DataFrame
    inventories_2023_row = current_assets_df[current_assets_df["PARTICULARS in cr"] == 'Inventories']
    inventories_2024_row = current_assets_df[current_assets_df["PARTICULARS in cr"] == 'Inventories']
        
    inventories_2023 = inventories_2023_row["2023"].iloc[0] if not inventories_2023_row.empty else None
    inventories_2023 = int(inventories_2023) if inventories_2023 is not None else 0

    inventories_2024 = inventories_2024_row["2024"].iloc[0] if not inventories_2024_row.empty else None
    inventories_2024 = int(inventories_2024) if inventories_2024 is not None else 0







    st.divider()

    if st.button("Save Balance Sheet Data"):
        # Saving the current DataFrames to session state
        st.session_state.shareholder_data = shareholder_df
        st.session_state.non_current_liabilities = non_current_df
        st.session_state.current_liabilities = current_liabilities_df
        st.session_state.current_assets = current_assets_df
        st.session_state.fixed_assets = fixed_assets_df



        # Saving the totals to session state
        st.session_state.total_non_current_2023 = total_non_current_2023
        st.session_state.total_shareholder_2023 = total_shareholder_2023
        st.session_state.total_non_current_2024 = total_non_current_2024
        st.session_state.total_shareholder_2024 = total_shareholder_2024
        st.session_state.total_current_assets_2023 = total_current_assets_2023
        st.session_state.total_current_assets_2024 = total_current_assets_2024
        st.session_state.total_current_liabilities_2023 = total_current_liabilities_2023
        st.session_state.total_current_liabilities_2024 = total_current_liabilities_2024
        st.session_state.inventories_2023 = inventories_2023
        st.session_state.inventories_2024 = inventories_2024
        st.session_state.total_assets_2023 = total_assets_2023
        st.session_state.total_assets_2024 = total_assets_2024
        st.success("Balance Sheet data saved successfully!")
        # Save data to JSON
        save_data_to_json()

    return st.session_state.shareholder_data
