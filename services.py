"""
This module contains all the core operations (CRUD) and statistics
for managing the inventory in memory.
"""


def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Adds a new product to the inventory list.

    Parameters:
        inventario (list): list of product dictionaries
        nombre (str): product name
        precio (float): product price
        cantidad (int): product quantity
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Product added successfully.")


def mostrar_inventario(inventario):
    """
    Displays all products stored in the inventory.
    """
    if len(inventario) == 0:
        print("Inventory is empty.")
    else:
        print("\n--- INVENTORY ---")
        for p in inventario:
            print(p["nombre"], "|", p["precio"], "|", p["cantidad"])


def buscar_producto(inventario, nombre):
    """
    Searches for a product by its name.

    Returns:
        dict if found, otherwise None
    """
    encontrado = None

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            encontrado = p

    return encontrado


def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    """
    Updates the price and quantity of a product.
    """
    producto = buscar_producto(inventario, nombre)

    if producto != None:
        producto["precio"] = nuevo_precio
        producto["cantidad"] = nueva_cantidad
        print("Product updated.")
    else:
        print("Product not found.")


def eliminar_producto(inventario, nombre):
    """
    Removes a product from the inventory.
    """
    producto = buscar_producto(inventario, nombre)

    if producto != None:
        inventario.remove(producto)
        print("Product removed.")
    else:
        print("Product not found.")


def calcular_estadisticas(inventario):
    """
    Calculates and displays basic statistics of the inventory:
    - Total units
    - Total value
    - Most expensive product
    - Product with highest stock
    """
    if len(inventario) == 0:
        print("Inventory is empty.")
    else:
        unidades_totales = 0
        valor_total = 0

        # Initialize with the first product
        mas_caro = inventario[0]
        mayor_stock = inventario[0]

        for p in inventario:
            # Accumulate totals
            unidades_totales = unidades_totales + p["cantidad"]
            valor_total = valor_total + (p["precio"] * p["cantidad"])

            # Check most expensive product
            if p["precio"] > mas_caro["precio"]:
                mas_caro = p

            # Check highest stock
            if p["cantidad"] > mayor_stock["cantidad"]:
                mayor_stock = p

        print("\n--- STATISTICS ---")
        print("Total units:", unidades_totales)
        print("Total value:", valor_total)
        print("Most expensive product:", mas_caro["nombre"], "-", mas_caro["precio"])
        print("Highest stock product:", mayor_stock["nombre"], "-", mayor_stock["cantidad"])