import sqlite3

def criar_banco():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Banco criado com sucesso!")

if __name__ == "__main__":
    criar_banco()
