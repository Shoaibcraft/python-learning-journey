def main():
    # Get the cost of the meal and convert the string input to a float
    dollars = dollars_to_float(input("How much was the meal? "))
    # Get the tip percentage and convert it to a decimal (e.g., 15% -> 0.15)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    # Display the final tip amount formatted to 2 decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the '$' sign and convert the string to a float
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Remove the '%' sign, convert to float, and divide by 100 to get the decimal
    return float(p.replace("%", ""))/100


main()
