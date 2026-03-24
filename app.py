from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DB_NAME = "database.db"

def executar_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, params)

        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()

    return resultado


# GET - Listar todos
@app.route('/livros', methods=['GET'])
def listar_livros():
    dados = executar_query("SELECT * FROM livros", fetch=True)
    return jsonify([dict(l) for l in dados]), 200


# GET - Buscar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = executar_query("SELECT * FROM livros WHERE id = ?", (id,), fetch=True)

    if livro:
        return jsonify(dict(livro[0])), 200
    return jsonify({"erro": "Livro não encontrado"}), 404


# POST - Inserir
@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()

    executar_query("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (
        dados.get("titulo"),
        dados.get("autor"),
        dados.get("ano"),
        dados.get("disponivel", True)
    ), commit=True)

    return jsonify({"mensagem": "Livro criado com sucesso"}), 201


# PUT - Atualizar
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = request.get_json()

    existe = executar_query("SELECT id FROM livros WHERE id = ?", (id,), fetch=True)
    if not existe:
        return jsonify({"erro": "Livro não encontrado"}), 404

    executar_query("""
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?, disponivel = ?
        WHERE id = ?
    """, (
        dados.get("titulo"),
        dados.get("autor"),
        dados.get("ano"),
        dados.get("disponivel"),
        id
    ), commit=True)

    return '', 204


# DELETE - Remover o livro selecionado pelo comando
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = executar_query("SELECT * FROM livros WHERE id = ?", (id,), fetch=True)

    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    executar_query("DELETE FROM livros WHERE id = ?", (id,), commit=True)

    return jsonify({"mensagem": "Livro removido com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)
