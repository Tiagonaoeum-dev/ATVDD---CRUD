# Biblioteca API

API REST simples para gerenciamento de Jogos usando Flask + SQLite.

---

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/Tiagonaoeum-dev/ATVDD---CRUD
```

---

### 2. Criar ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Criar banco de dados

```bash
python init_db.py
```

---

### 5. Rodar a API

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000/jogos
```

---

# Testes com CURL

---

## Criar Jogo

```bash
curl -X POST http://127.0.0.1:5000/jogos \
-H "Content-Type: application/json" \
-d "{
  "titulo": "Call of Duty WW2",
  "genero": "FPS",
  "preco": 249.90,
  "estoque": 8
}"
```

---

## Listar todos

```bash
curl http://127.0.0.1:5000/jogos
```

---

## Buscar por ID

```bash
curl http://127.0.0.1:5000/Jogoss/1
```

---

## Atualizar

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 \
-H "Content-Type: application/json" \
-d "{
  "titulo": "Call of Duty WW2",
  "genero": "FPS",
  "preco": 229.90,
  "estoque": 8
}}"
```

---

## Deletar

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

# Critérios atendidos

- ✔ CRUD completo
- ✔ SQL parametrizado (seguro)
- ✔ REST padrão
- ✔ JSON organizado
- ✔ Código limpo
- ✔ Script de inicialização

---

# Melhorias futuras

- Validação de dados
- Paginação
- Autenticação JWT
- Docker
