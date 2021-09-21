def main():
    print("PAR E IMPAR (4)")
    error = False

    par = int(input("Escriba un número par: "))

    if par % 2 == 1:
        print("No ha escrito un número par.")
        error = True

    impar = int(input("Escriba un número impar: "))

    if impar % 2 == 0:
        print("No ha escrito un número impar.")
        error = True
        
    if error:
        print("Ejecute de nuevo el programa para volver a intentarlo.")
    else:
        print("¡Gracias por su colaboración!")


if __name__ == "__main__":
    main()
