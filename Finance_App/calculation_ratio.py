import streamlit as st
import json

def save_data_to_json():
    # Retrieve the balance sheet data from session state
    data = {
        "debt_to_equity_ratio_2024": st.session_state.get("debt_to_equity_ratio_2024", 0),
        "debt_to_equity_ratio_2023": st.session_state.get("debt_to_equity_ratio_2023", 0),
        "current_ratio_2024": st.session_state.get("current_ratio_2024", 0),
        "current_ratio_2023": st.session_state.get("current_ratio_2023", 0),
        "quick_ratio_2024": st.session_state.get("quick_ratio_2024", 0),
        "quick_ratio_2023": st.session_state.get("quick_ratio_2023", 0),
        "roe_2024": st.session_state.get("roe_2024", 0),
        "roe_2023": st.session_state.get("roe_2023", 0),
        "working_capital_turnover_ratio_2024": st.session_state.get("working_capital_turnover_ratio_2024", 0),
        "working_capital_turnover_ratio_2023": st.session_state.get("working_capital_turnover_ratio_2023", 0),
        "operating_profit_ratio_2024": st.session_state.get("operating_profit_ratio_2024", 0),
        "operating_profit_ratio_2023": st.session_state.get("operating_profit_ratio_2023", 0),
        "roa_2024": st.session_state.get("roa_2024", 0),
        "roa_2023": st.session_state.get("roa_2023", 0),
        "fixed_charge_cover_ratio_2024": st.session_state.get("fixed_charge_cover_ratio_2024", 0),
        "fixed_charge_cover_ratio_2023": st.session_state.get("fixed_charge_cover_ratio_2023", 0)
           }

        # Save the data to a JSON file
    with open("calculation_data.json", "w") as json_file:
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
        revenue_from_operations_2024 = st.session_state.get("revenue_from_operations_2024", 0)
        revenue_from_operations_2023 = st.session_state.get("revenue_from_operations_2023", 0)
        profit_before_tax_2024 = st.session_state.get("profit_before_tax_2024", 0)
        profit_before_tax_2023 = st.session_state.get("profit_before_tax_2023", 0)
        depreciation_expenses_2024 = st.session_state.get("depreciation_expenses_2024", 0)
        depreciation_expenses_2023 = st.session_state.get("depreciation_expenses_2023", 0)
        finance_costs_2024 = st.session_state.get("finance_costs_2024", 0)
        finance_costs_2023 = st.session_state.get("finance_costs_2023", 0)
        other_income_2024 = st.session_state.get("other_income_2024", 0)
        other_income_2023 = st.session_state.get("other_income_2023", 0)
        total_assets_2024 = st.session_state.get("total_assets_2024", 0)
        total_assets_2023 = st.session_state.get("total_assets_2023", 0)

        # Debt to Equity Ratio
        debt_to_equity_ratio_2024 = total_current_liabilities_2024 / total_shareholder_funds_2024 if total_shareholder_funds_2024 else None
        debt_to_equity_ratio_2023 = total_current_liabilities_2023 / total_shareholder_funds_2023 if total_shareholder_funds_2023 else None

        # Current Ratio
        current_ratio_2024 = total_current_assets_2024 / total_current_liabilities_2024 if total_current_liabilities_2024 else None
        current_ratio_2023 = total_current_assets_2023 / total_current_liabilities_2023 if total_current_liabilities_2023 else None

        # Quick Ratio
        quick_ratio_2024 = (total_current_assets_2024 - inventories_2024) / total_current_liabilities_2024 if total_current_liabilities_2024 else None
        quick_ratio_2023 = (total_current_assets_2023 - inventories_2023) / total_current_liabilities_2023 if total_current_liabilities_2023 else None

        # Return on Equity (ROE)
        roe_2024 = profit_after_tax_2024 / total_shareholder_funds_2024 if total_shareholder_funds_2024 else None
        roe_2023 = profit_after_tax_2023 / total_shareholder_funds_2023 if total_shareholder_funds_2023 else None

        # Working Capital Turnover Ratio
        working_capital_turnover_ratio_2024 = revenue_from_operations_2024 / (total_current_assets_2024 - total_current_liabilities_2024) if (total_current_assets_2024 - total_current_liabilities_2024) else None
        working_capital_turnover_ratio_2023 = revenue_from_operations_2023 / (total_current_assets_2023 - total_current_liabilities_2023) if (total_current_assets_2023 - total_current_liabilities_2023) else None

        # Operating Profit Ratio
        operating_profit_ratio_2024 = (profit_before_tax_2024 + depreciation_expenses_2024 + finance_costs_2024 - other_income_2024)
        operating_profit_ratio_2023 = (profit_before_tax_2023 + depreciation_expenses_2023 + finance_costs_2023 - other_income_2023)

        # Return on Assets (ROA)
        roa_2024 = revenue_from_operations_2024 / total_assets_2024 if total_assets_2024 else None
        roa_2023 = revenue_from_operations_2023 / total_assets_2023 if total_assets_2023 else None

        # Fixed Charge Cover Ratio
        fixed_charge_cover_ratio_2024 = (profit_before_tax_2024 + finance_costs_2024) / finance_costs_2024 if finance_costs_2024 else None
        fixed_charge_cover_ratio_2023 = (profit_before_tax_2023 + finance_costs_2023) / finance_costs_2023 if finance_costs_2023 else None

        # Display the metrics
        st.subheader("Debt to Equity Ratio")
        st.metric("2024", f"{debt_to_equity_ratio_2024:.2f}" if debt_to_equity_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{debt_to_equity_ratio_2023:.2f}" if debt_to_equity_ratio_2023 is not None else "N/A")
        st.divider()

        st.subheader("Current Ratio")
        st.metric("2024", f"{current_ratio_2024:.2f}" if current_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{current_ratio_2023:.2f}" if current_ratio_2023 is not None else "N/A")
        st.divider()

        st.subheader("Quick Ratio")
        st.metric("2024", f"{quick_ratio_2024:.2f}" if quick_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{quick_ratio_2023:.2f}" if quick_ratio_2023 is not None else "N/A")
        st.divider()

        st.subheader("Return on Equity (ROE)")
        st.metric("2024", f"{roe_2024:.2f}" if roe_2024 is not None else "N/A")
        st.metric("2023", f"{roe_2023:.2f}" if roe_2023 is not None else "N/A")
        st.divider()

        st.subheader("Working Capital Turnover Ratio")
        st.metric("2024", f"{working_capital_turnover_ratio_2024:.2f}" if working_capital_turnover_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{working_capital_turnover_ratio_2023:.2f}" if working_capital_turnover_ratio_2023 is not None else "N/A")
        st.divider()

        st.subheader("Operating Profit Ratio")
        st.metric("2024", f"{operating_profit_ratio_2024:.2f}")
        st.metric("2023", f"{operating_profit_ratio_2023:.2f}")
        st.divider()

        st.subheader("Return on Assets (ROA)")
        st.metric("2024", f"{roa_2024:.2f}" if roa_2024 is not None else "N/A")
        st.metric("2023", f"{roa_2023:.2f}" if roa_2023 is not None else "N/A")
        st.divider()

        st.subheader("Fixed Charge Cover Ratio")
        st.metric("2024", f"{fixed_charge_cover_ratio_2024:.2f}" if fixed_charge_cover_ratio_2024 is not None else "N/A")
        st.metric("2023", f"{fixed_charge_cover_ratio_2023:.2f}" if fixed_charge_cover_ratio_2023 is not None else "N/A")

    else:
        st.warning("Please complete the Balance Sheet or Income Sheet first.")

    if st.button("Save Calculation Data"):
        st.session_state["operating_profit_ratio_2024"] = operating_profit_ratio_2024
        st.session_state["operating_profit_ratio_2023"] = operating_profit_ratio_2023
        st.session_state["roa_2024"] = roa_2024 
        st.session_state["roa_2023"] = roa_2023
        st.session_state["fixed_charge_cover_ratio_2024"] = fixed_charge_cover_ratio_2024
        st.session_state["fixed_charge_cover_ratio_2023"] = fixed_charge_cover_ratio_2023
        st.session_state["debt_to_equity_ratio_2024"] = debt_to_equity_ratio_2024 
        st.session_state["debt_to_equity_ratio_2023"] = debt_to_equity_ratio_2023
        st.session_state["current_ratio_2024"] = current_ratio_2024 
        st.session_state["current_ratio_2023"] = current_ratio_2023
        st.session_state["quick_ratio_2024"] = quick_ratio_2024 
        st.session_state["quick_ratio_2023"] = quick_ratio_2023
        st.session_state["roe_2024"] = roe_2024 
        st.session_state["roe_2023"] = roe_2023
        st.session_state["working_capital_turnover_ratio_2024"] = working_capital_turnover_ratio_2024 
        st.session_state["working_capital_turnover_ratio_2023"] = working_capital_turnover_ratio_2023
  

        save_data_to_json()
        st.success("Calculation data saved successfully!")
