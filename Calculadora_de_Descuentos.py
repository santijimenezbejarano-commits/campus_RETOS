def calcular_presio_final():
    print("---bienvenido al Sistema de Descuentos---")

    while True:
        print("\nCategorias Disponibles: Alimentos, Ropa, Electrónica, Hogar")
        Categoria = input("Ingrese la categoria del producto(o escriba 'Salir' para terminar):").strip().capitalize()


        if Categoria == 'Salir':
            print("¡Gracias por usar el sistema! Hasta luego.")
            break

        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
        except ValueError:
            print("Error: Por favor, ingrese un numero valido para el precio.")
            continue

        descuento = 0
        Categoria_valida = True
        
        if Categoria == 'Alimentos':
            descuento = 0.05
        elif Categoria == 'Ropa':
            descuento = 0.10
        elif Categoria =='Electrónica':
            descuento = 0.15
        elif Categoria == 'Hogar':
            descuento = 0.08
        else:
            Categoria_valida = False
            print(f"Error: la categoria '{Categoria}' no existe. intenta de nuevo")

        if Categoria_valida:
            monto_descuento = precio * descuento
            precio_final = precio - monto_descuento

            print(f"\n--- Resumen de Compra ---") 
            print(f"presio original: ${precio:,.2f}")
            print(f"descuento aplicado({descuento*100}%): -${monto_descuento:,.2f}")
            print(f"precio final a pagar: ${precio_final:,.2f}")
            print("-" * 25 )
            
if __name__ =="__main__":
    calcular_presio_final()
