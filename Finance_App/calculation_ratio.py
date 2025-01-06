import streamlit as st
import json

def save_data_to_json():
    # Retrieve the balance sheet data from session state
    if "df_balance" in st.session_state:
        df_balance = st.session_state.df_balance
        balance_json = df_balance.to_json(orient="records")

        # Save other relevant financial data from session state if required
        total_non_current_liabilities_2023 = st.session_state.get("total_non_current_2023", 0)
        total_shareholder_funds_2023 = st.session_state.get("total_shareholder_2023", 0)

        # Create the data dictionary
        data = {
            "balance_sheet": json.loads(balance_json),
            "total_non_current_liabilities_2023": total_non_current_liabilities_2023,
            "total_shareholder_funds_2023": total_shareholder_funds_2023
        }

        # Save the data to a JSON file
        with open("financial_calculation_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

def display_calculation_ratio():
    st.title("Calculation Ratio")

    if "df_balance" in st.session_state:
        # Retrieve required values from session state
        total_current_assets_2024 = st.session_state.get("total_current_assets_2024", 0)
        total_current_liabilities_2024 = st.session_state.get("total_current_liabilities_2024", 0)
        total_current_assets_2023 = st.session_state.get("total_current_assets_2023", 0)
        total_current_liabilities_2023 = st.session_state.get("total_current_liabilities_2023", 0)
        inventories_2024 = st.session_state.get("inventories_2024", 0)
        inventories_2023 = st.session_state.get("inventories_2023", 0)
        profit_after_tax_2024 = st.session_state.get("profit_after_tax_2024", 0)
        profit_after_tax_2023 = st.session_state.get("profit_after_tax_2023", 0)
        total_shareholder_funds_2024 = st.session_state.get("total_shareholder_2024", 0)
        total_shareholder_funds_2023 = st.session_state.get("total_shareholder_2023", 0)

        # Debt to Equity Ratio
        if total_shareholder_funds_2024 != 0:
            debt_to_equity_ratio_2024 = total_current_liabilities_2024 / total_shareholder_funds_2024
        else:
            debt_to_equity_ratio_2024 = None

        if total_shareholder_funds_2023 != 0:
            debt_to_equity_ratio_2023 = total_current_liabilities_2023 / total_shareholder_funds_2023
        else:
            debt_to_equity_ratio_2023 = None

        # Current Ratio
        if total_current_liabilities_2024 != 0:
            current_ratio_2024 = total_current_assets_2024 / total_current_liabilities_2024
        else:
            current_ratio_2024 = None

        if total_current_liabilities_2023 != 0:
            current_ratio_2023 = total_current_assets_2023 / total_current_liabilities_2023
        else:
            current_ratio_2023 = None

        # Quick Ratio
        if total_current_liabilities_2024 != 0:
            quick_ratio_2024 = (total_current_assets_2024 - inventories_2024) / total_current_liabilities_2024
        else:
            quick_ratio_2024 = None

        if total_current_liabilities_2023 != 0:
            quick_ratio_2023 = (total_current_assets_2023 - inventories_2023) / total_current_liabilities_2023
        else:
            quick_ratio_2023 = None

        # Return on Equity (ROE)
        if total_shareholder_funds_2024 != 0:
            roe_2024 = profit_after_tax_2024 / total_shareholder_funds_2024
        else:
            roe_2024 = None

        if total_shareholder_funds_2023 != 0:
            roe_2023 = profit_after_tax_2023 / total_shareholder_funds_2023
        else:
            roe_2023 = None

        # Display the metrics
        st.subheader("Debt to Equity Ratio")
        st.metric("2024", f"{debt_to_equity_ratio_2024:.2f}" if debt_to_equity_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{debt_to_equity_ratio_2023:.2f}" if debt_to_equity_ratio_2023 is not None else "N/A")

        st.subheader("Current Ratio")
        st.metric("2024", f"{current_ratio_2024:.2f}" if current_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{current_ratio_2023:.2f}" if current_ratio_2023 is not None else "N/A")

        st.subheader("Quick Ratio")
        st.metric("2024", f"{quick_ratio_2024:.2f}" if quick_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{quick_ratio_2023:.2f}" if quick_ratio_2023 is not None else "N/A")

        st.subheader("Return on Equity (ROE)")
        st.metric("2024", f"{roe_2024:.2f}" if roe_2024 is not None else "N/A")
        st.metric("2023", f"{roe_2023:.2f}" if roe_2023 is not None else "N/A")

    else:
        st.warning("Please complete the Balance Sheet or Income Sheet first.")

    if st.button("Save Calculation Data"):
        save_data_to_json()
        st.success("Calculation data saved to JSON successfully!")
