class MortgageCalculator:
    def __init__(self, loan_amount, interest_rate, loan_term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term

    def calculate_monthly_payment(self):
        monthly_interest_rate = self.interest_rate / 100 / 12
        num_payments = self.loan_term * 12

        monthly_payment = (self.loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

        return monthly_payment


def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to the Mortgage Calculator!")

    loan_amount = get_user_input("Enter the loan amount: ")
    interest_rate = get_user_input("Enter the annual interest rate (%): ")
    loan_term = get_user_input("Enter the loan term (in years): ")

    mortgage_calculator = MortgageCalculator(loan_amount, interest_rate, loan_term)
    monthly_payment = mortgage_calculator.calculate_monthly_payment()

    print("Monthly mortgage payment: $%.2f" % monthly_payment)


if __name__ == "__main__":
    main()