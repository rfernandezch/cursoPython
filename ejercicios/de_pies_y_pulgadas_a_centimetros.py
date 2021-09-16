def main():
    print("CONVERTIDOR DE PIES Y PULGADAS A CENTÍMETROS")
    pies = int(input("Escriba una cantidad de pies:"))
    pulgadas = int(input("Escriba una cantidad de pulgadas:"))
    
   
    # Convertir de pies a centímetros
    centimetros = (pies * 12 + pulgadas) * 2.54
    
    print (f"{pies} pies y {pulgadas} pulgadas son {centimetros} cm")

if __name__=="__main__":
    main()
