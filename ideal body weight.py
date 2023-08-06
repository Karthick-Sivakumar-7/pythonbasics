#create a function
def healthy_weight(height):
    return round((24.9*height**2),2)

#create a input
your_Height=float(input("Enter your height in metres:"))
your_weight=float(input("Enter your weight in kg:"))

#calling the function
ideal_weight=healthy_weight(your_Height)
print("Your healthy weight goal is",ideal_weight)
print("weight(kg) to reduce is",round(your_weight-ideal_weight))

