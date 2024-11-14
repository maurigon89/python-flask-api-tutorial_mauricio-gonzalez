from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False},
]

# Ruta para obtener todos los todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# Ruta para agregar un todo
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify(todos), 201

# Ruta para eliminar un todo por posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Position not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)