productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], ...
}

def mostrar_stock_marca():
    marca = input("Ingrese la marca a consultar: ").strip().lower()
    total_stock = 0
    modelos_marca = []
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            if modelo in stock:
                total_stock += stock[modelo][1]
                modelos_marca.append((modelo, stock[modelo][1]))
    if total_stock > 0:
        print(f"\nStock total para la marca '{marca}': {total_stock} unidades.")
        print("Detalle por modelo:")
        for modelo, cantidad in modelos_marca:
            print(f" - Modelo {modelo}: {cantidad} unidades")
    else:
        print(f"No se encontraron productos con stock para la marca '{marca}'.")

def busqueda_por_precio():
    try:
        precio_min = int(input("Ingrese el precio mínimo: "))
        precio_max = int(input("Ingrese el precio máximo: "))
    except ValueError:
        print("Debe ingresar números válidos para los precios.")
        return

    encontrados = []
    for modelo, (precio, cantidad) in stock.items():
        if precio_min <= precio <= precio_max and cantidad > 0:
            marca = productos[modelo][0]
            encontrados.append((modelo, marca, precio, cantidad))

    if encontrados:
        print(f"\nProductos con precio entre {precio_min} y {precio_max}:")
        for modelo, marca, precio, cantidad in encontrados:
            print(f"Modelo: {modelo} | Marca: {marca} | Precio: {precio} | Stock: {cantidad}")
    else:
        print("No se encontraron productos dentro del rango de precio indicado con stock disponible.")

def actualizar_precio():
    modelo = input("Ingrese el modelo a actualizar: ").strip()
    if modelo not in stock:
        print("Modelo no encontrado en stock.")
        return
    try:
        nuevo_precio = int(input(f"Ingrese el nuevo precio para el modelo {modelo}: "))
    except ValueError:
        print("Debe ingresar un número válido para el precio.")
        return
    stock[modelo][0] = nuevo_precio
    print(f"Precio actualizado correctamente para el modelo {modelo}.")

def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_stock_marca()
        elif opcion == '2':
            busqueda_por_precio()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
