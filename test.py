import os

# Example 1: Hardcoded sensitive information
def connect_to_database():
    # Security issue: Hardcoded credentials
    username = "admin"
    password = "password123"  
    print(f"Connecting to database with username: {username} and password: {password}")

# Example 2: Using a predictable temporary file
def create_temp_file():
    # Security issue: Using a hardcoded temp file path
    temp_file_path = "/tmp/my_temp_file.txt"  
    with open(temp_file_path, "w") as temp_file:
        temp_file.write("This is a temporary file.")
    print("Temporary file created:", temp_file_path)

# Example 3: Unused variable
def calculate_sum(a, b):
    result = a + b
    unused_variable = "I am not used"  # Bug: Unused variable
    return result

# Example 4: Inefficient string concatenation in a loop
def inefficient_concatenation():
    concatenated_string = ""
    for i in range(1000):
        concatenated_string += str(i) + " "  # Performance issue: Inefficient string concatenation
    return concatenated_string

# Example 5: SQL Injection vulnerability
def find_user(username):
    # Security issue: SQL injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    print("Executing query:", query)

# Example 6: Potential divide by zero
def divide_numbers(a, b):
    # Bug: Possible division by zero error
    return a / b

# Example 7: Redundant if statement
def check_value(value):
    # Bug: Redundant if statement
    if value == 1:
        return True
    if value == 1:
        return True  # Redundant

if __name__ == "__main__":
    connect_to_database()
    create_temp_file()
    print("Sum:", calculate_sum(5, 10))
    print("Concatenated string:", inefficient_concatenation())
    find_user("admin'; DROP TABLE users; --")  # Intentional SQL Injection example
    print("Division result:", divide_numbers(10, 0))  # Intentional divide by zero
    print("Check value:", check_value(1))
