# Biblioteca API

API REST simples para gerenciamento de livros usando Flask + SQLite.

---

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/biblioteca-api.git
cd biblioteca-api
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
http://127.0.0.1:5000
```

---

# Testes com CURL

---

## Criar livro

```bash
curl -X POST http://127.0.0.1:5000/livros \
-H "Content-Type: application/json" \
-d '{"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899}'
```

---

## Listar todos

```bash
curl http://127.0.0.1:5000/livros
```

---

## Buscar por ID

```bash
curl http://127.0.0.1:5000/livros/1
```

---

## Atualizar

```bash
curl -X PUT http://127.0.0.1:5000/livros/1 \
-H "Content-Type: application/json" \
-d '{"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1900, "disponivel": false}'
```

---

## Deletar

```bash
curl -X DELETE http://127.0.0.1:5000/livros/1
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
