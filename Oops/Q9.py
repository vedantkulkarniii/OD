# *9. Financial Calculator *
# 📌 Question:
# Build financial calculator: Use try-catch blocks to handle potential exceptions, such as dividing by zero during interest rate calculations, null pointers for uninitialized data, and custom exceptions for invalid user inputs.

# 📖 Explanation:
# Exception handling ensures safe execution


try:
    a = int(input("Enter amount: "))
    b = int(input("Enter rate: "))

    if b == 0:
        raise ValueError("Rate cannot be zero")

    print("Result:", a/b)

except ValueError as e:
    print("Error:", e)