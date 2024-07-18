from flask import Flask, request, render_template
import csv
import json
import sqlite3

app = Flask(__name__)

def get_data_from_csv():
    data = []
    with open('products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_data_from_json():
    with open('products.json') as jsonfile:
        data = json.load(jsonfile)
    return data

def get_data_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    if source == 'csv':
        data = get_data_from_csv()
    elif source == 'json':
        data = get_data_from_json()
    elif source == 'sql':
        data = get_data_from_sql()
        if data is None:
            return "Database error", 500
    else:
        return "Wrong source", 400
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
