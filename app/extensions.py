from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate  # Para migraciones

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"

admin_panel = Admin(name="Panel Administrador")
migrate = Migrate()