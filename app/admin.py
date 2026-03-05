from flask_login import current_user
from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from .extensions import admin_panel, db
from .models import User, Producto  

class SecurityModelView(ModelView):
    column_exclude_list = ["password"]

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))

def configuracion_admin():
    admin_panel.add_view(SecurityModelView(User, db.session))
    admin_panel.add_view(SecurityModelView(Producto, db.session))  # Tabla de Producto en Admin