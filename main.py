"""
Main application file.
Handles user interaction through a console menu.
"""

from services import *
from file_manager import *


inventario = []
salir = False

# Main loop controlled by a boolean variable (not while True)
while salir == False:

    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Load CSV")
    print("9. Exit")

    opcion = input("Select an option: ")

    # Add product
    if opcion == "1":
        nombre = input("Name: ")
        precio = float(input("Price: "))
        cantidad = int(input("Quantity: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    # Show inventory
    elif opcion == "2":
        mostrar_inventario(inventario)

    # Search product
    elif opcion == "3":
        nombre = input("Product name: ")
        p = buscar_producto(inventario, nombre)

        if p != None:
            print(p)
        else:
            print("Product not found.")

    # Update product
    elif opcion == "4":
        nombre = input("Product name: ")
        precio = float(input("New price: "))
        cantidad = int(input("New quantity: "))
        actualizar_producto(inventario, nombre, precio, cantidad)

    # Delete product
    elif opcion == "5":
        nombre = input("Product name: ")
        eliminar_producto(inventario, nombre)

    # Show statistics
    elif opcion == "6":
        calcular_estadisticas(inventario)

    # Save CSV
    elif opcion == "7":
        ruta = input("File path: ")
        guardar_csv(inventario, ruta)

    # Load CSV
    elif opcion == "8":
        ruta = input("File path: ")
        nuevos = cargar_csv(ruta)

        decision = input("Overwrite current inventory? (S/N): ")

        if decision == "S":
            inventario = nuevos
            print("Inventory replaced.")
        else:
            # Merge inventories
            for nuevo in nuevos:
                existe = buscar_producto(inventario, nuevo["nombre"])

                if existe != None:
                    # Update quantity and price
                    existe["cantidad"] = existe["cantidad"] + nuevo["cantidad"]
                    existe["precio"] = nuevo["precio"]
                else:
                    inventario.append(nuevo)

            print("Inventory merged.")

    # Exit program
    elif opcion == "9":
        salir = True
        print("Program finished.")

    else:
        print("Invalid option.")