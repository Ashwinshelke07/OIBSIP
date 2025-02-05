# """Calculate BMI given weight in kg and height in meters."""

def calculate_bmi(weight, height):
   
    return weight / (height ** 2)

def classify_bmi(bmi):
   
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()