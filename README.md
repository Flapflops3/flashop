# FlaShop

[English](README.en.md)

从后台添加分类和商品，到通过接口读取商品列表，FlaShop 用一个小商城串起表单、路由、会话和数据库。项目面向 Flask 学习与本地演示：管理员操作模板页面，用户注册和登录使用 JSON 接口，数据默认存入 SQLite。

## 先走一遍流程

使用 Python 3.12，在仓库根目录执行：

```sh
python -m pip install -r requirements.txt
python shop/manage.py init
python shop/manage.py admin
python shop/run.py
```

打开 `http://127.0.0.1:5000/admin/login`，使用命令行创建的管理员账号登录。先新增分类，再录入商品；访问 `/api/products` 可以读取商品列表。

一次后台提交依次经过路由、表单验证和 ORM 持久化，随后重定向到列表页。登录时校验密码哈希并建立会话；会话标识区分普通用户和管理员，用户接口只返回当前账号可访问的信息。

## 文件与分工

| 位置 | 作用 |
| --- | --- |
| `shop/run.py` | 启动本地服务。 |
| `shop/manage.py` | 初始化数据库、创建管理员、列出路由。 |
| `shop/config.py` | SQLite、会话、上传目录和环境变量配置。 |
| `shop/flask_online_store/__init__.py` | 创建应用，注册数据库、蓝图、上传组件和登录管理器。 |
| `shop/flask_online_store/models/` | 定义用户、管理员、分类、商品及关联数据模型。 |
| `shop/flask_online_store/views/admin/` | 后台登录、分类与商品页面的请求处理。 |
| `shop/flask_online_store/views/api/` | 注册登录、用户资料和商品读取接口。 |
| `shop/flask_online_store/forms/` | 表单字段和验证规则。 |
| `shop/flask_online_store/templates/`、`static/` | 页面模板、样式及浏览器脚本。 |
| `shop/flask_online_store/utils/` | 密码哈希、文件处理与模板辅助函数。 |
| `tests/test_shop.py` | 注册登录、权限隔离、分类创建、商品录入和读取流程测试。 |

`SHOP_DATABASE_URL` 可以替换数据库地址。设置 `SHOP_SECRET_KEY` 可让会话密钥在重启间保持一致；未设置时每次启动生成临时密钥。测试命令是 `python -m unittest discover -s tests -v`。

订单、支付和完整用户管理仍未实现。目前定位为本地学习项目。项目基于 [sunhuachuang/flask-online-store](https://github.com/sunhuachuang/flask-online-store)，保留 [MIT 许可证](LICENSE)。
