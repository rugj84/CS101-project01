def calculate_mortgage(loan_amount, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = loan_term * 12

    # Calculate the monthly mortgage payment
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    return monthly_payment


def main():
    print("Welcome to the Mortgage Calculator!")

    # Get user inputs
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    loan_term = int(input("Enter the loan term (in years): "))

    # Calculate the monthly payment
    monthly_payment = calculate_mortgage(loan_amount, interest_rate, loan_term)

    # Display the result
    print("Monthly mortgage payment: $%.2f" % monthly_payment)


if __name__ == "__main__":
    main()