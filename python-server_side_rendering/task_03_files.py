from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Fonction pour lire et parser le fichier JSON
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Fonction pour lire et parser le fichier CSV
def read_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Route pour afficher les produits en fonction du paramètre source (json ou csv)
@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source == 'json':
        try:
            products_data = read_json('products.json')
        except FileNotFoundError:
            error_message = "File 'products.json' not found."
            return render_template('product_display.html', error=error_message)
        except json.JSONDecodeError:
            error_message = "Error decoding JSON file."
            return render_template('product_display.html', error=error_message)
    elif source == 'csv':
        try:
            products_data = read_csv('products.csv')
        except FileNotFoundError:
            error_message = "File 'products.csv' not found."
            return render_template('product_display.html', error=error_message)
        except Exception as e:
            error_message = f"Error reading CSV file: {str(e)}"
            return render_template('product_display.html', error=error_message)
    else:
        error_message = "Wrong source parameter. Use 'json' or 'csv'."
        return render_template('product_display.html', error=error_message)

    if id_param:
        filtered_products = [product for product in products_data if str(product.get('id')) == id_param]
        if not filtered_products:
            error_message = f"Product with id={id_param} not found."
            return render_template('product_display.html', error=error_message)
        return render_template('product_display.html', products=filtered_products)
    else:
        return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True)
