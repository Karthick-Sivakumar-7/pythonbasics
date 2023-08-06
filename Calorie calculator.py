def basal_metabolic_rate(height,weight,age,gender):
    if gender=="Male":
        return(10*weight+6.25*height-5*age+5)
    else:
        return(10*weight+6.25*height-5*age-161)

H=float(input("Enter your height in cm:"))
W=float(input("Enter your weight in kgs:"))
A=float(input("Enter your age in yrs:"))
G=input("Specify your gender(Male,Female,Others):")

BMR=basal_metabolic_rate(H,W,A,G)
print("your BMR value is",BMR + "kcal")