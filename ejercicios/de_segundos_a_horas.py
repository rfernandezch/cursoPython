def main():
    print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
    seg = int(input("Escriba una cantidad de segundos:"))
    
    hor = seg // 3600
    seg_1 = seg % 3600
    min = seg_1 // 60
    seg_resultado = seg_1 % 60
   
    print (f"{seg} segundos son {hor} horas, {min} minutos y {seg_resultado} segundos")


if __name__=="__main__":
    main()
