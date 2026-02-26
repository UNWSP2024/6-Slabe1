# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
def county_sales_tax(sales):
    result = sales * 0.05
    return result

def state_sales_tax(sales):
    result = sales * 0.025
    return result

def check_input(input):
    if input <= 0:
        return None
    else:
        return input

def main():
    sales = check_input(float(input("What is your sales for this month?  ")))
    county = county_sales_tax(sales)
    state = state_sales_tax(sales)
    print("County sales tax:", county)
    print("State sales tax:", state)
    total = county + state
    print("Total sales tax:", total)

main()

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program