from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from database import init_db, add_usage, get_usages, add_user, get_user
from forms import LoginForm
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

# Inicializa o banco de dados
init_db()

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.username.data, form.password.data)
        if user:
            login_user(User(user[0]))
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    usages = get_usages()
    return render_template('index.html', usages=usages)

@app.route('/api/usage', methods=['POST'])
def log_usage():
    data = request.get_json()
    equipment_id = data['equipment_id']
    user_id = data['user_id']
    timestamp = data['timestamp']
    
    add_usage(equipment_id, user_id, timestamp)
    return jsonify({"message": "Usage logged successfully!"}), 201 
@app.route('/report', methods=['GET', 'POST'])
@login_required
def report():
    # Gerar relatorio de uso
    # Implementar relatorio
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
