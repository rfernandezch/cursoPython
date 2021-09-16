def main():
    print("CONVERTIDOR DE GRADOS CELSIUS A GRADOS FAHRENHEIT")
    cel = float(input("Escriba una temperatura en grados Celsius:"))
    # Convertir de celsius a fahrenheit
    fah = 1.8 * cel + 32
    print (f"{cel} ºC son {fah} ºF")
if __name__=="__main__":
    main()
