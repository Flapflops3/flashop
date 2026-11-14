# FlaShop

[中文](README.md)

FlaShop connects forms, routes, sessions and a database through a small catalog workflow: add categories and products in an admin interface, then retrieve products through an API. It is a local Flask learning project. Administrators use server-rendered pages, account flows expose JSON endpoints, and SQLite is the default database.

## Try the workflow

Use Python 3.12 from the repository root:

```sh
python -m pip install -r requirements.txt
python shop/manage.py init
python shop/manage.py admin
python shop/run.py
```

Visit `http://127.0.0.1:5000/admin/login` and sign in with the administrator created at the command line. Create a category, add a product, then retrieve the catalog at `/api/products`.

A form submission passes through a route handler, validation and ORM persistence before redirecting to the list page. Login verifies a password hash and creates a session. Session identifiers distinguish user and administrator accounts; profile requests are limited to the current user.

| Location | Responsibility |
| --- | --- |
| `shop/run.py` | Start the local server. |
| `shop/manage.py` | Initialize the database, create an administrator and list routes. |
| `shop/config.py` | Database, session, uploads and environment settings. |
| `shop/flask_online_store/__init__.py` | Application factory and extension/blueprint registration. |
| `shop/flask_online_store/models/` | User, administrator, category, product and related models. |
| `shop/flask_online_store/views/admin/` | Admin login and category/product page handlers. |
| `shop/flask_online_store/views/api/` | Account and catalog endpoints. |
| `shop/flask_online_store/forms/` | Form fields and validators. |
| `shop/flask_online_store/templates/` and `static/` | Templates, styles and browser scripts. |
| `shop/flask_online_store/utils/` | Password hashing, file handling and template helpers. |
| `tests/test_shop.py` | Account isolation and category/product workflow tests. |

Set `SHOP_DATABASE_URL` to change databases. Set `SHOP_SECRET_KEY` to retain a stable session key across restarts; otherwise a temporary key is generated on each launch. Run tests with `python -m unittest discover -s tests -v`.

Orders, payments and full user administration are unfinished. This is a local learning project based on [sunhuachuang/flask-online-store](https://github.com/sunhuachuang/flask-online-store), with its [MIT license](LICENSE) retained.
