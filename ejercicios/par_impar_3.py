def main():
    print("PAR E IMPAR (3)")

    par = int(input("Escriba un número par:"))
    impar = int(input("Escriba un número impar:"))

    if par % 2 == 0 and impar % 2 == 1:
        print("¡Gracias por su colaboración!")
    elif par % 2 == 1 and impar % 2 == 1:
        print("No ha escrito un número par.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")
    elif impar % 2 == 0 and par % 2 == 0:
        print("No ha escrito un número impar.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")
    else:
        print("No ha escrito un número par.")
        print("No ha escrito un número impar.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")

if __name__ == "__main__":
    main()
