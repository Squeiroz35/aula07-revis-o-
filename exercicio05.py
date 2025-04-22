novocal="s"
while novocal== "s":
    peso= float (input("digite seu peso:"))
    altura= float (input("digite sua altura:"))
    imc= peso/(altura**2)
    if imc< 18.6:
        print ("abaixo do peso")
    elif imc>=18.6 and imc<=24.9:
        print("peso ideal (parabéns)")
    elif imc >= 25.0 and imc<=29.9:
        print ("levemente acima do peso")
    elif imc >= 30.0 and imc<=34.9:
        print("obesidade grau I")
    elif imc >=35.0 and imc<=39.9:
        print ("obesidade grau II (severa)")
    elif imc >=40:
        print ("obesidade grau III (morbida)")
    input("deseja fazer um novo teste?")