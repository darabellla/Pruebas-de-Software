"""Script que calcula el total de ventas utilizando dos archivos JSON: uno que contiene la lista de productos y otro que registra las ventas."""

import sys
import json
import time


def load_json_data(filename):
    """Importa información desde un archivo en formato JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except ValueError as e:
        print(f"Falló al procesar la lectura del archivo {filename}: {e}")
        return None
    except FileNotFoundError as e:
        print(f"No se encontro el archivo: {filename}: {e}")
        return None


def calculate_total_sales(prices, sales):
    """Determina el gasto total resultante de todas las transacciones."""
    total_cost = 0
    for sale in sales:
        product_title = sale["Product"]
        quantity = sale["Quantity"]
        if product_title in prices:
            total_cost += prices[product_title] * quantity
        else:
            print(f"El producto no se encuentra en el catálogo: {product_title}")
    return total_cost


def main(prices_filename, sales_filename):
    """Leer archivos, generar un archivo de texto y registrar los resultados."""
    start_time = time.time()
    
    # Cargar datos de productos y ventas desde archivos JSON
    products_data = load_json_data(prices_filename)
    sales_data = load_json_data(sales_filename)

    if products_data is None or sales_data is None:
        return

    # Construir diccionario de precios a partir de datos de productos
    prices = {product["title"]: product["price"] for product in products_data}

    # Calcular el costo total de las ventas
    total_cost = calculate_total_sales(prices, sales_data)

    # Escribir resultados en un archivo de texto
    with open('SalesResults.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(f"Costo total de ventas: {total_cost}\n")
        print(f"Costo total de ventas: {total_cost}")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Tiempo total de ejecución: {duration} segundos.")
    
    # Añadir tiempo total de ejecución al archivo de resultados
    with open('SalesResults.txt', 'a', encoding='utf-8') as outfile:
        outfile.write(f"Tiempo total de ejecución: {duration} segundos.")


if __name__ == '__main__':
    # Verificar que se proporcionen dos argumentos de línea de comandos
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py prices.json salesRecord.json")
        sys.exit(1)

    # Obtener nombres de archivos de la línea de comandos
    global_prices_filename = sys.argv[1]
    global_sales_filename = sys.argv[2]

    # Llamar a la función principal con los nombres de archivos proporcionados
    main(global_prices_filename, global_sales_filename)
