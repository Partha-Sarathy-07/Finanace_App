import streamlit as st
import pandas as pd
import json

# Function to save data to JSON

import streamlit as st
import json

def save_data_to_json():
    # Function to convert any non-serializable objects (like numpy.int64) to serializable ones
    def convert_to_serializable(obj):
        if isinstance(obj, (int, float, str, bool)):
            return obj
        elif isinstance(obj, (pd.Series, pd.DataFrame)):
            return obj.to_dict()
        elif hasattr(obj, 'tolist'):  # Convert numpy arrays or similar objects
            return obj.tolist()
        else:
            raise TypeError(f"Type {type(obj)} not serializable")

    # Create a dictionary of session state data to be saved
    data = {
        "total_income_2023": convert_to_serializable(st.session_state.get("total_income_2023", 0)),
        "total_income_2024": convert_to_serializable(st.session_state.get("total_income_2024", 0)),
        "total_expenses_2023": convert_to_serializable(st.session_state.get("total_expenses_2023", 0)),
        "total_expenses_2024": convert_to_serializable(st.session_state.get("total_expenses_2024", 0)),
        "total_tax_2023": convert_to_serializable(st.session_state.get("total_tax_2023", 0)),
        "total_tax_2024": convert_to_serializable(st.session_state.get("total_tax_2024", 0)),
        "profit_before_tax_2023": convert_to_serializable(st.session_state.get("profit_before_tax_2023", 0)),
        "profit_before_tax_2024": convert_to_serializable(st.session_state.get("profit_before_tax_2024", 0)),
        "profit_after_tax_2023": convert_to_serializable(st.session_state.get("profit_after_tax_2023", 0)),
        "profit_after_tax_2024": convert_to_serializable(st.session_state.get("profit_after_tax_2024", 0)),
        "revenue_from_operations_2023": convert_to_serializable(st.session_state.get("revenue_from_operations_2023", 0)),
        "revenue_from_operations_2024": convert_to_serializable(st.session_state.get("revenue_from_operations_2024", 0)),
        "other_income_2023": convert_to_serializable(st.session_state.get("other_income_2023", 0)),
        "other_income_2024": convert_to_serializable(st.session_state.get("other_income_2024", 0)),
        "finance_costs_2023": convert_to_serializable(st.session_state.get("finance_costs_2023", 0)),
        "finance_costs_2024": convert_to_serializable(st.session_state.get("finance_costs_2024", 0)),
        "depreciation_expenses_2023": convert_to_serializable(st.session_state.get("depreciation_expenses_2023", 0)),
        "depreciation_expenses_2024": convert_to_serializable(st.session_state.get("depreciation_expenses_2024", 0))
    }

    # Save the serialized data to a JSON file
    with open(r"D:\Finance_App\income_data.json", "w") as f:
        json.dump(data, f, indent=4)



def display_income_sheet():
    # Initialize session state for income and expense tables
    if "income_data" not in st.session_state:
        st.session_state.income_data = pd.DataFrame({
            "Particulars (In cr)": ["Revenue from operations", "Other income"],
            "2024": [None, None],
            "2023": [None, None],
        })

        st.session_state.expense_data = pd.DataFrame({
            "Particulars (In cr)": [
                "Cost of materials consumed",
                "Purchases of stock-in-trade",
                "Change in inventories",
                "Employee benefits expense",
                "Finance costs",
                "Depreciation and amortisation expenses",
                "Other expenses",
                "Vehicles/dies for own use",
            ],
            "2024": [None] * 8,
            "2023": [None] * 8,
        })

        st.session_state.tax_data = pd.DataFrame({
            "Particulars (In cr)": ["Current tax", "Deferred tax"],
            "2024": [None, None],
            "2023": [None, None],
        })

    # Dropdown 1: Income Table
    with st.expander("INCOME"):
        st.subheader("Income Table")
        income_df = st.data_editor(
            st.session_state.income_data, key="income_editor", use_container_width=True
        )

        # Convert data to numeric and handle None values
        income_df["2024"] = pd.to_numeric(income_df["2024"], errors="coerce").fillna(0)
        income_df["2023"] = pd.to_numeric(income_df["2023"], errors="coerce").fillna(0)

        # Total Income
        total_income_2024 = income_df["2024"].sum()
        total_income_2023 = income_df["2023"].sum()
        st.session_state.total_income_2024 = total_income_2024
        st.session_state.total_income_2023 = total_income_2023
        st.metric("Total Income (2024)", f"₹{total_income_2024:,.2f}")
        st.metric("Total Income (2023)", f"₹{total_income_2023:,.2f}")

    # Dropdown 2: Expenses Table
    with st.expander("EXPENSES"):
        st.subheader("Expenses Table")
        expense_df = st.data_editor(
            st.session_state.expense_data, key="expenses_editor", use_container_width=True
        )

        # Convert data to numeric and handle None values
        expense_df["2024"] = pd.to_numeric(expense_df["2024"], errors="coerce").fillna(0)
        expense_df["2023"] = pd.to_numeric(expense_df["2023"], errors="coerce").fillna(0)

        # Total Expenses
        total_expenses_2024 = expense_df["2024"].sum()
        total_expenses_2023 = expense_df["2023"].sum()
        st.session_state.total_expenses_2024 = total_expenses_2024
        st.session_state.total_expenses_2023 = total_expenses_2023
        st.metric("Total Expenses (2024)", f"₹{total_expenses_2024:,.2f}")
        st.metric("Total Expenses (2023)", f"₹{total_expenses_2023:,.2f}")

    # Dropdown 3: Tax Table
    with st.expander("TAX"):
        st.subheader("Tax Table")

        # Calculate Profit Before Tax
        profit_before_tax_2024 = total_income_2024 - total_expenses_2024
        profit_before_tax_2023 = total_income_2023 - total_expenses_2023
        st.session_state.profit_before_tax_2024 = profit_before_tax_2024
        st.session_state.profit_before_tax_2023 = profit_before_tax_2023

        st.metric("Profit Before Tax (2024)", f"₹{profit_before_tax_2024:,.2f}")
        st.metric("Profit Before Tax (2023)", f"₹{profit_before_tax_2023:,.2f}")

        # Tax Input Table
        tax_df = st.data_editor(
            st.session_state.tax_data, key="tax_editor", use_container_width=True
        )

        # Convert data to numeric and handle None values
        tax_df["2024"] = pd.to_numeric(tax_df["2024"], errors="coerce").fillna(0)
        tax_df["2023"] = pd.to_numeric(tax_df["2023"], errors="coerce").fillna(0)

        # Calculate Total Tax
        total_tax_2024 = tax_df["2024"].sum()
        total_tax_2023 = tax_df["2023"].sum()

        # Display Total Tax
        st.metric("Total Tax (2024)", f"₹{total_tax_2024:,.2f}")
        st.metric("Total Tax (2023)", f"₹{total_tax_2023:,.2f}")

        # Calculate Profit After Tax
        profit_after_tax_2024 = profit_before_tax_2024 - total_tax_2024
        profit_after_tax_2023 = profit_before_tax_2023 - total_tax_2023
        st.session_state.profit_after_tax_2024 = profit_after_tax_2024
        st.session_state.profit_after_tax_2023 = profit_after_tax_2023

        # Display Profit After Tax
        st.metric("Profit After Tax (2024)", f"₹{profit_after_tax_2024:,.2f}")
        st.metric("Profit After Tax (2023)", f"₹{profit_after_tax_2023:,.2f}")
    # Extract specific values
# Revenue from operations
    revenue_from_operations_2024_row = income_df[income_df['Particulars (In cr)'] == 'Revenue from operations']
    revenue_from_operations_2023_row = income_df[income_df['Particulars (In cr)'] == 'Revenue from operations']

    revenue_from_operations_2024 = revenue_from_operations_2024_row['2024'].iloc[0] if not revenue_from_operations_2024_row.empty else 0
    revenue_from_operations_2023 = revenue_from_operations_2023_row['2023'].iloc[0] if not revenue_from_operations_2023_row.empty else 0

# Other income
    other_income_2024_row = income_df[income_df['Particulars (In cr)'] == 'Other income']
    other_income_2023_row = income_df[income_df['Particulars (In cr)'] == 'Other income']

    other_income_2024 = other_income_2024_row['2024'].iloc[0] if not other_income_2024_row.empty else 0
    other_income_2023 = other_income_2023_row['2023'].iloc[0] if not other_income_2023_row.empty else 0

# Finance costs
    finance_costs_2024_row = expense_df[expense_df['Particulars (In cr)'] == 'Finance costs']
    finance_costs_2023_row = expense_df[expense_df['Particulars (In cr)'] == 'Finance costs']

    finance_costs_2024 = finance_costs_2024_row['2024'].iloc[0] if not finance_costs_2024_row.empty else 0
    finance_costs_2023 = finance_costs_2023_row['2023'].iloc[0] if not finance_costs_2023_row.empty else 0

# Depreciation and amortisation expenses
    depreciation_expenses_2024_row = expense_df[expense_df['Particulars (In cr)'] == 'Depreciation and amortisation expenses']
    depreciation_expenses_2023_row = expense_df[expense_df['Particulars (In cr)'] == 'Depreciation and amortisation expenses']

    depreciation_expenses_2024 = depreciation_expenses_2024_row['2024'].iloc[0] if not depreciation_expenses_2024_row.empty else 0
    depreciation_expenses_2023 = depreciation_expenses_2023_row['2023'].iloc[0] if not depreciation_expenses_2023_row.empty else 0

    # Save button
    if st.button("Save Income Sheet Data"):
        # Saving totals to session state
        st.session_state.total_income_2023 = total_income_2023
        st.session_state.total_income_2024 = total_income_2024
        st.session_state.total_expenses_2023 = total_expenses_2023
        st.session_state.total_expenses_2024 = total_expenses_2024
        st.session_state.total_tax_2023 = total_tax_2023
        st.session_state.total_tax_2024 = total_tax_2024
        st.session_state.profit_before_tax_2023 = profit_before_tax_2023
        st.session_state.profit_before_tax_2024 = profit_before_tax_2024
        st.session_state.profit_after_tax_2023 = profit_after_tax_2023
        st.session_state.profit_after_tax_2024 = profit_after_tax_2024
        st.session_state.revenue_from_operations_2023 = revenue_from_operations_2023
        st.session_state.revenue_from_operations_2024 = revenue_from_operations_2024
        st.session_state.other_income_2023 = other_income_2023
        st.session_state.other_income_2024 = other_income_2024
        st.session_state.finance_costs_2023 = finance_costs_2023
        st.session_state.finance_costs_2024 = finance_costs_2024
        st.session_state.depreciation_expenses_2023 = depreciation_expenses_2023
        st.session_state.depreciation_expenses_2024 = depreciation_expenses_2024
        # Save data to JSON
        save_data_to_json()

    return st.session_state.income_data
