height = int(input("Enter your height in cm:"))
age = int(input("Enter your age: "))
adult_present = int(input("enter 1 if an adult is present: "))
minimum_height = 130
minimum_age = 8

adult_required = age < minimum_age
above_minimum_height = height >= minimum_height
print("Adult is required: ",adult_required)
print("Above minimum height: ",above_minimum_height )
print("Allowed on the ride: ",((age>minimum_age) or (adult_present)) and (height>minimum_height))


