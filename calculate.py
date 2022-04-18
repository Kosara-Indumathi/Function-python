# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def function(weight,height):
    i=0
    bmi=weight/height
    if bmi<=18.5:
        return "under weight"
    elif bmi <= 25.0 :
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    i=i+1
weight=int(input("enter the weight"))
height=int(input("enter the height"))
print(function(weight,height))
