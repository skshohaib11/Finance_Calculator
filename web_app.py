import streamlit as st
from calculator import InvestmentCalculator  # Import your InvestmentCalculator class

# Create a Streamlit app title
st.title("Financial Calculator")

#about this Calculator
github_link = "[GitHub Repository](https://github.com/skshohaib11/Stoploss_calculator)"
LinkedIn_link = "[LinkedIn](https://www.linkedin.com/in/shaikh-mohammed-shohaib-043317251/)"
st.sidebar.title("About The Calculator.")
st.sidebar.write("This calculator provides you to calculate your investment using Mutual Funds calculator with SIP and One Time Investment.")
st.sidebar.write("The Loan EMI calculator let's you know the EMI on monthly basis excluding the bank Interest Amount and other fees depending on different banks.")
st.sidebar.write("With FD and RD calculator you can get to know the interest gained on your principle amount.")
st.sidebar.markdown(github_link)
st.sidebar.markdown(LinkedIn_link)
st.sidebar.write('Prepared By: Shohaib Shaikh')

# Create a dropdown for navigation
col1, col2 = st.columns(2)
menu = col1.selectbox("Select Your Calculator", ["Mutual Fund Calculator", "Loan EMI Calculator", "FD Calculator", "RD Calculator"])

if menu == "Mutual Fund Calculator":
    sub_menu = col2.selectbox("Select Type of Investment", ["SIP (Systematic Investment Plan)", "One-Time Investment "])
    if sub_menu == "SIP (Systematic Investment Plan)":
        st.subheader("SIP (Systematic Investment Plan)")
        # Create Streamlit widgets for SIP inputs
        principal_amount = st.number_input("Enter Principal Amount")
        monthly_investment = st.number_input("Enter Monthly Investment")
        annual_growth_rate = st.slider("Enter Annual Growth Rate (%)", min_value=0, max_value=100, value=12)
        tenure_years = int(st.number_input("Enter Tenure (in years)"))  # Convert to integer
        annual_inflation_rate = st.slider("Enter Annual Inflation Rate (%)", min_value=0, max_value=100, value=3)  # Added inflation rate input

        # Create a button to calculate SIP results
        if st.button("Calculate SIP"):
            # Create an instance of your InvestmentCalculator class
            sip_calculator = InvestmentCalculator(monthly_investment, annual_growth_rate, tenure_years, annual_inflation_rate)  # Added inflation rate parameter

            # Calculate SIP results based on user inputs
            invested_amount, profit, total_amount = sip_calculator.calculate_sip(principal_amount)

            # Display the results to the user
            st.write(f"Total Invested Amount: {invested_amount}")
            st.write(f"Profit on Investment: {profit}")
            st.write(f"Total Amount: {total_amount}")

    elif sub_menu == "One-Time Investment ":
        st.subheader("One-Time Investment ")
        # Create Streamlit widgets for one-time investment inputs
        one_time_amount = st.number_input("Enter One-Time Investment Amount")
        annual_growth_rate = st.slider("Enter Annual Growth Rate (%)", min_value=0, max_value=100, value=8)
        tenure_years = int(st.number_input("Enter Tenure (in years)"))  # Convert to integer
        annual_inflation_rate = st.slider("Enter Annual Inflation Rate (%)", min_value=0, max_value=100, value=3)  # Added inflation rate input

        # Create a button to calculate One-Time Investment results
        if st.button("Calculate One-Time Investment"):
            # Create an instance of your InvestmentCalculator class
            one_time_calculator = InvestmentCalculator(0, annual_growth_rate, tenure_years, annual_inflation_rate)  # Added inflation rate parameter

            # Calculate One-Time Investment results based on user inputs
            invested_amount, profit, total_amount = one_time_calculator.calculate_one_time_investment(one_time_amount)

            # Display the results to the user
            st.write(f"Total Invested Amount: {invested_amount}")
            st.write(f"Profit on Investment: {profit}")
            st.write(f"Total Amount: {total_amount}")

elif menu == "Loan EMI Calculator":
    st.subheader("Loan EMI Calculator")
    # Create Streamlit widgets for loan EMI inputs
    principal_amount = st.number_input("Enter Loan Principal Amount")
    annual_interest_rate = st.number_input("Enter Annual Interest Rate (%)")
    tenure_years = int(st.number_input("Enter Loan Tenure (in years)"))  # Convert to integer

    # Create a button to calculate Loan EMI results
    if st.button("Calculate Loan EMI"):
        # Create an instance of your InvestmentCalculator class
        loan_calculator = InvestmentCalculator(0, 0, 0)

        # Calculate Loan EMI based on user inputs
        try:
            loan_emi, num_monthly_installments = loan_calculator.calculate_loan_emi(principal_amount, annual_interest_rate, tenure_years)

            # Handle division by zero error
            if loan_emi == 0:
                st.write("Loan EMI calculation error. Please check your input values.")
            else:
            # Display the results to the user
                st.write(f"Loan EMI: {loan_emi}")
                st.write(f"Loan Tenure (in months): {num_monthly_installments}")
        except ZeroDivisionError:
            st.write("Loan Tenure and Annual Interest Rate should not be 0. Please check your input values.")

elif menu == "FD Calculator":
    st.subheader("FD Calculator")
    col1, col2 = st.columns(2)

    # Create Streamlit widgets for FD inputs in two columns
    with col1:
        fd_principal_amount = st.number_input("FD Principal Amount")
    with col2:
        fd_interest_rate = st.number_input("Annual FD Interest Rate (%)")
    fd_tenure_years = int(st.number_input("FD Tenure (in years)"))  # Convert to integer

    # Create a button to calculate FD results
    if st.button("Calculate FD Returns"):
        # Create an instance of your InvestmentCalculator class
        fd_calculator = InvestmentCalculator(0, 0, 0)

        # Calculate FD returns based on user inputs
        fd_invested_amount, fd_interest_earned, fd_total_value = fd_calculator.calculate_fd_returns(fd_principal_amount, fd_interest_rate, fd_tenure_years)

        # Display the results to the user
        st.write(f"FD Total Invested Amount: {fd_invested_amount}")
        st.write(f"FD Interest Earned: {fd_interest_earned}")
        st.write(f"FD Total Value: {fd_total_value}")

elif menu == "RD Calculator":
    st.subheader("RD Calculator")
    col1, col2 = st.columns(2)

    # Create Streamlit widgets for RD inputs in two columns
    with col1:
        rd_monthly_deposit = st.number_input("Monthly RD Deposit Amount")
    with col2:
        rd_interest_rate = st.number_input("Annual RD Interest Rate (%)")
    rd_tenure_years = int(st.number_input("RD Tenure (in years)"))  # Convert to integer

    # Create a button to calculate RD results
    if st.button("Calculate RD Returns"):
        # Create an instance of your InvestmentCalculator class
        rd_calculator = InvestmentCalculator(0, 0, 0)

        # Calculate RD returns based on user inputs
        rd_invested_amount, rd_interest_earned, rd_total_value = rd_calculator.calculate_rd_returns(rd_monthly_deposit, rd_interest_rate, rd_tenure_years)

        # Display the results to the user
        st.write(f"RD Total Invested Amount: {rd_invested_amount}")
        st.write(f"RD Interest Earned: {rd_interest_earned}")
        st.write(f"RD Total Value: {rd_total_value}")


st.write('DISCLAIMER:')
st.write('Before you use this calculator please visit the about section in the side bar by clicking on the arrow at top left side of this page.')