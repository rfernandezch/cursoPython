def main():
    print("PAR E IMPAR (2)")

    par = int(input("Escriba un número par:"))
    
    if par % 2 == 0: 
        impar = int(input("Escriba un número impar:"))
        if impar % 2 == 1:
            print("¡Gracias por su colaboración!")
        else:
            print("No ha escrito un número impar.")
            print("Ejecute de nuevo el programa para volver a intentarlo.")
    else:
        print("No ha escrito un número par.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")

if __name__ == "__main__":
    main()
