# 🚗 Ticket Veículos

Sistema de controle de acesso de veículos para condomínios, utilizando tags para registro de entrada e saída.

---

## 📌 Descrição

Este projeto simula um sistema de portaria para gerenciamento de veículos, permitindo:

- Cadastro de veículos
- Registro de entrada e saída
- Consulta de veículos cadastrados
- Persistência de dados em JSON
- Estrutura preparada para banco relacional (SQLite)

---

## 🧠 Arquitetura

O projeto foi estruturado em camadas para facilitar manutenção e escalabilidade:

- **models/** → definição das entidades (Veículo)
- **services/** → regras de negócio
- **repositories/** → persistência de dados (JSON / SQLite)
- **data/** → armazenamento dos dados

---

## ⚙️ Tecnologias utilizadas

- Python
- JSON (persistência)
- SQLite (em desenvolvimento)
- Pandas (visualização de dados)

---

## 🚀 Como executar o projeto

```bash
# Clonar repositório
git clone https://github.com/Gabriel-Reis021/ticket-veiculos.git

# Entrar na pasta
cd ticket-veiculos

# Executar
python main.py
