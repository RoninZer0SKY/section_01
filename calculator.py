


while True:
 print("Terület")
 bemenet = float(input("Hossz:"))
 bemenet2 = float(input("Magasság:"))
 bemenet3 = float(bemenet)*float(bemenet2)
 print("A terület =", bemenet3)

 dolog4 = 24
 dolog2 = 26.6666667
 dolog = 2.4
 dolog3 = 1.3333332
 dolog10 = 66.6666668
 dolog11 = 44.44444444

 penz = 15
 penz2 = 5

 bemenet4 = float(bemenet3) / float(dolog)
 bemenet5 = float(bemenet3) * float(dolog2)
 bemenet6 = float(dolog3) * float(bemenet3)
 bemenet7 = float(bemenet3) * float(dolog4)
 bemenet8 = float(bemenet3) * float(dolog10)
 bemenet9 = float(bemenet3) * float(dolog11)

 bevetel = float(bemenet3) * float(penz)
 bevetel2 = float(bemenet3) * float(penz2)
 print("A végeredmény =", bemenet4)

 print("Végeredmény kerekítve =", (round(bemenet4, 0)))

 print(bemenet5, "tégla fér", bemenet3, "négyzetméterre.")
 print(bemenet6, "tégla veszteség", bemenet3, "négyzetméterre")
 print(bemenet7, "egész tégla fér", bemenet3, "négyzetméterre")
 print("------------------------------------------------------")
 print(bemenet8, "külső szél jut", bemenet3, "négyzetméterre")
 print(bemenet9, "belső szél jut", bemenet3, "négyzetméterre" )
 print("------------------------------------------------------")
 print("Bevétel:")
 print(bevetel, "€ kapok a belső részekért")
 print(bevetel2, "€ kapok a külső részekért")
 print("------------------------------------------------------")













