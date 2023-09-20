class InvestmentCalculator:
    def __init__(self, monthly_investment, annual_growth_rate, tenure_years, adjusted_inflation_rate=0):
        self.monthly_investment = monthly_investment
        self.annual_growth_rate = annual_growth_rate / 100  # Convert to decimal
        self.tenure_years = tenure_years
        self.adjusted_inflation_rate = adjusted_inflation_rate / 100  # Convert to decimal

    def calculate_sip(self, principal_amount):
        n = 12 * self.tenure_years  # Number of compounding periods (monthly)
        total_invested_amount = principal_amount + (self.monthly_investment * n)
        total_value = principal_amount

        for _ in range(n):
            total_value += self.monthly_investment
            total_value *= (1 + (self.annual_growth_rate / 12))
            total_value -= total_value * self.adjusted_inflation_rate / 12

        profit_on_investment = total_value - total_invested_amount
        total_amount = total_value

        return round(total_invested_amount, 2), round(profit_on_investment, 2), round(total_amount, 2)

    def calculate_one_time_investment(self, one_time_amount):
        total_invested_amount = one_time_amount
        total_value = one_time_amount
        n = 12 * self.tenure_years

        for _ in range(n):
            total_value *= (1 + (self.annual_growth_rate / 12))
            total_value -= total_value * self.adjusted_inflation_rate / 12

        profit_on_investment = total_value - total_invested_amount
        total_amount = total_value

        return round(total_invested_amount, 2), round(profit_on_investment, 2), round(total_amount, 2)

    def calculate_fd_returns(self, principal_amount, fd_interest_rate, fd_tenure_years):
        total_value = principal_amount * (1 + (fd_interest_rate / 100) * (fd_tenure_years))
        interest_earned = total_value - principal_amount

        return round(principal_amount, 2), round(interest_earned, 2), round(total_value, 2)

    def calculate_rd_returns(self, monthly_deposit, rd_interest_rate, rd_tenure_years):
        n = 12 * rd_tenure_years  # Number of compounding periods (monthly)
        total_value = 0

        for _ in range(n):
            total_value += monthly_deposit
            total_value *= (1 + (rd_interest_rate / 100) / 12)

        interest_earned = total_value - (monthly_deposit * n)

        return round((monthly_deposit * n), 2), round(interest_earned, 2), round(total_value, 2)

    @staticmethod
    def calculate_loan_emi(principal_amount, annual_interest_rate, tenure_years):
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        num_monthly_installments = tenure_years * 12

        emi_numerator = principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** num_monthly_installments
        emi_denominator = ((1 + monthly_interest_rate) ** num_monthly_installments) - 1
        emi = emi_numerator / emi_denominator

        return round(emi, 2), num_monthly_installments

    @staticmethod
    def calculate_loan_interest(principal_amount, emi, num_monthly_installments, current_month, annual_interest_rate):
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        remaining_principal = principal_amount
        for i in range(current_month):
            interest_payment = remaining_principal * monthly_interest_rate
            remaining_principal -= (emi - interest_payment)
        return round(interest_payment, 2)

# Input values for SIP, One-Time Investment, FD, RD, and Loan Calculator
sip_monthly_investment = 1000  # Monthly investment amount
annual_growth_rate = 12  # Annual growth rate (in percentage)
tenure_years = 10  # SIP tenure in years
adjusted_inflation_rate = 0  # Adjusted inflation rate (in percentage)
sip_principal_amount = 1000  # Initial principal amount
one_time_investment_amount = 10000  # One-time investment amount
fd_principal_amount = 100000  # FD principal amount (₹100,000)
fd_interest_rate = 7  # FD annual interest rate (7%)
fd_tenure_years = 5  # FD tenure in years (5 years)
rd_monthly_deposit = 5000  # Monthly RD deposit amount (₹5,000)
rd_interest_rate = 6  # RD annual interest rate (6%)
rd_tenure_years = 3  # RD tenure in years (3 years)
loan_principal_amount = 2500000  # Loan principal amount (₹2,500,000)
loan_annual_interest_rate = 8  # Loan annual interest rate (8%)
loan_tenure_years = 20  # Loan tenure in years (20 years)

# Create calculators for SIP, One-Time Investment, FD, RD, and Loan
sip_calculator = InvestmentCalculator(sip_monthly_investment, annual_growth_rate, tenure_years, adjusted_inflation_rate)
one_time_calculator = InvestmentCalculator(0, annual_growth_rate, tenure_years, adjusted_inflation_rate)
fd_calculator = InvestmentCalculator(0, 0, 0)  # FD calculator doesn't require growth or inflation
rd_calculator = InvestmentCalculator(0, 0, 0)  # RD calculator doesn't require growth or inflation
loan_calculator = InvestmentCalculator(0, 0, 0)  # Loan calculator doesn't require growth or inflation

# Calculate SIP results
sip_invested_amount, sip_profit, sip_total_amount = sip_calculator.calculate_sip(sip_principal_amount)

# Calculate One-Time Investment results
one_time_invested_amount, one_time_profit, one_time_total_amount = one_time_calculator.calculate_one_time_investment(one_time_investment_amount)

# Calculate FD returns
fd_invested_amount, fd_interest_earned, fd_total_value = fd_calculator.calculate_fd_returns(fd_principal_amount, fd_interest_rate, fd_tenure_years)

# Calculate RD returns
rd_invested_amount, rd_interest_earned, rd_total_value = rd_calculator.calculate_rd_returns(rd_monthly_deposit, rd_interest_rate, rd_tenure_years)

# Calculate Loan EMI
loan_emi, num_monthly_installments = loan_calculator.calculate_loan_emi(loan_principal_amount, loan_annual_interest_rate, loan_tenure_years)



# Output SIP results
print("\nSIP Total Invested Amount:", sip_invested_amount)
print("SIP Profit on Investment:", sip_profit)
print("SIP Total Amount:", sip_total_amount)

# Output One-Time Investment results
print("\nOne-Time Investment Total Invested Amount:", one_time_invested_amount)
print("One-Time Investment Profit on Investment:", one_time_profit)
print("One-Time Investment Total Amount:", one_time_total_amount)

# FD Details
print("\nFD Total Invested Amount:", fd_invested_amount)
print("FD Interest Earned:", fd_interest_earned)
print("FD Total Amount:", fd_total_value)

# RD Details
print("\nRD Total Invested Amount:", rd_invested_amount)
print("RD Interest Earned:", rd_interest_earned)
print("RD Total Amount:", rd_total_value)

# Calculate and display Loan EMI and Interest Paid on a Monthly Basis
print("\nLoan EMI:", loan_emi)
print("Loan Tenure (in months):", num_monthly_installments)
print("\nMonth\tEMI\tInterest Paid")

for month in range(1, num_monthly_installments + 1):
    interest_paid_monthly = loan_calculator.calculate_loan_interest(loan_principal_amount, loan_emi, num_monthly_installments, month, loan_annual_interest_rate)
    print(f"{month}\t{loan_emi}\t{interest_paid_monthly}")
