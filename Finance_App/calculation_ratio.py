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
        revenue_operations_2024 = st.session_state.get("revenue_operations_2024", 0)
        revenue_operations_2023 = st.session_state.get("revenue_operations_2023", 0)
        total_assets_2024 = st.session_state.get("total_assets_2024", 0)
        total_assets_2023 = st.session_state.get("total_assets_2023", 0)
        profit_before_tax_2024 = st.session_state.get("profit_before_tax_2024", 0)
        profit_before_tax_2023 = st.session_state.get("profit_before_tax_2023", 0)
        depreciation_amortization_2024 = st.session_state.get("depreciation_amortization_2024", 0)
        depreciation_amortization_2023 = st.session_state.get("depreciation_amortization_2023", 0)
        finance_cost_2024 = st.session_state.get("finance_cost_2024", 0)
        finance_cost_2023 = st.session_state.get("finance_cost_2023", 0)
        other_income_2024 = st.session_state.get("other_income_2024", 0)
        other_income_2023 = st.session_state.get("other_income_2023", 0)

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

        # Return on Equity (ROE)
        if total_shareholder_funds_2024 != 0:
            roe_2024 = profit_after_tax_2024 / total_shareholder_funds_2024
        else:
            roe_2024 = None

        if total_shareholder_funds_2023 != 0:
            roe_2023 = profit_after_tax_2023 / total_shareholder_funds_2023
        else:
            roe_2023 = None

        # Working Capital Turnover Ratio
        if (total_current_assets_2024 - total_current_liabilities_2024) != 0:
            working_capital_turnover_2024 = revenue_operations_2024 / (total_current_assets_2024 - total_current_liabilities_2024)
        else:
            working_capital_turnover_2024 = None

        if (total_current_assets_2023 - total_current_liabilities_2023) != 0:
            working_capital_turnover_2023 = revenue_operations_2023 / (total_current_assets_2023 - total_current_liabilities_2023)
        else:
            working_capital_turnover_2023 = None

        # Operating Profit Ratio
        operating_profit_ratio_2024 = profit_before_tax_2024 + depreciation_amortization_2024 + finance_cost_2024 - other_income_2024
        operating_profit_ratio_2023 = profit_before_tax_2023 + depreciation_amortization_2023 + finance_cost_2023 - other_income_2023

        # Return on Asset
        if total_assets_2024 != 0:
            return_on_asset_2024 = revenue_operations_2024 / total_assets_2024
        else:
            return_on_asset_2024 = None

        if total_assets_2023 != 0:
            return_on_asset_2023 = revenue_operations_2023 / total_assets_2023
        else:
            return_on_asset_2023 = None

        # Quick Asset Ratio
        if total_current_liabilities_2024 != 0:
            quick_asset_2024 = (total_current_assets_2024 - inventories_2024) / total_current_liabilities_2024
        else:
            quick_asset_2024 = None

        if total_current_liabilities_2023 != 0:
            quick_asset_2023 = (total_current_assets_2023 - inventories_2023) / total_current_liabilities_2023
        else:
            quick_asset_2023 = None

        # Fixed Charge Cover Ratio
        if finance_cost_2024 != 0:
            fixed_charge_cover_2024 = (profit_before_tax_2024 + finance_cost_2024) / finance_cost_2024
        else:
            fixed_charge_cover_2024 = None

        if finance_cost_2023 != 0:
            fixed_charge_cover_2023 = (profit_before_tax_2023 + finance_cost_2023) / finance_cost_2023
        else:
            fixed_charge_cover_2023 = None

        # Display the metrics
        st.subheader("Debt to Equity Ratio")
        st.metric("2024", f"{debt_to_equity_ratio_2024:.2f}" if debt_to_equity_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{debt_to_equity_ratio_2023:.2f}" if debt_to_equity_ratio_2023 is not None else "N/A")

        st.subheader("Current Ratio")
        st.metric("2024", f"{current_ratio_2024:.2f}" if current_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{current_ratio_2023:.2f}" if current_ratio_2023 is not None else "N/A")

        st.subheader("Return on Equity (ROE)")
        st.metric("2024", f"{roe_2024:.2f}" if roe_2024 is not None else "N/A")
        st.metric("2023", f"{roe_2023:.2f}" if roe_2023 is not None else "N/A")

        st.subheader("Working Capital Turnover Ratio")
        st.metric("2024", f"{working_capital_turnover_2024:.2f}" if working_capital_turnover_2024 is not None else "N/A")
        st.metric("2023", f"{working_capital_turnover_2023:.2f}" if working_capital_turnover_2023 is not None else "N/A")

        st.subheader("Operating Profit Ratio")
        st.metric("2024", f"{operating_profit_ratio_2024:.2f}" if operating_profit_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{operating_profit_ratio_2023:.2f}" if operating_profit_ratio_2023 is not None else "N/A")

        st.subheader("Return on Asset")
        st.metric("2024", f"{return_on_asset_2024:.2f}" if return_on_asset_2024 is not None else "N/A")
        st.metric("2023", f"{return_on_asset_2023:.2f}" if return_on_asset_2023 is not None else "N/A")

        st.subheader("Quick Asset Ratio")
        st.metric("2024", f"{quick_asset_2024:.2f}" if quick_asset_2024 is not None else "N/A")
        st.metric("2023", f"{quick_asset_2023:.2f}" if quick_asset_2023 is not None else "N/A")

        st.subheader("Fixed Charge Cover Ratio")
        st.metric("2024", f"{fixed_charge_cover_2024:.2f}" if fixed_charge_cover_2024 is not None else "N/A")
        st.metric("2023", f"{fixed_charge_cover_2023:.2f}" if fixed_charge_cover_2023 is not None else "N/A")

    else:
        st.warning("Please complete the Balance Sheet first.")

    if st.button("Save Calculation Data"):
        save_data_to_json()
        st.success("Calculation data saved to JSON successfully!")
