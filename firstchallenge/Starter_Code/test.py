new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
} 
annual_discount_rate = 0.2
future_value = 1000
remaining_months = 12

new_present_value = future_value / (1+ (annual_discount_rate / 12)) ** remaining_months


def new_present_value(x):
    return new_present_value

print(f"The present value of the loan is: {new_present_value: .2f}")
