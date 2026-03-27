"""
This module handles CSV file operations:
- Saving inventory to a file
- Loading inventory from a file
"""

import csv


def guardar_csv(inventario, ruta):
    """
    Saves the inventory into a CSV file.

    Parameters:
        inventario (list): list of products
        ruta (str): file path
    """
    if len(inventario) == 0:
        print("Inventory is empty, cannot save.")
    else:
        try:
            archivo = open(ruta, "w", newline="", encoding="utf-8")
            writer = csv.writer(archivo)

            # Write header
            writer.writerow(["nombre", "precio", "cantidad"])

            # Write product data
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

            archivo.close()
            print("File saved at:", ruta)

        except:
            print("Error while saving file.")


def cargar_csv(ruta):
    """
    Loads inventory data from a CSV file.

    Returns:
        list: list of valid products
    """
    productos = []
    errores = 0

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        reader = csv.reader(archivo)

        # Read header
        header = next(reader)

        if header != ["nombre", "precio", "cantidad"]:
            print("Invalid header.")
        else:
            for fila in reader:

                # Validate number of columns
                if len(fila) == 3:
                    try:
                        nombre = fila[0]
                        precio = float(fila[1])
                        cantidad = int(fila[2])

                        # Validate non-negative values
                        if precio >= 0 and cantidad >= 0:
                            producto = {
                                "nombre": nombre,
                                "precio": precio,
                                "cantidad": cantidad
                            }
                            productos.append(producto)
                        else:
                            errores = errores + 1

                    except:
                        # Conversion error
                        errores = errores + 1
                else:
                    errores = errores + 1

        archivo.close()

    except:
        print("ERROR")
    return productos