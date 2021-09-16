def main():
    print("CONVERTIDOR DE GRADOS FAHRENHEIT A GRADOS CELSIUS")
    fah = float(input("Escriba una temperatura en grados Fahrenheit:"))
    # Convertir de fahrenheit a celsius 
    cel = (fah - 32) / 1.8
    resultado = round (cel,1)
    print (f"{fah} ºF son {resultado} ºC")
if __name__=="__main__":
    main()
