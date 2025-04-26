peso = int(input("ingrese su peso en Kg "))
altura = float(input("ingrese sul altura en M: "))
IMC = peso / altura **2
if IMC< 18.5:
    print("bajo de peso")
elif IMC >= 18.5 and IMC < 24.5 :
    print("normal")
elif IMC >= 25 and IMC <29.9 :
    print("sobrepeso")
elif IMC >= 30 :
    print("obesidad")
