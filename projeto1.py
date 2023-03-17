from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados em memória
products = [
    {"id": 1, "name": "PlayStation 5", "price": 4000.0},
    {"id": 2, "name": "Pc Gamer", "price": 6000.0},
    {"id": 3, "name": "Drone", "price": 1000.0}
]

# Operação READ: Retorna todos os produtos
@app.route('/products')
def get_products():
    return jsonify(products)

# Operação READ: Retorna um produto pelo ID
@app.route('/products/<int:product_id>')
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'})

# Operação CREATE: Adiciona um novo produto
@app.route('/products', methods=['POST'])
def add_product():
    product = request.json
    product['id'] = len(products) + 1
    products.append(product)
    return jsonify(product)

# Operação UPDATE: Atualiza um produto pelo ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    for product in products:
        if product['id'] == product_id:
            product.update(request.json)
            return jsonify(product)
    return jsonify({'error': 'Produto não encontrado'})

# Operação DELETE: Remove um produto pelo ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            return jsonify({'message': 'Produto removido com sucesso'})
    return jsonify({'error': 'Produto não encontrado'})

if __name__ == '__main__':
    app.run(debug=True)
    