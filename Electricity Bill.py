# Q13.
# Create a function that calculates electricity bills based on unit consumption.

def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 5      # $5 per unit for first 100 units
    elif units <= 300:
        bill = (100 * 5) + ((units - 100) * 7)  # $7 per unit next
    else:
        bill = (100 * 5) + (200 * 7) + ((units - 300) * 10) # $10 beyond
    return bill


consumed_units = 250
total_bill = calculate_electricity_bill(consumed_units)
print(f"Your bill for {consumed_units} units is: ${total_bill}")
