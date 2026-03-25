from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def executar_query(query, *args, fetch=False, commit=False):
    conn = sqlite3.connect('loja.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, args)

        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()

    return resultado


# GET - Listar todos
@app.route('/jogos', methods=['GET'])
def listar_jogos():
    dados = executar_query("SELECT * FROM jogos", fetch=True)
    jogos = [dict(jogo) for jogo in dados]
    return jsonify(jogos), 200


# GET - Buscar por ID
@app.route('/jogos/<int:id>', methods=['GET'])
def buscar_jogo(id):
    jogo = executar_query("SELECT * FROM jogos WHERE id = ?", id, fetch=True)

    if jogo:
        return jsonify(dict(jogo[0])), 200
    return jsonify({"erro": "Jogo não encontrado"}), 404


# POST - Inserir
@app.route('/jogos', methods=['POST'])
def inserir_jogo():
    dados = request.get_json()

    executar_query(
        "INSERT INTO jogos (titulo, genero, preco, estoque) VALUES (?, ?, ?, ?)",
        dados.get('titulo'),
        dados.get('genero'),
        dados.get('preco'),
        dados.get('estoque'),
        commit=True
    )

    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201


# PUT - Atualizar
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    existe = executar_query("SELECT id FROM jogos WHERE id = ?", id, fetch=True)
    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "UPDATE jogos SET titulo = ?, genero = ?, preco = ?, estoque = ? WHERE id = ?",
        dados.get('titulo'),
        dados.get('genero'),
        dados.get('preco'),
        dados.get('estoque'),
        id,
        commit=True
    )

    return '', 204


# ❌ DELETE - Remover
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query("SELECT titulo FROM jogos WHERE id = ?", id, fetch=True)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query("DELETE FROM jogos WHERE id = ?", id, commit=True)

    return jsonify({"mensagem": f"Jogo '{jogo[0]['titulo']}' removido!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
