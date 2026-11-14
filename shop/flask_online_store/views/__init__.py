from flask import Blueprint
from flask_restful import Resource, Api
from .api.user import UserView
from .api.order import OrderView
from .api.product import ProductView
from .api.security import LoginView, LogoutView

from .admin import admin_static
from .admin.user import admin_user
from .admin.order import admin_order
from .admin.product import admin_product
from .admin.category import admin_category
from .admin.security import admin_security


def register_blueprints(app):

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(UserView, '/users', '/users/<int:id>')
    api.add_resource(OrderView, '/orders', '/orders/<int:id>')
    api.add_resource(ProductView, '/products', '/products/<int:id>')
    api.add_resource(LoginView, '/login')
    api.add_resource(LogoutView, '/logout')

    app.register_blueprint(api_bp, url_prefix='/api')

    app.register_blueprint(admin_security, url_prefix='/admin')
    app.register_blueprint(
        admin_static, url_prefix='/admin/static')
    app.register_blueprint(admin_user, url_prefix='/admin/users')
    app.register_blueprint(
        admin_order, url_prefix='/admin/orders')
    app.register_blueprint(
        admin_product, url_prefix='/admin/products')
    app.register_blueprint(
        admin_category, url_prefix='/admin/categories')
