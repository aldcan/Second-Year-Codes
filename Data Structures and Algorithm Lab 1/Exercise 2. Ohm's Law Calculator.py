print("Ohm's Law Calculator: \n(V) Voltage \n(I) Current \n(R) Resistance")

# Prompts user for the unit to calculate.
while True:
    unit = input("Select unit to calculate (V, I, or R): ").upper()
    if unit in ["V", "I", "R"]:
        break
    else:
        print("Invalid input. Select V, I, or R only.")

# Performs the calculation for Voltage, Current, or Resistance.
try:   
    if unit == "V":
        I = float(input("Enter the value of current in Amperes: "))
        R = float(input("Enter the value of resistance in Ohms: "))
        V = I * R
        print(f"{V} Volts")  

    elif unit == "I":
        V = float(input("Enter the value of voltage in Volts: "))
        R = float(input("Enter the value of resistance in Ohms: "))
        I = V / R
        print(f"{I} Amperes")  

    elif unit == "R":
        V = float(input("Enter the value of voltage in Volts: "))
        I = float(input("Enter the value of current in Amperes: "))
        R = V / I
        print(f"{R} Ohms")
           
# Handles Zero Division Error.
except ZeroDivisionError:
    print("Zero Division Error. You cannot divide by zero.")
# Handles invalid input values.
except ValueError:
    print("\nInvalid value. Enter valid values only.\n")