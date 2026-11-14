# Flask 商城练习

在原项目结构上整理出的本地演示版。保留 `sunhuachuang/flask-online-store` 的 MIT 许可证，见 [LICENSE](LICENSE)。

在仓库根目录安装依赖后：

```sh
python shop/manage.py init
python shop/manage.py admin
python shop/run.py
```

打开 `http://127.0.0.1:5000/admin/login`，用创建管理员时输入的用户名和密码登录。新增分类后可以新增商品。商品列表接口为 `/api/products`，用户接口为 `/api/users` 和 `/api/login`。

默认使用本地 SQLite；原来的多子域路由改为 `/admin` 与 `/api`，不需要修改 hosts 或部署 MySQL、Nginx。数据库、上传文件和本地配置位于 `instance/`，不会进入版本管理。

`SHOP_SECRET_KEY` 可通过环境变量设置；未设置时每次启动生成临时密钥，因此重启后旧会话失效。数据库可通过 `SHOP_DATABASE_URL` 指定。

这是学习项目：已验证注册、登录、访问隔离、分类和商品的基本流程。订单、支付和用户管理页面仍未完成，不适合直接作为面向公众的真实商城部署。
