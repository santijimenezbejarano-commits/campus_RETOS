import json
import os

# Nombre del archivo donde se guardarán los productos
ARCHIVO_DATOS = "productos.json"

def cargar_productos():
    """Carga los productos desde el archivo JSON. Si no existe, devuelve una lista vacía."""
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("Error al leer el archivo de datos. Se iniciará con una lista vacía.")
            return []
    return []

def guardar_productos(productos):
    """Guarda la lista de productos en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=4, ensure_ascii=False)
    except IOError:
        print("Error: No se pudieron guardar los datos en el archivo.")

def agregar_producto(productos):
    """Solicita los datos de un nuevo producto y lo agrega a la lista."""
    print("\n--- AGREGAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()
    
    # Validar que el código no esté duplicado
    for prod in productos:
        if prod["codigo"] == codigo:
            print(f"❌ Error: Ya existe un producto con el código '{codigo}'.")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validar que el valor unitario sea un número válido
    try:
        valor_unitario = float(input("Ingrese el valor unitario: "))
    except ValueError:
        print("❌ Error: El valor unitario debe ser un número válido.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "valor_unitario": valor_unitario
    }
    
    productos.append(nuevo_producto)
    guardar_productos(productos)
    print(f"✅ Producto '{nombre}' agregado y guardado con éxito.")

def listar_productos(productos):
    """Muestra en pantalla todos los productos registrados."""
    print("\n--- LISTA DE PRODUCTOS ---")
    if not productos:
        print("No hay productos registrados actualmente.")
        return

    # Encabezados de la tabla para una mejor visualización
    print(f"{'Código':<15} | {'Nombre del Producto':<30} | {'Valor Unitario':<15}")
    print("-" * 66)
    for prod in productos:
        print(f"{prod['codigo']:<15} | {prod['nombre']:<30} | ${prod['valor_unitario']:<14,.2f}")
    print("-" * 66)

def eliminar_producto(productos):
    """Busca un producto por su código y lo elimina de la lista."""
    print("\n--- ELIMINAR PRODUCTO ---")
    if not productos:
        print("No hay productos registrados para eliminar.")
        return

    codigo_buscar = input("Ingrese el código del producto a eliminar: ").strip()
    
    producto_encontrado = None
    for prod in productos:
        if prod["codigo"] == codigo_buscar:
            producto_encontrado = prod
            break
            
    if producto_encontrado:
        productos.remove(producto_encontrado)
        guardar_productos(productos)
        print(f"🗑️ Producto '{producto_encontrado['nombre']}' eliminado con éxito.")
    else:
        print(f"❌ No se encontró ningún producto con el código '{codigo_buscar}'.")

def menu_principal():
    """Función principal que controla el flujo del menú."""
    # Cargamos los datos guardados al iniciar
    productos = cargar_productos()
    
    while True:
        print("\n================ MENU ================")
        print("1. Agregar producto.")
        print("2. Listar todos los productos.")
        print("3. Eliminar un producto.")
        print("0. Salir.")
        print("======================================")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            listar_productos(productos)
        elif opcion == "3":
            eliminar_producto(productos)
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    menu_principal()