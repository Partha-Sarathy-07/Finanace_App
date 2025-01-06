import streamlit as st

def display_insights():
    st.title("Financial Insights")

    # Retrieve calculated ratio values from session state
    debt_to_equity_ratio_2024 = st.session_state.get("debt_to_equity_ratio_2024", None)
    working_capital_turnover_ratio_2024 = st.session_state.get("working_capital_turnover_ratio_2024", None)
    operating_profit_ratio_2024 = st.session_state.get("operating_profit_ratio_2024", None)
    roa_2024 = st.session_state.get("roa_2024", None)
    current_ratio_2024 = st.session_state.get("current_ratio_2024", None)
    quick_ratio_2024 = st.session_state.get("quick_ratio_2024", None)
    fixed_charge_cover_ratio_2024 = st.session_state.get("fixed_charge_cover_ratio_2024", None)
    roe_2024 = st.session_state.get("roe_2024", None)
    debt_to_equity_ratio_2024 = st.session_state.get("debt_to_equity_ratio_2024", None)
    working_capital_turnover_ratio_2024 = st.session_state.get("working_capital_turnover_ratio_2024", None)
    operating_profit_ratio_2024 = st.session_state.get("operating_profit_ratio_2024", None)
    roa_2024 = st.session_state.get("roa_2024", None)
    current_ratio_2024 = st.session_state.get("current_ratio_2024", None)
    quick_ratio_2024 = st.session_state.get("quick_ratio_2024", None)
    fixed_charge_cover_ratio_2024 = st.session_state.get("fixed_charge_cover_ratio_2024", None)
    roe_2024 = st.session_state.get("roe_2024", None)

    debt_to_equity_ratio_2023 = st.session_state.get("debt_to_equity_ratio_2023", None)
    working_capital_turnover_ratio_2023 = st.session_state.get("working_capital_turnover_ratio_2023", None)
    operating_profit_ratio_2023 = st.session_state.get("operating_profit_ratio_2023", None)
    roa_2023 = st.session_state.get("roa_2023", None)
    current_ratio_2023 = st.session_state.get("current_ratio_2023", None)
    quick_ratio_2023 = st.session_state.get("quick_ratio_2023", None)
    fixed_charge_cover_ratio_2023 = st.session_state.get("fixed_charge_cover_ratio_2023", None)
    roe_2023 = st.session_state.get("roe_2023", None)
    debt_to_equity_ratio_2023 = st.session_state.get("debt_to_equity_ratio_2023", None)
    working_capital_turnover_ratio_2023 = st.session_state.get("working_capital_turnover_ratio_2023", None)
    operating_profit_ratio_2023 = st.session_state.get("operating_profit_ratio_2023", None)
    roa_2023 = st.session_state.get("roa_2023", None)
    current_ratio_2023 = st.session_state.get("current_ratio_2023", None)
    quick_ratio_2023 = st.session_state.get("quick_ratio_2023", None)
    fixed_charge_cover_ratio_2023 = st.session_state.get("fixed_charge_cover_ratio_2023", None)
    roe_2023 = st.session_state.get("roe_2023", None)

    # Function to display insights based on ratio values
    def provide_insight(ratio, standard_low, standard_high, above_msg, below_msg):
        if ratio is None:
            st.write("Data not available.")
        elif ratio > standard_high:
            st.success(f"Above Standard: {above_msg}")
        elif ratio < standard_low:
            st.warning(f"Below Standard: {below_msg}")
        else:
            st.info("Within Standard Range")

    # Debt to Equity Ratio
    st.subheader("Debt to Equity Ratio (Standard: 2:1)")
    st.metric("2024", f"{debt_to_equity_ratio_2024:.2f}" if debt_to_equity_ratio_2024 is not None else "N/A")
    provide_insight(debt_to_equity_ratio_2024, 0, 2,
                    "High financial leverage. Could indicate aggressive expansion or high reliance on debt financing.",
                    "Low financial leverage. Could indicate conservative financing or strong internal cash flows.")
    

    st.metric("2023", f"{debt_to_equity_ratio_2023:.2f}" if debt_to_equity_ratio_2023 is not None else "N/A")
    provide_insight(debt_to_equity_ratio_2023, 0, 2,
                    "High financial leverage. Could indicate aggressive expansion or high reliance on debt financing.",
                    "Low financial leverage. Could indicate conservative financing or strong internal cash flows.")
    st.divider()

    # Working Capital Turnover Ratio
    st.subheader("Working Capital Turnover Ratio (Standard: 6 to 10)")
    st.metric("2024", f"{working_capital_turnover_ratio_2024:.2f}" if working_capital_turnover_ratio_2024 is not None else "N/A")
    provide_insight(working_capital_turnover_ratio_2024, 6, 10,
                    "Efficient use of working capital to generate sales.",
                    "Inefficient use of working capital. Could indicate excessive inventory or declining sales.")
    
   
    st.metric("2023", f"{working_capital_turnover_ratio_2023:.2f}" if working_capital_turnover_ratio_2023 is not None else "N/A")
    provide_insight(working_capital_turnover_ratio_2023, 6, 10,
                    "Efficient use of working capital to generate sales.",
                    "Inefficient use of working capital. Could indicate excessive inventory or declining sales.")
    st.divider()

    # Operating Profit Ratio
    st.subheader("Operating Profit Ratio (Standard: 10% to 20%)")
    st.metric("2024", f"{operating_profit_ratio_2024:.2f}" if operating_profit_ratio_2024 is not None else "N/A")
    provide_insight(operating_profit_ratio_2024, 0.1, 0.2,
                    "Strong operational efficiency and cost control.",
                    "Poor operational efficiency. Could indicate high operating costs or low sales.")

    st.metric("2023", f"{operating_profit_ratio_2023:.2f}" if operating_profit_ratio_2023 is not None else "N/A")
    provide_insight(operating_profit_ratio_2023, 0.1, 0.2,
                    "Strong operational efficiency and cost control.",
                    "Poor operational efficiency. Could indicate high operating costs or low sales.")
    st.divider()

    # Return on Assets (ROA)
    st.subheader("Return on Assets (ROA) (Standard: 5% or higher)")
    st.metric("2024", f"{roa_2024:.2f}" if roa_2024 is not None else "N/A")
    provide_insight(roa_2024, 0.05, float('inf'),
                    "Efficient use of assets to generate profits.",
                    "Inefficient use of assets. Could indicate underutilized assets or declining profitability.")

    st.metric("2023", f"{roa_2023:.2f}" if roa_2023 is not None else "N/A")
    provide_insight(roa_2023, 0.05, float('inf'),
                    "Efficient use of assets to generate profits.",
                    "Inefficient use of assets. Could indicate underutilized assets or declining profitability.")
    st.divider()

    # Current Ratio
    st.subheader("Current Ratio (Standard: 2:1)")
    st.metric("2024", f"{current_ratio_2024:.2f}" if current_ratio_2024 is not None else "N/A")
    provide_insight(current_ratio_2024, 2, float('inf'),
                    "Strong liquidity.",
                    "Potential liquidity issues. Could indicate high short-term liabilities.")
    

    st.metric("2023", f"{current_ratio_2023:.2f}" if current_ratio_2023 is not None else "N/A")
    provide_insight(current_ratio_2023, 2, float('inf'),
                    "Strong liquidity.",
                    "Potential liquidity issues. Could indicate high short-term liabilities.")
    st.divider()

    # Quick Ratio
    st.subheader("Quick Ratio (Standard: 1:1)")
    st.metric("2024", f"{quick_ratio_2024:.2f}" if quick_ratio_2024 is not None else "N/A")
    provide_insight(quick_ratio_2024, 1, float('inf'),
                    "Strong short-term liquidity.",
                    "Potential liquidity issues. Could indicate high reliance on inventory for liquidity.")
    
 
    st.metric("2023", f"{quick_ratio_2023:.2f}" if quick_ratio_2023 is not None else "N/A")
    provide_insight(quick_ratio_2023, 1, float('inf'),
                    "Strong short-term liquidity.",
                    "Potential liquidity issues. Could indicate high reliance on inventory for liquidity.")
    st.divider()

    # Fixed Charge Coverage Ratio
    st.subheader("Fixed Charge Coverage Ratio (Standard: > 1.5)")
    st.metric("2024", f"{fixed_charge_cover_ratio_2024:.2f}" if fixed_charge_cover_ratio_2024 is not None else "N/A")
    provide_insight(fixed_charge_cover_ratio_2024, 1.5, float('inf'),
                    "Strong ability to cover fixed charges.",
                    "Potential difficulty in covering fixed charges. Could indicate high fixed costs.")
    st.metric("2023", f"{fixed_charge_cover_ratio_2023:.2f}" if fixed_charge_cover_ratio_2023 is not None else "N/A")
    provide_insight(fixed_charge_cover_ratio_2023, 1.5, float('inf'),
                    "Strong ability to cover fixed charges.",
                    "Potential difficulty in covering fixed charges. Could indicate high fixed costs.")
    st.divider()

    # Return on Equity (ROE)
    st.subheader("Return on Equity (ROE) (Standard: 15% or higher)")
    st.metric("2024", f"{roe_2024:.2f}" if roe_2024 is not None else "N/A")
    provide_insight(roe_2024, 0.15, float('inf'),
                    "Efficient use of equity capital to generate profits.",
                    "Inefficient use of equity. Could indicate low net income or poor management performance.")

    st.metric("2023", f"{roe_2023:.2f}" if roe_2023 is not None else "N/A")
    provide_insight(roe_2023, 0.15, float('inf'),
                    "Efficient use of equity capital to generate profits.",
                    "Inefficient use of equity. Could indicate low net income or poor management performance.")
    # Function to evaluate each ratio
    def evaluate_ratio(ratio, standard_low, standard_high):
        if ratio is None:
            return 0  # No score if data is not available
        elif standard_low <= ratio <= standard_high:
            return 2  # Full score if within standard range
        elif ratio > standard_high:
            return 1  # Partial score if above standard
        else:
            return 1  # Partial score if below standard

    # Calculate scores for each ratio in both years
    scores_2024 = sum([
        evaluate_ratio(debt_to_equity_ratio_2024, 0, 2),
        evaluate_ratio(working_capital_turnover_ratio_2024, 6, 10),
        evaluate_ratio(operating_profit_ratio_2024, 0.1, 0.2),
        evaluate_ratio(roa_2024, 0.05, float('inf')),
        evaluate_ratio(current_ratio_2024, 2, float('inf')),
        evaluate_ratio(quick_ratio_2024, 1, float('inf')),
        evaluate_ratio(fixed_charge_cover_ratio_2024, 1.5, float('inf')),
        evaluate_ratio(roe_2024, 0.15, float('inf'))
    ])

    scores_2023 = sum([
        evaluate_ratio(debt_to_equity_ratio_2023, 0, 2),
        evaluate_ratio(working_capital_turnover_ratio_2023, 6, 10),
        evaluate_ratio(operating_profit_ratio_2023, 0.1, 0.2),
        evaluate_ratio(roa_2023, 0.05, float('inf')),
        evaluate_ratio(current_ratio_2023, 2, float('inf')),
        evaluate_ratio(quick_ratio_2023, 1, float('inf')),
        evaluate_ratio(fixed_charge_cover_ratio_2023, 1.5, float('inf')),
        evaluate_ratio(roe_2023, 0.15, float('inf'))
    ])

    # Display overall insights
    st.subheader("###Overall Insights")
    if scores_2024 > scores_2023:
        st.success(f"2024 is a better year with a total score of {scores_2024} compared to 2023's score of {scores_2023}.")
    elif scores_2024 < scores_2023:
        st.success(f"2023 is a better year with a total score of {scores_2023} compared to 2024's score of {scores_2024}.")
    else:
        st.info(f"Both years have similar performance with a score of {scores_2024}.")
    
# Call the function in the appropriate part of your Streamlit app
if __name__ == "__main__":
    display_insights()
