import datetime
def validate_input(number, base):
    # Function to validate if the input number is valid for the specified base
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in number:
        if char.upper() not in valid_chars[:base]:
            return False
    return True
def convert_base(number, from_base, to_base):
    # Function to convert a number from one base to another
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert to base 10 first
    base_10_value = 0
    power = 0
    for digit in reversed(str(number).upper()):
        base_10_value += valid_chars.index(digit) * (from_base ** power)
        power += 1

    # Convert to the desired base
    converted_number = ''
    while base_10_value:
        remainder = base_10_value % to_base
        converted_number = valid_chars[remainder] + converted_number
        base_10_value //= to_base

    return converted_number


# Take user input for the number and bases
number = input("Enter the number to convert: ")
from_base = int(input("Enter the base of the given number: "))
to_base = int(input("Enter the base to convert to: "))

# Validate input
if not validate_input(number, from_base):
    print("Error: Invalid input for the specified base")
else:
    # Perform the conversion
    converted_number = convert_base(number, from_base, to_base)

    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Print the conversion result
    print(f"Conversion of {number} from base {from_base} to base {to_base}: {converted_number}")
    print(f"Current date and time: {current_datetime}")