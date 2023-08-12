#segunda parte
n=0
fecha=""
tb=5
costtal=0.0

n=int(input("ingresa la cantidad de boletas a comprar?"))
fecha=input("la boleta es para fin de semana(si o no)")
if fecha=='si':
 costtal=tb*1.20
else:
 costtal=tb
    #Proceso segun eleccion de palco:
palco=input("escribe A,B,C segun el palco: ")
if palco=='A':
 costtal+=tb*.1 #costtal= costtal +tb*.1
elif palco=='B':
 costtal+=tb*.05
#proceso de descuentos por cantidad de boletas
if n>=5 and n<=10:
 costtal=costtal*.9
print("el costo total a pagar: ", round(costtal*n, 2)) #PARA REDONDIAR LA CIFRA
