# Gerenciador de Estudo e Habilidades CLI

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em Python para rastrear o progresso em módulos de estudo, cursos e habilidades técnicas. Ele demonstra proficiência na integração de Python com um banco de dados NoSQL.

---

## 🚀 Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **MongoDB:** Banco de dados NoSQL utilizado para persistência de dados.
- **PyMongo:** Driver oficial do MongoDB para Python.

---

## ✨ Funcionalidades (CRUD Completo)

O aplicativo oferece um menu interativo com as seguintes operações:

- **CREATE:** Adicionar novos módulos de estudo.
- **READ:** Listar todos os módulos e seus status.
- **UPDATE:** Atualizar o status (Ex: "Iniciado" para "Concluído") e o tempo gasto.
- **DELETE:** Remover módulos finalizados.

---

## 🛠️ Como Executar o Projeto

### Pré-requisitos

1.  **Python 3.10+** instalado.
2.  **MongoDB Server** instalado e rodando (pode ser localmente via Compass).

### 1. Clonar o Repositório

```bash
git clone https://github.com/VitorTFraga/Gerenciador-de-Estudo-CLI.git
cd Gerenciador-de-Estudo-CLI
```

### 2. Instalar Dependências

Instale a biblioteca Python PyMongo usando o arquivo requirements.txt:

```bash
 pip install -r requirements.txt
```

### 3. Configurar o Banco de Dados

1. Verifique se o seu servidor MongoDB está rodando na porta padrão (27017).
2. Edite o arquivo mongo_db_config.py caso você precise alterar o HOST, PORT ou o nome do Database (DB_NAME).

### 4. Executar o Programa

Inicie a aplicação de gerenciamento CLI:

```bash
python app.py
```

---

## 🪪 Contatos

Vitor Táboas Fraga - [LINKEDIN](https://www.linkedin.com/in/vitor-táboas-fraga-002651212) - vitortaboasfraga@gmail.com

Link do Projeto: [Gerenciado de Estudos CLI](https://github.com/VitorTFraga/Gerenciador-de-Estudo-CLI)

