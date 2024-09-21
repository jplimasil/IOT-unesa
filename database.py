import sqlite3
import bcrypt

# Inicializa o banco de dados
def init_db():
    try:
        conn = sqlite3.connect('gym_usage.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipment_id TEXT,
                user_id INTEGER,
                timestamp REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        conn.close()

# Adiciona um uso de equipamento ao banco de dados
def add_usage(equipment_id, user_id, timestamp):
    try:
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usages (equipment_id, user_id, timestamp) VALUES (?, ?, ?)
            ''', (equipment_id, user_id, timestamp))
            conn.commit()
    except Exception as e:
        print(f"Erro ao adicionar uso: {e}")

# Obtém todos os registros de uso
def get_usages():
    try:
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username=?', (username,))
            stored_password = cursor.fetchone()
            print(f"Senha armazenada: {stored_password}")
            if stored_password and verify_password(stored_password[0], password):
                print("Autenticação bem-sucedida")
                return True
            else:
                print("Autenticação falhou")
            return False
    except Exception as e:
        print(f"Erro ao obter usuário: {e}")
        return False

# Adiciona um novo usuário com senha hash
def add_user(username, password):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"Erro: Nome de usuário '{username}' já existe.")
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")

# Verifica se o usuário existe e se a senha está correta
def get_user(username, password):
    try:
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username=?', (username,))
            stored_password = cursor.fetchone()
            if stored_password and bcrypt.checkpw(password.encode('utf-8'), stored_password[0]):
                return True
            return False
    except Exception as e:
        print(f"Erro ao obter usuário: {e}")
        return False

# Adiciona um usuário padrão (admin)
def create_default_user():
    add_user('username', 'password')  # Altere para um nome de usuário e senha desejados.

# Filtra usos por usuário
def get_usages_by_user(user_id):
    try:
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usages WHERE user_id=?', (user_id,))
            usages = cursor.fetchall()
            return [{"id": u[0], "equipment_id": u[1], "user_id": u[2], "timestamp": u[3]} for u in usages]
    except Exception as e:
        print(f"Erro ao filtrar usos por usuário: {e}")
        return []

# Filtra usos por equipamento
def get_usages_by_equipment(equipment_id):
    try:
        with sqlite3.connect('gym_usage.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM usages WHERE equipment_id=?', (equipment_id,))
            usages = cursor.fetchall()
            return [{"id": u[0], "equipment_id": u[1], "user_id": u[2], "timestamp": u[3]} for u in usages]
    except Exception as e:
        print(f"Erro ao filtrar usos por equipamento: {e}")
        return []

# Inicializa o banco de dados e cria o usuário padrão
if __name__ == "__main__":
    init_db()
    create_default_user()
