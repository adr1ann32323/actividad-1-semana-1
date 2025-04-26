año = int(input("ingresa un año: "))
if año %4 !=0:
    print("no es año biciesto")
elif año %4 ==0 and año %100 !=0 :
    print("es bisiesto")
elif año %4 ==0 and año %400 !=0 :
    print("no es bisiesto")
elif año %4 ==0 and año %400 ==0 :
    print("es bisiesto")
