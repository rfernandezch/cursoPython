def main():
    print("PAR E IMPAR 1")

    par = int(input("Escriba un número par:"))
    impar = int(input("Escriba un número impar:"))

    if par % 2 == 1 or impar % 2 == 0:
        print("Uno o más de los valores que ha escrito no son correctos.")
        print("Ejecute de nuevo el programa para volver a intentarlo.")
    else:
        print("¡Gracias por su colaboración!")

if __name__ == "__main__":
    main()
