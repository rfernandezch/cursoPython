def main():
    print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
    seg = int(input("Escriba una cantidad de segundos:"))
    
    min = seg // 60
    seg_resultado = seg % 60

    print (f"{seg} segundos son {min} minutos y {seg_resultado} segundos")


if __name__=="__main__":
    main()
