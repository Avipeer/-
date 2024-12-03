
pie=3.14
shape=input("Enter the shape you need: ")
if shape=="triangle":
    edge1=float(input("Enter edge 1 length in cm: "))
    edge2=float(input("Enter edge 2 length in cm: "))
    area=(edge1*edge2)/2
    hypotenuse=(edge1 ** 2 + edge2 ** 2) ** 0.5
    perimeter=edge1+edge2+hypotenuse
elif shape=="circle":
    radius=float(input("Enter radius length in cm: "))
    area=pie*radius**2
    perimeter=pie*radius*2
elif shape=="trapeze":
    short_edge=float(input("Enter short edge length in cm: "))
    long_edge=float(input("Enter long edge length in cm: "))
    height=float(input("Enter trapeze h: "))
    area=(short_edge+long_edge)*height/2
    side=((long_edge-short_edge)*2+height2)*0.5
    perimeter=short_edge+long_edge+2*side
elif shape=="square":
    edge=float(input("Enter edge length in cm: "))
    area=edge**2
    perimeter=edge*4
price=area*(2/perimeter)
print("The", shape, "you want will cost", price, "$")