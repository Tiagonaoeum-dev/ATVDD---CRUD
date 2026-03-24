import sqlite3

def criar_banco():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER,
        disponivel BOOLEAN DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco()
