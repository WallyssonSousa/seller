# 📦 API de Gestão de Sellers, Produtos e Vendas

API para gerenciamento de **sellers**, **produtos** e **vendas** com autenticação JWT e validações de status.

---

## 🔐 Autenticação

Todos os endpoints que alteram dados (produtos e vendas) exigem token JWT obtido no login.  

**Exemplo de header de autenticação:**

```

http
Authorization: Bearer SEU_TOKEN

```

1️⃣ Cadastro e Ativação de Seller
1.1 Criar Seller

```

POST /auth/users

Payload:

{
  "name": "Loja Teste",
  "cnpj": "12345678000171",
  "email": "seller@example2.com",
  "celular": "11997135477",
  "password": "senha1234"
}


curl -X POST "http://127.0.0.1:5000/auth/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "Loja Teste", "cnpj": "12345678000171", "email": "seller@example2.com", "celular": "", "password": ""}'

```

1.2 Ativar Seller

```
POST /auth/users/verificar

Payload:

{
  "celular": "",
  "code": ""
}

Exemplo curl:

curl -X POST "http://127.0.0.1:5000/auth/users/verificar" \
     -H "Content-Type: application/json" \
     -d '{"celular": "", "code": ""}'

```

2️⃣ Login

```
POST /auth/login

Payload:

{
  "email": "seller@example2.com",
  "password": ""
}


curl -X POST "http://127.0.0.1:5000/auth/login" \
     -H "Content-Type: application/json" \
     -d '{"email": "seller@example2.com", "password": ""}'



Retorno esperado:
Token JWT que deve ser usado nos endpoints protegidos.

```


3️⃣ Gerenciamento de Produtos
3.1 Criar Produto

```
POST /product

Headers: Authorization: Bearer SEU_TOKEN

Payload:

{
  "nome": "MacBook Pro Apple 14",
  "preco": 13999,
  "quantidade": 10,
  "status": "Active",
  "image": "https://www.kabum.com.br/imagem.jpg"
}


curl -X POST "http://127.0.0.1:5000/product" \
     -H "Authorization: Bearer SEU_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"nome": "MacBook Pro Apple 14", "preco": 13999, "quantidade": 10, "status": "Active", "image": "https://www.kabum.com.br/imagem.jpg"}'

```

3.2 Listar Produtos

```

GET /product

Headers: Authorization: Bearer SEU_TOKEN

Exemplo curl:

curl -X GET "http://127.0.0.1:5000/product" \
     -H "Authorization: Bearer SEU_TOKEN"

```


3.3 Ver Produto

```
GET /product/<int:product_id>

Headers: Authorization: Bearer SEU_TOKEN


curl -X GET "http://127.0.0.1:5000/product/1" \
     -H "Authorization: Bearer SEU_TOKEN"

```

3.4 Editar Produto

```

PUT /product/<int:product_id>

Headers: Authorization: Bearer SEU_TOKEN

Payload:

{
  "nome": "MacBook Pro Apple 14 M1",
  "preco": 14500,
  "quantidade": 8,
  "status": "Active"
}


curl -X PUT "http://127.0.0.1:5000/product/1" \
     -H "Authorization: Bearer SEU_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"nome": "MacBook Pro Apple 14 M1", "preco": 14500, "quantidade": 8, "status": "Active"}'

```

3.5 Inativar Produto

```

PATCH /product/<int:product_id>/inactivate

Headers: Authorization: Bearer SEU_TOKEN


curl -X PATCH "http://127.0.0.1:5000/product/1/inactivate" \
     -H "Authorization: Bearer SEU_TOKEN"

```

4️⃣ Gerenciamento de Sellers


4.1 Listar Sellers

```

GET /auth/users

Headers: Authorization: Bearer SEU_TOKEN

Exemplo curl:

curl -X GET "http://127.0.0.1:5000/auth/users" \
     -H "Authorization: Bearer SEU_TOKEN"

```

4.2 Ver Detalhes do Seller


```
GET /auth/users/<int:user_id>

Headers: Authorization: Bearer SEU_TOKEN

Exemplo curl:

curl -X GET "http://127.0.0.1:5000/auth/users/1" \
     -H "Authorization: Bearer SEU_TOKEN"

```

4.3 Editar Seller

```

PUT /auth/users/<int:user_id>

Headers: Authorization: Bearer SEU_TOKEN

Payload:

{
  "name": "Loja Teste Atualizada",
  "cnpj": "12345678000171",
  "email": "seller@example2.com",
  "celular": "",
  "password": ""
}


curl -X PUT "http://127.0.0.1:5000/auth/users/1" \
     -H "Authorization: Bearer SEU_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Loja Teste Atualizada", "cnpj": "12345678000171", "email": "seller@example2.com", "celular": "", "password": ""}'

```

5️⃣ Vendas
5.1 Criar Venda

```
POST /sale

Headers: Authorization: Bearer SEU_TOKEN

Payload:

{
  "product_id": 1,
  "quantity": 2
}

Regras de negócio:

Não vender mais que a quantidade em estoque.

Produtos inativos não podem ser vendidos.

Sellers inativos não podem realizar vendas.

curl -X POST "http://127.0.0.1:5000/sale" \
     -H "Authorization: Bearer SEU_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"product_id": 1, "quantity": 2}'

```

5.2 Listar Vendas

```

GET /sale

Headers: Authorization: Bearer SEU_TOKEN

curl -X GET "http://127.0.0.1:5000/sale" \
     -H "Authorization: Bearer SEU_TOKEN"

```

5.3 Ver Detalhes da Venda

```

GET /sale/<int:sale_id>

Headers: Authorization: Bearer SEU_TOKEN

Exemplo curl:

curl -X GET "http://127.0.0.1:5000/sale/1" \
     -H "Authorization: Bearer SEU_TOKEN"

```