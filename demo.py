import mysql.connector  # Import the MySQL connector library

def connect_to_database():
    """Connects to the MySQL database and returns a connection object."""
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your database host
            user="your_username",  # Replace with your username
            password="your_password",  # Replace with your password
            database="your_database"  # Replace with your database name
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def calculate_bmi(height, weight):
    """Calculate BMI (Body Mass Index)."""
    return weight / (height ** 2)

def assess_bmi_category(bmi):
    """Assess BMI category based on the calculated BMI or retrieved from database."""
    # Option 1: Use calculated BMI (same as original code)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

    # Option 2: Retrieve BMI categories from database (commented out)
    # connection = connect_to_database()  # Uncomment to connect to database
    # if connection:
    #     cursor = connection.cursor()
    #     # Write a query to retrieve BMI categories based on BMI value
    #     # For example:
    #     # cursor.execute("SELECT category FROM bmi_categories WHERE bmi_min <= %s AND bmi_max > %s", (bmi, bmi))
    #     # category = cursor.fetchone()[0]  # Assuming one category per BMI range
    #     # connection.close()
    #     # return category  # Return retrieved category
    # else:
    #     return None  # Return None if database connection fails

def main():
    # Take inputs from the user
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    age = int(input("Enter your age in years: "))
    sex = input("Enter your sex (male/female): ").lower()

    # Calculate BMI
    bmi = calculate_bmi(height, weight)

    # Assess BMI category (choose either option 1 or 2 from assess_bmi_category)
    bmi_category = assess_bmi_category(bmi)

    # Print the result
    print("\nBMI Result:")
    print("BMI:", round(bmi, 2))
    print("BMI Category:", bmi_category)

    # Additional information can be added based on age and sex
    print("\nAdditional Information:")
    print("Age:", age)
    print("Sex:", sex)

if __name__ == "__main__":
    main()
