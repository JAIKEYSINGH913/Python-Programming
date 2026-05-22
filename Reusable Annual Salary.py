# Q14
# A company wants a reusable function to calculate annual salary from monthly salary.

def calculate_annual_salary(monthly_salary):
    annual_salary = monthly_salary * 12
    return annual_salary


monthly = 4500
yearly = calculate_annual_salary(monthly)
print(f"A monthly salary of ${monthly} equals an annual salary of ${yearly}.")
