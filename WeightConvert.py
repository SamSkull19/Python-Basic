weight = int(input("Enter your weight: "))

# specify the unit of weight (Lbs or Kg)
unit = input("(L)Lbs or (K)kg: ")

# If the unit is 'L' (Lbs) and convert it to kilograms
if unit.upper() == 'L':  # Input is converted into uppercase to make it case-insensitive
    convertedWeight = weight * 0.45  # Conversion : 1 pound = 0.45 kg
    print(f"Weight is {convertedWeight : 0.2f} kilos")

# If the unit is not 'L', assume it is 'K' (Kg) and convert it to pounds
else:  
    convertedWeight = weight / 0.45  # Conversion : 1 kg = 1/0.45 pounds
    print(f"Weight is {convertedWeight : 0.2f} pounds")
