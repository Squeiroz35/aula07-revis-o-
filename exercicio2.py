novaop="sim"
while novaop == "sim":
    n1= int(input("digite um numero:"))
    if n1%2== 1 and n1 <0 :
        print ("o numero impar e negativo")
    elif n1%2== 0 and n1 >=00:
        print ("o numero é par e positivo")
    elif n1%2== 1 and n1 >0:
        print ("o numero é impar e positivo")
    elif n1%2== 0 and n1 <0:
        print ("o numero é par e negativo")
    novaop=input (" deseja fazer outra operação?")