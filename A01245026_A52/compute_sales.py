"""Script para calcular las ventas totales utilizando datos de dos archivos JSON:
uno para la lista de productos y otro para las ventas."""

import sys
import json
import time


def load_json_data(filename):
    """Carga datos desde un archivo JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except ValueError as e:
        print(f"Error al leer el archivo {filename}: {e}")
        return None
    except FileNotFoundError as e:
        print(f"No se encontró el archivo: {filename}: {e}")
        return None


def calculate_total_sales(prices, sales):
    """Calcula el costo total de las ventas."""
    total_cost = 0
    for sale in sales:
        product_title = sale["Product"]
        quantity = sale["Quantity"]
        if product_title in prices:
            total_cost += prices[product_title] * quantity
        else:
            print(f"Producto no encontrado: {product_title}")
    return total_cost


def main(prices_filename, sales_filename):
    """Carga archivos, realiza cálculos y guarda resultados en un archivo de texto."""
    start_time = time.time()

    # Cargar datos de precios y ventas desde archivos JSON
    products_data = load_json_data(prices_filename)
    sales_data = load_json_data(sales_filename)

    if products_data is None or sales_data is None:
        return

    # Construir diccionario de precios
    prices = {product["title"]: product["price"] for product in products_data}

    # Calcular el costo total de ventas
    total_cost = calculate_total_sales(prices, sales_data)

    # Escribir el resultado en un archivo de texto
    with open('SalesResults.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(f"Costo total de ventas: {total_cost}\n")
        print(f"Costo total de ventas: {total_cost}")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Tiempo total de ejecución: {duration} segundos.")

    # Agregar información de duración al archivo de resultados
    with open('SalesResults.txt', 'a', encoding='utf-8') as outfile:
        outfile.write(f"Tiempo total de ejecución: {duration} segundos.")


if __name__ == '__main__':
    # Verificar si se proporcionan los argumentos necesarios en la línea de comandos
    if len(sys.argv) != 3:
        print("Uso: python computeSales.py prices.json salesRecord.json")
        sys.exit(1)

    # Obtener los nombres de archivo de precios y ventas de los argumentos de línea de comandos
    global_prices_filename = sys.argv[1]
    global_sales_filename = sys.argv[2]

    # Llamar a la función principal con los nombres de archivo proporcionados
    main(global_prices_filename, global_sales_filename)
