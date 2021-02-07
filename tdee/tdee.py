import os

##################
# Function definitions

def calculateBMRforMen(weight, height, age):
    return (10 * weight) + (6.25 * height) - (5 * age) + 5

def calculateBMRforWomen(weight, height, age):
    return (10 * weight) + (6.25 * height) - (5 * age) - 161

def getPALValue(id):
    if(id == 1):
        return 1.2
    elif(id == 2):
        return 1.375
    elif(id == 3):
        return 1.55
    elif(id == 4):
        return 1.725
    elif(id ==5):
        return 1.9
##################

repeat = True

while(repeat == True):
    os.system("clear")
    print("******************************************")
    print("***** WELCOME TO THE TDEE CALCULATOR *****")
    print("******************************************")
    print("ctrl + C to quit")
    print()
    
    weight = input("Please insert your weight in KG: ")
    weight = float(weight)

    height = input("Please insert your height in CM: ")
    height = float(height)

    age = input("Please insert your age: ")
    age = int(age)

    gender = input("Please insert your gender (M/F): ")

    bmr = 0.0
    if(gender == "M" or gender == "m"):
        bmr = calculateBMRforMen(weight, height, age)
    else:
        bmr = calculateBMRforWomen(weight, height, age)

    print()
    print("========================================================================")
    print("\tID\t||Lifestyle")
    print("------------------------------------------------------------------------")
    print("\t1\t||Sedentary (little or no exercise + work a desk job)")
    print("------------------------------------------------------------------------")
    print("\t2\t||Lightly Active (light exercise 1-3 days per week)")
    print("------------------------------------------------------------------------")
    print("\t3\t||Moderately Active (moderate exercise 3-5 days per week)")
    print("------------------------------------------------------------------------")
    print("\t4\t||Very Active (heavy exercise 6-7 days per week)")
    print("------------------------------------------------------------------------")
    print("\t5\t||Extremely Active (very heavy exercise, hard labor job)")
    print("========================================================================")
    print()

    palID = input("Based on the table above, input the ID of the lifestyle which fits yours the best: ")
    palID = int(palID)

    palValue = getPALValue(palID)

    tdee = bmr * palValue

    print()
    print("Your Basal Metabolic Rate(BMR) is: " + str(bmr))
    print("Your Total Daily Energy Expenditure(TDEE) is: " + str(tdee))
    print()
    
    ans = input("Calculate another? (Y/N): ")
    repeat = False if ans == "N" or ans == "n" else True

os.system("clear")
print("Goodbye!")