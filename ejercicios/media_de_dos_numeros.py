def main():
    print("CÁLCULO DE LA MEDIA DE DOS NÚMEROS")
    numero_1 = float(input("Escriba un número:"))
    numero_2 = float(input("Escriba otro número:"))
    
    print(
        f"La media aritmética de {numero_1} y {numero_2} "
        f"es {(numero_1 + numero_2) / 2}"
    )

    
if __name__=="__main__":
    main()
