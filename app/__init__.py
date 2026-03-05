import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
from .extensions import db, login_manager, admin_panel, migrate
from .admin import configuracion_admin

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # Se inicializa las migraciones
    login_manager.init_app(app)
    admin_panel.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    configuracion_admin()

    return app