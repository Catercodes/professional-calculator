import math
import statistics


class Calculator:
    def __init__(self):
        self.memory = 0

    # Basic arithmetic
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error: Division by zero")
        return x / y

    # Trigonometric functions
    def sin(self, x):
        return math.sin(math.radians(x))

    def cos(self, x):
        return math.cos(math.radians(x))

    def tan(self, x):
        return math.tan(math.radians(x))

    def asin(self, x):
        if x < -1 or x > 1:
            raise ValueError("Error: Input must be between -1 and 1")
        return math.degrees(math.asin(x))

    def acos(self, x):
        if x < -1 or x > 1:
            raise ValueError("Error: Input must be between -1 and 1")
        return math.degrees(math.acos(x))

    def atan(self, x):
        return math.degrees(math.atan(x))

    # Hyperbolic functions
    def sinh(self, x):
        return math.sinh(x)

    def cosh(self, x):
        return math.cosh(x)

    def tanh(self, x):
        return math.tanh(x)

    # Logarithmic functions
    def log(self, x):
        if x <= 0:
            raise ValueError("Error: Invalid input for logarithm")
        return math.log10(x)

    def ln(self, x):
        if x <= 0:
            raise ValueError("Error: Invalid input for natural logarithm")
        return math.log(x)

    # Power and root functions
    def power(self, x, y):
        return math.pow(x, y)

    def sqrt(self, x):
        if x < 0:
            raise ValueError(
                "Error: Cannot calculate square root of a negative number")
        return math.sqrt(x)

    # Conversion functions
    def deg_to_rad(self, x):
        return math.radians(x)

    def rad_to_deg(self, x):
        return math.degrees(x)

    # Factorial
    def factorial(self, x):
        if x < 0 or not isinstance(x, int):
            raise ValueError(
                "Error: Factorial is only defined for non-negative integers")
        return math.factorial(x)

    # Statistical functions
    def mean(self, numbers):
        return statistics.mean(numbers)

    def median(self, numbers):
        return statistics.median(numbers)

    def std_dev(self, numbers):
        return statistics.stdev(numbers)

    # Memory functions
    def memory_store(self, x):
        self.memory = x

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    # Advanced functions with steps
    def quadratic_solver(self, a, b, c):
        steps = [
            f"Quadratic equation: {a}x² + {b}x + {c} = 0",
            f"Step 1: Calculate the discriminant (b² - 4ac)",
            f"discriminant = {b}² - 4({a})({c})"
        ]
        discriminant = b**2 - 4 * a * c
        steps.append(f"discriminant = {discriminant}")

        if discriminant < 0:
            steps.append(
                "Step 2: The discriminant is negative, so there are no real roots.")
            steps.append("Result: No real roots")
        elif discriminant == 0:
            steps.append(
                "Step 2: The discriminant is zero, so there is one real root.")
            steps.append("Step 3: Calculate the root using x = -b / (2a)")
            x = -b / (2 * a)
            try:
                if choice == '1':
                    # Your logic for choice 1
                elif choice == '2':
                    #Your logic for choice 2
                elif choice == '3':
                    # Your logic for choice 3
                elif choice == '4':
                    # Your logic for choice 4
                elif choice == '5':
                    # Complete the logic for choice 5
                    print("1. [Operation for choice 5]")
                else:
                    print("Invalid choice")


except Exception as e:
    print(f"An error occurred: {e}")
s.append(f"x = -({b}) / (2({a})) = {x}")
   steps.append(f"Result: One root: {x}")
       else:
            steps.append(
                "Step 2: The discriminant is positive, so there are two real roots.")
            steps.append(
                "Step 3: Calculate the roots using the quadratic formula:")
            steps.append("x = (-b ± √(b² - 4ac)) / (2a)")
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            steps.append(f"x₁ = (-({b}) + √{discriminant}) / (2({a})) = {x1}")
            steps.append(f"x₂ = (-({b}) - √{discriminant}) / (2({a})) = {x2}")
            steps.append(f"Result: Two roots: {x1} and {x2}")

            return "\n".join(steps)

    def log_with_steps(self, x, base=10):
        steps = [
            f"Calculate log{base}({x})",
            f"Step 1: Check if the input is valid (x > 0)"
            ]
        if x <= 0:
            steps.append(f"Error: {x} is not a valid input for logarithm")
            return "\n".join(steps)

        steps.append(f"Step 2: Calculate the logarithm")
        if base == 10:
            result = math.log10(x)
            steps.append(f"Using the log10() function: log10({x}) = {result}")
        elif base == math.e:
            result = math.log(x)
            steps.append(f"Using the natural log function: ln({x}) = {result}")
        else:
            result = math.log(x) / math.log(base)
            steps.append(f"Using the change of base formula:")
            steps.append(f"log{base}({x}) = ln({x}) / ln({base})")
            steps.append(f"           = {math.log(x)} / {math.log(base)}")
            steps.append(f"           = {result}")

        steps.append(f"Result: log{base}({x}) = {result}")
        return "\n".join(steps)

    def trig_with_steps(self, angle, function):
        steps = [
            f"Calculate {function}({angle}°)",
            f"Step 1: Convert the angle to radians",
            f"{angle}° * (π / 180°) = {math.radians(angle)} radians"
        ]
        rad_angle = math.radians(angle)

        unit_circle = {
            0: (1, 0), 30: (math.sqrt(3) /2, 1/2), 45: (math.sqrt(2)/2, math.sqrt(2)/2),
            60: (1 /2, math.sqrt(3)/2), 90: (0, 1), 180: (-1, 0), 270: (0, -1)
        }

        if angle in unit_circle:
            x, y = unit_circle[angle]
            steps.append(
    f"Step 2: Identify the point on the unit circle for {angle}°: ({x}, {y})")
            if function == 'sin':
                result = y
                steps.append(f"Step 3: sin({angle}°) is the y-coordinate: {y}")
            elif function == 'cos':
                result = x
                steps.append(f"Step 3: cos({angle}°) is the x-coordinate: {x}")
            elif function == 'tan':
                result = y / x if x != 0 else "undefined"
                steps.append(
    f"Step 3: tan({angle}°) is y/x: {y}/{x} = {result}")
        else:
            if function == 'sin':
                result = math.sin(rad_angle)
                steps.append(f"Step 2: Calculate using math.sin(): {result}")
            elif function == 'cos':
                result = math.cos(rad_angle)
                steps.append(f"Step 2: Calculate using math.cos(): {result}")
            elif function == 'tan':
                result = math.tan(rad_angle)
                steps.append(f"Step 2: Calculate using math.tan(): {result}")

        steps.append(f"Result: {function}({angle}°) = {result}")
        return "\n".join(steps)

    def matrix_operation_with_steps(self, mat1, mat2, operation):
        steps = [f"Perform matrix {operation}:"]
        steps.append("Matrix 1:")
        steps.extend([" ".join(map(str, row)) for row in mat1])
        steps.append("Matrix 2:")
        steps.extend([" ".join(map(str, row)) for row in mat2])

        if operation == "addition":
            if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
                return "Error: Matrices must have the same dimensions for addition."
            result = []
            steps.append("Step 1: Add corresponding elements")
            for i in range(len(mat1)):
                row = []
                step = []
                for j in range(len(mat1[0])):
                    sum_val = mat1[i][j] + mat2[i][j]
                    row.append(sum_val)
                    step.append(f"{mat1[i][j]} + {mat2[i][j]} = {sum_val}")
                result.append(row)
                steps.append(" | ".join(step))
        elif operation == "multiplication":
            if len(mat1[0]) != len(mat2):
                return "Error: Number of columns in first matrix must equal number of rows in second matrix."
            result = [[0 for _ in range(len(mat2[0]))]
                                        for _ in range(len(mat1))]
            steps.append(
                "Step 1: Multiply rows of Matrix 1 with columns of Matrix 2")
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    step = []
                    for k in range(len(mat2)):
                        result[i][j] += mat1[i][k] * mat2[k][j]
                        step.append(f"{mat1[i][k]} * {mat2[k][j]}")
                    steps.append(f"Element [{i +1},{j +1}]: {' + '.join(step)} = {result[i][j]}")

        steps.append("Result:")
        steps.extend([" ".join(map(str, row)) for row in result])
        return "\n".join(steps)

    def derivative_with_steps(self, coefficient, exponent):
        steps = [f"Calculate the derivative of {coefficient}x^{exponent}"]
        if exponent == 0:
            steps.append("Step 1: The derivative of a constant is 0")
            result = 0
        else:
            steps.append(
                "Step 1: Apply the power rule: d/dx(ax^n) = a * n * x^(n-1)")
            new_coefficient = coefficient * exponent
            new_exponent = exponent - 1
            steps.append(
    f"Step 2: Multiply the coefficient by the exponent: {coefficient} * {exponent} = {new_coefficient}")
            steps.append(
    f"Step 3: Reduce the exponent by 1: {exponent} - 1 = {new_exponent}")
            if new_exponent == 0:
                result = f"{new_coefficient}"
            elif new_exponent == 1:
                result = f"{new_coefficient}x"
            else:
                result = f"{new_coefficient}x^{new_exponent}"
        steps.append(f"Result: The derivative is {result}")
        return "\n".join(steps)


def get_numbers_list():
    numbers = input("Enter numbers separated by spaces: ").split()
    return [float(num) for num in numbers]


def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter {cols} values for row {i +1}, separated by spaces: ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} values, but got {len(row)}")
        matrix.append(row)
    return matrix


def main():
    calc = Calculator()
    while True:
        print("\nAdvanced Engineering Calculator")
        print("1. Basic Arithmetic")
        print("2. Trigonometric Functions (with steps)")
        print("3. Hyperbolic Functions")
        print("4. Logarithmic Functions (with steps)")
        print("5. Power and Root")
        print("6. Conversions")
        print("7. Factorial")
        print("8. Quadratic Equation Solver (with steps)")
        print("9. Statistical Functions")
        print("10. Memory Functions")
        print("11. Matrix Operations (with steps)")
        print("12. Basic Derivative (with steps)")
        print("13. Exit")

        choice = input("Enter choice (1-13): ")

        try:
            if choice == '1':
                print("1. Add  2. Subtract  3. Multiply  4. Divide")
                op = input("Choose operation: ")
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                if op == '1':
                    print("Result:", calc.add(x, y))
                elif op == '2':
                    print("Result:", calc.subtract(x, y))
                elif op == '3':
                    print("Result:", calc.multiply(x, y))
                elif op == '4':
                    print("Result:", calc.divide(x, y))
                else:
                    print("Invalid Oparation.")

            elif choice == '2':
                print("1. sin  2. cos  3. tan")
                op = input("Choose operation: ")
                angle = float(input("Enter angle in degrees: "))
                if op == '1':
                    print(calc.trig_with_steps(angle, 'sin'))
                elif op == '2':
                    print(calc.trig_with_steps(angle, 'cos'))
                elif op == '3':
                    print(calc.trig_with_steps(angle, 'tan'))
                else:
                    print("Invalid Operation.")

            elif choice == '3':
                print("1. sinh  2. cosh  3. tanh")
                op = input("Choose operation: ")
                x = float(input("Enter number: "))
                if op == '1':
                    print("Result:", calc.sinh(x))
                elif op == '2':
                    print("Result:", calc.cosh(x))
                elif op == '3':
                    print("Result:", calc.tanh(x))
                else:
                    print("Invalid Operation.")

            elif choice == '4':
                print("1. log (base 10)  2. ln (natural log)  3. Custom base")
                op = input("Choose operation: ")
                x = float(input("Enter number: "))
                if op == '1':
                    print(calc.log_with_steps(x, 10))
                elif op == '2':
                    print(calc.log_with_steps(x, math.e))
                elif op == '3':
                    base = float(input("Enter the base: "))
                    print(calc.log_with_steps(x, base))
                else:
                    print("Invalid Operation")

            elif choice == '5':
                print("1 . Power 2.Root")
                op = input("Choose Operation: ")
                x = float(input("Enter the base number: "))
                y = float(input("Enter the exponent/root: "))
                if op == '1':
                    print (f" Result: {x} ^ {y} = {calc.power(x, y)}")
                elif op == '2':
                    print (f" Result: {x} ^ {y} = {calc.root(x, y)}")
                else:
                    print("Invalid Operation.")
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
            except Exception as e:
                print(f"An error occurred: {e}")
