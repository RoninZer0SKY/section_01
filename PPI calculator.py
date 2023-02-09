import math

# MY OWN PPI CALCULATOR HEHEHEHEH XD

while True:
 bemenet = float(input("Vertical pixels: " ))
 bemenet2 = float(input("Horizontal pixels: "))
 bemenet7 = float(input("Size of the phone (inch): "))


 bemenet4 = float(bemenet)*float(bemenet) #négyzetre emelve
 bemenet5 = float(bemenet2)*float(bemenet2)

 bemenet3 = float(bemenet4)+float(bemenet5)


 bemenet6 = math.sqrt(bemenet3)

 bemenet8 = bemenet6/bemenet7


 print("Total number of pixels:", bemenet3)
 print("Root subtractioned pixels:", round(bemenet6))
 print("Final result of PPI:", round(bemenet8))



