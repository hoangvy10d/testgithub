def BMI(height,weight):
    return weight/(height**2)
def Classify(bmi):
    if bmi<18.5:
        return "Thin"
    elif bmi<=24.9:
        return"Normal"
    elif bmi<=29.9:
        return"Slightly fat"
    elif bmi<=34.9:
        return ("Obesity level 1")
    elif bmi<39.9:
        return "Obesity level 2"
    else:
        return "Obesity level 3"
def RiskOfDisease(bmi):
    if bmi<18.5:
        return "Low"
    elif bmi<=24.9:
        return "Normal"
    elif bmi<=29.9:
        return "High"
    elif bmi<=34.9:
        return "Very High"
    else:
        return "Danger"
print ("Enter height:")
height=float(input())
print("enter weight:")
weight=float(input())
bmi=BMI(height,weight)
print("Your BMI=",bmi)
print("Classify=",Classify(bmi))
print("Risk of disease = ",RiskOfDisease(bmi))
