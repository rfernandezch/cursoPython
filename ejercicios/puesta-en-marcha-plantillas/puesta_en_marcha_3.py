def main():

    print("PUESTA EN MARCHA 3")

    print("Piense un número de 1 a 4.")
    print("Conteste S (sí) o N (no) a mis preguntas.")

    primera = input("¿El número pensado es mayor que 2? ")
    if primera == "S":
        segunda = input("¿El número pensado es mayor que 3? ")

        if segunda == "S":
            print("El número pensado es 4.")
        else:
            print("El número pensado es 3")
    else:
        segunda = input("¿El número pensado es mayor que 1? ")

        if segunda == "S":
            print("El número pensado es 2.")
        else:
            print("El número pensado es 1.")
    print("¡Hasta la próxima!")


if __name__ == "__main__":

    main()
