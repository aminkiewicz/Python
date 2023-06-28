def bmi_calc(weight, height):
    # Creating a function that calculates BMI and prints the result.

    bmi = round(weight / (height ** 2), 1)

    if bmi < 18.5:
        print("\nYour BMI is:", bmi, "and your classification is: Underweight. \
        \nThe risk of comorbidities is: Low.")
    elif bmi <= 24.9:
        print("Your BMI is:", bmi, "and your classification is: Normal weight. \
        \nThe risk of comorbidities is: Average.")
    elif bmi <= 29.9:
        print("Your BMI is:", bmi, "and your classification is: Pre-obesity. \
        \nThe risk of comorbidities is: Mildly increased.")
    elif bmi <= 34.9:
        print("Your BMI is:", bmi, "and your classification is: Obesity class I. \
        \nThe risk of comorbidities is: Moderate.")
    elif bmi <= 39.9:
        print("Your BMI is:", bmi, "and your classification is: Obesity class II. \
        \nThe risk of comorbidities is: Severe.")
    else:
        print("Your BMI is:", bmi, "and your classification is: Obesity class III. \
        \nThe risk of comorbidities is: Very Severe.")


# Asking the user for their weight and checking
# if it's in a correct format.

while True:
    weight = float(input("Please enter your weight in kgs: "))

    if weight < 1 or weight > 200:
        print("The weight should be between 1 and 200 kgs.")
        continue
    else:
        break

# Asking the user for their height and checking
# if it's in a correct format.

while True:
    height = float(input("Please enter your height in meters: "))

    if height < 1 or height > 2.50:
        print("The height should be between 1 and 2.50 meters.")
        continue
    else:
        break

bmi_calc(weight, height)