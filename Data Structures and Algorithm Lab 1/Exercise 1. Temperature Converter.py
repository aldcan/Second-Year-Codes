print ("Temperature Converter\n")

while True:
    try:
# Prompts user for temperature input.
        temp = float(input("Enter temperature: "))
        break
# Error tracking and loop until input is valid.
    except ValueError:
        print ("Invalid input. Please enter numbers only.")
        
print ("Conversion Type \n(1) Celsius to Fahrenheit \n(2) Fahrenheit to Celsius")
while True:
# Prompts user for the conversion type.
    choice = input("Select conversion type (1 or 2): ")
# Error tracking for the conversion type.
    if choice in ["1", "2"]:
        break 
    else:
        print("Invalid choice. Select 1 or 2 only.")

# Performs the calculations for the celsius to fahrenheit conversion.
if choice == "1":
    fahrenheit = (temp * 9/5) + 32
    print (f"{fahrenheit} °F")
else:
# Performs the calculations for the fahrenheit to celsius conversion.
    celsius = (temp - 32) * 5/9 
    print (f"{celsius} °C")

