


# Sistema de Revenda de Veículos 🚗  

Sistema Web desenvolvido em Django com Bootstrap para gestão de revenda de veículos.  
O sistema permite o cadastro, visualização, atualização e remoção de usuários e carros, além de controle de permissões e autenticação.  
Uma funcionalidade extra permite gerar automaticamente uma bio do cliente utilizando a API Gemini-2.0-Flash-Lite (LLM).

---

## Funcionalidades ✅  

- CRUD completo de Usuários (Cadastro, Listagem, Atualização e Remoção)  
- CRUD completo de Carros (Cadastro, Listagem, Atualização e Remoção)  
- Autenticação de Usuários:  
  - Login  
  - Cadastro  
  - Logout  
- Permissões de Usuários:  
  - Diferentes níveis de acesso (Admin, Usuário Comum)  
- Adição de Bio do Cliente com LLM (Gemini-2.0-Flash-Lite)  
- Integração com Bootstrap para responsividade e estilo do sistema  

---
![design-system-cars-project](https://github.com/user-attachments/assets/f48af386-c80b-4791-9626-e3b4d90ba824)


## Tecnologias Utilizadas 🚀  

- Python 3.12.2  
- Django 5.1.6  
- Bootstrap 5  
- SQLite3  
- Gemini-2.0-Flash-Lite (LLM API)  
- Python-Decouple (Leitura de variáveis de ambiente)  

---

## Instalação e Execução do Projeto 🖥️  

### 1. Clone o Repositório  

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie e Ative o Ambiente Virtual  

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências  

```bash
pip install -r requirements.txt
```

### 4. Realize as Migrações  

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Execute o Projeto  

```bash
python manage.py runserver
```

O sistema estará disponível em:  
```
http://127.0.0.1:8000/
```

---

## Configuração da API Gemini-2.0-Flash-Lite 🤖  

Para utilizar a funcionalidade de geração automática da bio do cliente, é necessário obter e configurar a chave da API do Gemini.

### Obter a Chave da API  

1. Crie uma conta no Google AI Studio:  
https://makersuite.google.com/

2. Gere sua chave de API (Gemini API Key).

### Criar o Arquivo `.env`  

Na raiz do projeto, crie o arquivo `.env` e adicione o seguinte conteúdo:  

```
GEMINI_API_KEY=sua_chave_api_aqui
```

> Substitua `sua_chave_api_aqui` pela chave gerada no Google AI Studio.

### Como o Sistema Lê a Variável  

O sistema utiliza o pacote `python-decouple` para carregar as variáveis do arquivo `.env`.  
No código, a variável é lida da seguinte forma:  

```python
from decouple import config

API_KEY = config('GEMINI_API_KEY')
```

---

## Como Contribuir 💡  

1. Fork este repositório  
2. Crie uma branch com sua feature:  
```bash
git checkout -b minha-feature
```

3. Faça commit das suas alterações:  
```bash
git commit -m 'Adicionando nova feature'
```

4. Suba a branch:  
```bash
git push origin minha-feature
```

5. Abra um Pull Request  

---

