print("===============this programme calculates bmi====================")
weight = float(input("enter weight in kg(e.g :52kg) "))
hieght = float(input("enter hieght in meters(e.g :1.8 meters) "))
BMI = weight/(hieght*hieght)

if (BMI <= 18.5):
    print("underweight")
elif (BMI > 18.5 and BMI < 24.9):
    print("print normal weight")
elif (BMI > 24.9 and BMI < 29.9):
    print("print over weight")
else:
    print("obesity")
