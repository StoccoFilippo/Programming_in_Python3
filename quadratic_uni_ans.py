import cmath  # Import the cmath module for complex number operations
import math  # Import the math module for mathematical functions
import sys  # Import the sys module for system-specific parameters and functions


# Function to get a valid float input from the user
def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))  # Get user input and convert to float
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")  # Check if zero is not allowed
                x = None
        except ValueError as err:
            print(err)  # Handle invalid input errors
    return x


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")  # Print the equation header

# Get coefficients 'a', 'b', and 'c' from the user
a = get_float("enter a: ", False)  # 'a' cannot be zero
b = get_float("enter b: ", True)   # 'b' can be zero
c = get_float("enter c: ", True)   # 'c' can be zero

x1 = None  # Initialize the first root
x2 = None  # Initialize the second root
simbolb = ""  # Initialize symbol for coefficient 'b'
simbolc = ""  # Initialize symbol for coefficient 'c'

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Calculate roots based on the discriminant
if discriminant == 0:
    x1 = -(b / (2 * a))  # Calculate the root for a single solution
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)  # Calculate the square root for real roots
    else:  # discriminant < 0 (complex roots)
        root = cmath.sqrt(discriminant)  # Calculate the square root for complex roots
    x1 = (-b + root) / (2 * a)  # Calculate the first root
    x2 = (-b - root) / (2 * a)  # Calculate the second root

# Determine the symbols for coefficients 'b' and 'c'
if b > 0:
    simbolb = "+"
if c > 0:
    simbolc = "+"

# Generate the equation based on coefficients and roots
if a == 0:
    equation = ("{3}{0}x{4}{1} = 0"
                " \N{RIGHTWARDS ARROW} x = {2}").format(b, c, x1, simbolb, simbolc)
elif b == 0:
    equation = ("{0}x\N{SUPERSCRIPT TWO}{3}{1} = 0"
                " \N{RIGHTWARDS ARROW} x = {2}").format(a, c, x1, simbolc)
elif c == 0:
    equation = ("{0}x\N{SUPERSCRIPT TWO} {3} {1}x = 0"
                " \N{RIGHTWARDS ARROW} x = {2}").format(a, b, x1, simbolb)
else:
    equation = ("{0}x\N{SUPERSCRIPT TWO} {4} {1}x {5} {2} = 0\N{RIGHTWARDS ARROW} x = {3}").format(a, b, c, x1, simbolb, simbolc)

# Add the second root to the equation if it exists
if x2 is not None:
    equation += " or x = {0}".format(x2)

print(equation)  # Print the final equation
