def gestionar_imventario():
    invenatario = []

    while True:
        print("\n=========================================")
        print("      🧰 GESTOR DE INVENTARIO V1.0       ")
        print("=========================================")
        print("1. Añadir ítem")
        print("2. Eliminar ítem")
        print("3. Mostrar inventario completo")
        print("4. Verificar si existe un ítem")
        print("5. Salir")
        print("=========================================")
        
        opcion = input("selecciona una opción (1-5): ").strip()

        if opcion == "1":
            nuevo_item =input("\n📝 Introduce el nombre del item a añadir: ").strip()

            if nuevo_item == "":
                print("❌ El nombre del ítem no puede estar vacío.")
            elif nuevo_item.lower() in [ item.lower() for item in invenatario]:
                print(f"⚠️ ¡El ítem '{nuevo_item}' ya existe en el inventario! No se permiten duplicados.")
            else:
                invenatario.append(nuevo_item)
                print(f"✅ '{nuevo_item}' ha sido añadido con éxito.")
        
        elif opcion == "2":
            if not invenatario:
                print ("\n introduce el nombre del item a eliminar: ").strip()
                continue
            item_a_eliminar = input("\n🗑️ Introduce el nombre del ítem a eliminar: ").strip()

            encontrado = False
            for item in invenatario:
                if item.lower() == item_a_eliminar.lower():
                    invenatario.remove(item)
                    print(f"💥 '{item}' ha sido eliminado del inventario.")
                    encontrado = True
                    break
            if not encontrado:
                print(f"❌ El ítem '{item_a_eliminar}' no se encuentra en el inventario.")

        elif opcion == "3":
            print("\n-----------------------------------------")
            print("         📦 ÍTEMS EN INVENTARIO          ")
            print("-------------------------------------------")
            if not invenatario:
                print("   [ El inventario está vacío ]")
            else:
                for indice, item in enumerate(invenatario, start=1):
                    print(f"{indice}. {item}")
            print("-------------------------------------------")

        elif opcion == "4":
            item_a_buscar = input("\n ¿Què item deseas buscar?: ").strip()

            if item_a_buscar.lower() in [item.lower() for item in invenatario]:
                print(f"¡Sí!'{item_a_buscar}' està en el invetario.")
            else:
                print(f"No se encontró '{item_a_buscar}en el inventario.")
        
        elif opcion == "5":
            print("\n Guardando datos... ¡Gracias por usar el Gestor de Inventario!")

        else:
            print("\n Opciòn no valida. Por favor, selecione un nùmero del 1 al 5.")

if __name__ =="__main__":
    gestionar_imventario()