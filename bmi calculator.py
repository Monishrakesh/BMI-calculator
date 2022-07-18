name = input("Enter your name : ")
height_m = float(input("Enter your height in m : "))
weight_kg = float(input("Enter your weight in kg : "))
bmi = weight_kg / (height_m ** 2)

print("Name : " + str(name))
print("Height : " + str(height_m))
print ("Weight : " + str(weight_kg))
print("Your BMI is" + str(bmi))

if bmi < 18.5:
    print("Your are Underweight")    
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are normal weight")    
elif bmi >= 25 and bmi <=29.9:
    print("You are Overweight")   
else:
    if bmi >= 30:
        print("You are Obese")