weight = 85
height = 1.85

bmi = weight / (height ** 2)

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height * height)
rounded_bmi = round(bmi,2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")