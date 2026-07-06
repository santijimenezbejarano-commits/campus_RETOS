def calculadora_caloria():
    print("======================================")
    print(" Calculadora de Calorias - Healthech  ")
    print("======================================")

    try:

        proteinas = float(input("ingrese los gramos de proteínas: "))
        carbohidratos = float(input("Ingrese los gramos de carbohidratos: "))
        grasas = float(input("ingrese los gramos de grasas: "))

        if proteinas < 0 or carbohidratos < 0 or grasas < 0:
            print("\n❌ Error: los gramos no pueden ser valorados negativos.")
            return
        
        CAL_PROTEINAS = 4
        CAL_CARBOHIDRATOS = 4
        CAL_GRASAS = 9

        total_cal_proteinas = proteinas * CAL_PROTEINAS
        total_cal_carbohidratos = carbohidratos * CAL_CARBOHIDRATOS
        total_cal_grasas = grasas * CAL_GRASAS

        calorias_totales = total_cal_proteinas + total_cal_carbohidratos + total_cal_grasas

        print("\n-----------------------------------------")
        print("           Resumen Nutricional           ")
        print("-----------------------------------------")
        print(f"• Proteínas:     {total_cal_proteinas:6.1f} kcal ({proteinas}g)")
        print(f"• Carbohidratos: {total_cal_carbohidratos:6.1f} kcal ({carbohidratos}g)")
        print(f"• Grasas:        {total_cal_grasas:6.1f} kcal ({grasas}g)")
        print("-----------------------------------------")
        print(f"🔥 TOTAL DE CALORÍAS: {calorias_totales:.1f} kcal")
        print("=========================================")
    except ValueError:
        print("\n❌ Error: Por favor, ingresa solo valores numéricos válidos.")

if __name__ == "__main__":
    calculadora_caloria()



    

    