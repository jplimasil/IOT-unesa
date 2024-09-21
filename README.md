# Sistema de Controle de Uso de Equipamentos de Academia

Este é um sistema básico de controle de uso de equipamentos de uma academia, desenvolvido em Python utilizando o framework Flask para o back-end e SQLite para o banco de dados. O objetivo é permitir o monitoramento do uso de equipamentos pelos usuários da academia e garantir um ambiente controlado e eficiente para os administradores.

## Funcionalidades

- **Registro de uso de equipamentos**: Cada vez que um usuário utiliza um equipamento, o sistema registra o ID do equipamento, o ID do usuário e a data/hora do uso.
- **Autenticação de usuários**: Um sistema simples de login e senha permite que apenas usuários autenticados registrem o uso.
- **Visualização de registros**: O administrador pode visualizar todos os registros de uso.
- **Criação de usuários**: O sistema permite a criação de novos usuários com nome de usuário e senha.

## Requisitos

- Python 3.7+
- Flask
- SQLite
- Bcrypt (para hash de senhas)

As dependências necessárias estão listadas no arquivo `requirements.txt` e podem ser instaladas com o seguinte comando:

```bash
pip install -r requirements.txt


